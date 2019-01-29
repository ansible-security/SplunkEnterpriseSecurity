SplunkEnterpriseSecurity
========================

This role is effectively a shim to distribute various modules to interact with
Splunk Enterprise Security, once [Ansible
Mazer](https://github.com/ansible/mazer) goes stable and becomes the default
means of distributing Ansible content this will be converted from a role into a
Mazer Collection.

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

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      tasks:
        - name: import the SplunkEnterpriseSecurity Role to access the modules
          import_role:
            name: SplunkEnterpriseSecurity

License
-------

GPLv3

Author Information
------------------

[Ansible Security Automation Team](https://github.com/ansible-security)
