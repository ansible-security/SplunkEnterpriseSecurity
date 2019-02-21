SplunkEnterpriseSecurity
========================

This role is effectively a shim to distribute various modules to interact with
Splunk Enterprise Security, once [Ansible
Mazer](https://github.com/ansible/mazer) goes stable and becomes the default
means of distributing Ansible content this will be converted from a role into a
Mazer Collection.

### IN DEVELOPMENT: Note that at this time, this content requires the patch provided by [this Pull Request](https://github.com/ansible/ansible/pull/52761)

Requirements
------------

None.

Role Variables
--------------

None.

Dependencies
------------

None.

Example Playbook
----------------

Using splunk modules are meant to be used with the [`httpapi` connection
plugin](https://docs.ansible.com/ansible/latest/plugins/connection/httpapi.html)
and as such we will set certain attributes in the inventory

Example `inventory.ini`:

NOTE: The passwords should be stored in a secure location or an [Ansible
Vault](https://docs.ansible.com/ansible/latest/user_guide/vault.html)

NOTE: the default port for Splunk's REST API is 8089


    [splunk]
    splunk.example.com

    [splunk:vars]
    ansible_network_os=splunk
    ansible_user=admin
    ansible_httpapi_pass=my_super_secret_admin_password
    ansible_httpapi_port=8089
    ansible_httpapi_use_ssl=yes
    ansible_httpapi_validate_certs=True
    ansible_connection=httpapi


Example playbook:

    - name: demo splunk
      hosts: splunk
      gather_facts: False
      tasks:
        - name: import the SplunkEnterpriseSecurity Role to access the modules
          import_role:
            name: SplunkEnterpriseSecurity
        - name: test splunk_data_input_monitor
          splunk_data_input_monitor:
            name: "/var/log/demo.log"
            state: "present"
            recursive: True
        - name: test splunk_data_input_network
          splunk_data_input_network:
            name: "9001"
            protocol: "tcp"
            state: "absent"
        - name: test splunk_coorelation_search
          splunk_correlation_search:
            name: "Test Demo Coorelation Search From Playbook"
            description: "Test Demo Coorelation Search From Playbook, description."
            search: 'source="/var/log/snort.log"'
            state: "present"
        - name: test splunk_adaptive_response_notable_event
          splunk_adaptive_response_notable_event:
            name: "Demo notable event from playbook"
            correlation_search_name: "Test Demo Coorelation Search From Playbook"
            description: "Test Demo notable event from playbook, description."
            state: "present"
            next_steps:
              - ping
              - nslookup
            recommended_actions:
              - script

License
-------

GPLv3

Author Information
------------------

[Ansible Security Automation Team](https://github.com/ansible-security)
