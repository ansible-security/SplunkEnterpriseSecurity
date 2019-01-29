#!/usr/bin/python
# -*- coding: utf-8 -*-

# (c) 2018, Adam Miller (admiller@redhat.com)
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)


from ansible.module_utils.urls import Request, CertificateError
from ansible.module_utils.six.moves.urllib.parse import urlencode, quote_plus
from ansible.module_utils.connection import ConnectionError
from ansible.module_utils.six.moves.urllib.error import HTTPError

import json
from functools import wraps

try:
    import splunklib.client
    HAS_SPLUNKLIB = True
except ImportError:
    HAS_SPLUNKLIB = False

SPLUNK_COMMON_ARGSPEC = dict(
    splunk_username=dict(required=True, type='str'),
    splunk_password=dict(required=True, type='str', no_log=True),
    splunk_servername=dict(required=True, type='str'),
    splunk_port=dict(required=False, type='int', default=8089),
    splunk_scheme=dict(required=False, type='str', default="https"),
    validate_certs=dict(required=False, type='bool', default=True),
)

def get_splunk_client(module):
    splunk_client = splunklib.client.connect(
        host=module.params['splunk_servername'],
        port=module.params['splunk_port'],
        username=module.params['splunk_username'],
        password=module.params['splunk_password'],
        scheme=module.params['splunk_scheme'],
        verify=module.params['validate_certs']
    )
    return splunk_client

def splunk_sanity_check(module):
    if not HAS_SPLUNKLIB:
        module.fail_json("This module requires splunk-sdk (https://pypi.org/project/splunk-sdk/) be installed")

def parse_splunk_args(module):
    """
    Get the valid fields that should be passed to the REST API as urlencoded
    data so long as the argument specification to the module follows the
    convention:
        1) name field is Required to be passed as data to REST API
        2) all module argspec items that should be passed to data are not
            Required by the module and are set to default=None
    """
    try:
        splunk_data = {}
        for argspec in module.argument_spec:
            if "default" in module.argument_spec[argspec] \
                    and module.argument_spec[argspec]["default"] is None \
                    and module.params[argspec] is not None:
                splunk_data[argspec] = module.params[argspec]
        return splunk_data
    except TypeError as e:
        module.fail_json(msg="Invalid data type provided for splunk module_util.parse_splunk_args: {0}".format(e))

class SplunkRequest(object):
    def __init__(self, module, headers=None, keymap={}, not_rest_data_keys=[]):
        self.request = Request(
            url_username=module.params['splunk_username'],
            url_password=module.params['splunk_password'],
            force_basic_auth=True,
            headers=headers
        )
        self.module = module

        # The Splunk REST API endpoints often use keys that aren't pythonic so
        # we need to handle that with a mapping to allow keys to be proper
        # variables in the module argspec
        self.keymap = keymap

        # This allows us to exclude specific argspec keys from being included by
        # the rest data that don't follow the splunk_* naming convention
        self.not_rest_data_keys = not_rest_data_keys
        self.not_rest_data_keys.append('validate_certs')

    def _request_error_handle(f):
        @wraps(f)
        def wrap(self, url, **kwargs):
            try:
                return f(self, url, **kwargs)
            except ConnectionError as e:
                self.module.fail_json(msg="connection error occurred: {0}".format(e))
            except CertificateError as e:
                self.module.fail_json(msg="certificate error occurred: {0}".format(e))
            except ValueError as e:
                self.module.fail_json(msg="certificate not found: {0}".format(e))
        return wrap

    @_request_error_handle
    def get(self, url, **kwargs):
        return self.request.get(url, **kwargs)

    @_request_error_handle
    def put(self, url, **kwargs):
        return self.request.put(url, **kwargs)

    @_request_error_handle
    def post(self, url, **kwargs):
        return self.request.post(url, **kwargs)

    @_request_error_handle
    def delete(self, url, **kwargs):
        return self.request.delete(url, **kwargs)


    def get_data(self):
        """
        Get the valid fields that should be passed to the REST API as urlencoded
        data so long as the argument specification to the module follows the
        convention:
            - the key to the argspec item does not start with splunk_
            - the key does not exist in the not_data_keys list
        """
        try:
            splunk_data = {}
            for param in self.module.params:
                if self.module.params[param] != None \
                        and not param.startswith('splunk_') \
                        and not param in self.not_rest_data_keys:
                    if param in self.keymap:
                        splunk_data[self.keymap[param]] = self.module.params[param]
                    else:
                        splunk_data[param] = self.module.params[param]
            return splunk_data


        except TypeError as e:
            self.module.fail_json(msg="invalid data type provided: {0}".format(e))

    def get_urlencoded_data(self):
        return urlencode(self.get_data())

    def get_by_path(self, rest_path):
        """
        GET attributes of a monitor by rest path
        """

        get_json = self.get(
            "{0}://{1}:{2}/{3}?output_mode=json".format(
                self.module.params['splunk_scheme'],
                self.module.params['splunk_servername'],
                self.module.params['splunk_port'],
                rest_path,
            ),
            validate_certs=self.module.params['validate_certs']
        ).read()

        return json.loads(get_json)

    def delete_by_path(self, rest_path):
        """
        DELETE attributes of a monitor by rest path
        """

        get_json = self.delete(
            "{0}://{1}:{2}/{3}?output_mode=json".format(
                self.module.params['splunk_scheme'],
                self.module.params['splunk_servername'],
                self.module.params['splunk_port'],
                rest_path,
            ),
            validate_certs=self.module.params['validate_certs']
        ).read()

        return json.loads(get_json)

    def create_update(self, rest_path, data=None):
        """
        Create or Update a file/directory monitor data input in Splunk
        """
        if data == None:
            data = self.get_urlencoded_data()
        post_json = self.post(
            "{0}://{1}:{2}/{3}?output_mode=json".format(
                self.module.params['splunk_scheme'],
                self.module.params['splunk_servername'],
                self.module.params['splunk_port'],
                rest_path
            ),
            validate_certs=self.module.params['validate_certs'],
            data=data
        ).read()

        return json.loads(post_json)

