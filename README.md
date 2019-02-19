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

NOTE: `splunk_vars.yaml` should ideally be a vars file or an [Ansible
Vault](https://docs.ansible.com/ansible/latest/user_guide/vault.html) and in
service of this example it needs to define three vars: `splunk_uname`,
`splunk_pass`, `splunk_host`.

    - name: demo splunk
      hosts: localhost
      gather_facts: False
      vars_files:
        - splunk_vars.yaml
      tasks:
        - name: import the SplunkEnterpriseSecurity Role to access the modules
          import_role:
            name: SplunkEnterpriseSecurity
        - name: test splunk_data_input_monitor
          splunk_data_input_monitor:
            name: "/var/log/demo.log"
            state: "present"
            splunk_username: "{{ splunk_uname }}"
            splunk_password: "{{ splunk_pass }}"
            splunk_servername: "{{ splunk_host }}"
            validate_certs: False
            recursive: True
        - name: test splunk_data_input_network
          splunk_data_input_network:
            name: "9001"
            protocol: "tcp"
            state: "absent"
            splunk_username: "{{ splunk_uname }}"
            splunk_password: "{{ splunk_pass }}"
            splunk_servername: "{{ splunk_host }}"
            validate_certs: False
        - name: test splunk_coorelation_search
          splunk_correlation_search:
            name: "Test Demo Coorelation Search From Playbook"
            description: "Test Demo Coorelation Search From Playbook, description."
            search: 'source="/var/log/snort.log"'
            state: "present"
            splunk_username: "{{ splunk_uname }}"
            splunk_password: "{{ splunk_pass }}"
            splunk_servername: "{{ splunk_host }}"
            validate_certs: False
        - name: test splunk_adaptive_response_notable_event
          splunk_adaptive_response_notable_event:
            name: "Demo notable event from playbook"
            correlation_search_name: "Test Demo Coorelation Search From Playbook"
            description: "Test Demo notable event from playbook, description."
            state: "present"
            splunk_username: "{{ splunk_uname }}"
            splunk_password: "{{ splunk_pass }}"
            splunk_servername: "{{ splunk_host }}"
            validate_certs: False
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
