## Ansible-Tools
Various tools and scripts for Ansible

## run-playbook:
Python module built to run Ansible playbooks aginst any number of devices within an Ansible inventory file (default hosts). Module assumes playbooks are in the same directory

### Source
[ansible-run_playbook](https://github.com/jtyr/ansible-run_playbook)

### Use

Need to define: 

    src_hosts = 'hosts'  
    src_playbook = 'playbooks/test.yml'  
    src_limit = 'all'  
    
src_hosts: Inventory file  
src_playbook: Playbook to run  
src_limit: Devices or groups within inventory to run against. (uses limit_to)  
    
Call the Runner() class:  

    def run_playbook():
        runner = Runner(
            playbook = src_playbook,
            hosts = src_hosts,
            limit_to = src_limit,  # all, none, Group Name, IP address or resolvable hostname. Must be in hosts file
            display = display,
            options={
                'subset': 'all',
                # 'become': True,
                # 'become_method': 'sudo',
                # 'become_user': 'root',
                # 'private_key_file': '/path/to/the/id_rsa',
                # 'tags': 'debug',
                # 'skip_tags': 'debug',
                'verbosity': 0,
            },
            # passwords={
            #     'become_pass': 'sudo_password',
            #     'conn_pass': 'ssh_password',
            # },
            # vault_pass='vault_password',
        )
        stats = runner.run()

    run_playbook()

