## Ansible-Tools
Various tools and scripts for Ansible

### run-playbook:
Python script built to run Ansible playbooks aginst any number of devices within an Ansible inventory file.

## Use
    python runplaybook.py host-name playbook-name
    ex:
    python runplaybook.py spine1 check_lldp_neigh.yml
