#!/usr/bin/env python2.7

import os
import sys
import argparse
from collections import namedtuple

from ansible.parsing.dataloader import DataLoader
from ansible.vars import VariableManager
from ansible.inventory import Inventory
from ansible.executor.playbook_executor import PlaybookExecutor
from ansible.utils.display import Display

parser = argparse.ArgumentParser(description='Arguments passed to the script.')

parser.add_argument('-d','--device', help='Enter device you want to run playbook aginst.')
parser.add_argument('-i','--inventory', help='Enter inventory file you want to run playbook aginst.')

args = parser.parse_args()
device_arg = args.device
inventory_arg = args.inventory

variable_manager = VariableManager()
loader = DataLoader()
device = device_arg
inventory = inventory_arg
playbook_path = '/opt/netmgmt/netmgmt-netstat.yml'


inventory = Inventory(loader=loader, variable_manager=variable_manager,  host_list=inventory)

if not os.path.exists(playbook_path):
    print '[INFO] The playbook does not exist'
    sys.exit()

Options = namedtuple('Options', ['listtags', 'listtasks', 'listhosts', 'syntax', 'connection','module_path', 'forks', 'remote_user', 'private_key_file', 'ssh_common_args', 'ssh_extra_args', 'sftp_extra_args', 'scp_extra_args', 'become', 'become_method', 'become_user', 'verbosity', 'check'])

options = Options(listtags=False, listtasks=False, listhosts=False, syntax=False, connection='ssh', module_path=None, forks=100, remote_user='slotlocker', private_key_file=None, ssh_common_args=None, ssh_extra_args=None, sftp_extra_args=None, scp_extra_args=None, become=True, become_method=None, become_user='root', verbosity=None, check=False)

variable_manager.extra_vars = {'hosts': 'mywebserver'} # This can accomodate various other command line arguments.`

passwords = {}

pbex = PlaybookExecutor(playbooks=[playbook_path], inventory=inventory, variable_manager=variable_manager, loader=loader, options=options, passwords=passwords)

results = pbex.run()
