import yaml
import os
import ansible_runner


def list_hosts():
    # Set the ANSIBLE_CONFIG environment variable
    os.environ['ANSIBLE_CONFIG'] = os.path.join(os.getcwd(), 'ansible.cfg')

    # Run the ansible command to list hosts
    

    out, err, rc = ansible_runner.run_command(
        executable_cmd='ansible',
        cmdline_args=['all:localhost', '-m', 'ping'],
    )

# Load the inventory fileimport yaml

# Load the inventory file
with open('hosts.yml', 'r') as file:
    inventory_data = yaml.safe_load(file)

# Create a dictionary to store hosts by their name
hosts_by_name = {}


# Iterate through hosts and group them by name
for group_name, group in inventory_data.items():
    for host_name, host_info in group['hosts'].items():
        if host_name not in hosts_by_name:
            hosts_by_name[host_name] = {'group_name': [], 'ip_address': []}
        hosts_by_name[host_name]['group_name'].append(group_name)
        if host_info is not None:
            hosts_by_name[host_name]['ip_address'].append(host_info.get('ansible_host', 'localhost'))

# Print the hosts' details grouped by name
for host_name, details in hosts_by_name.items():
    print("Host Name:", host_name)
    print("Group Names:", ', '.join(details['group_name']))
    print("IP Addresses:", ', '.join(details['ip_address']))
    print()

list_hosts()




