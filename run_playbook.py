import ansible_runner
import json
import os

os.environ['ANSIBLE_CONFIG'] = os.path.join(os.getcwd(), 'ansible.cfg')
# Run the hello.yml playbook on the 'app' group
results = ansible_runner.run(private_data_dir='./', playbook='hello.yml', extravars={'target_group': 'app'})

# Process the results
for each_host in results.events:
    print(each_host['event'])

# Verify the response of the NodeJS servers
nodejs_servers_response = {}
for each_event in results.events:
    if 'event_data' in each_event and 'stdout' in each_event['event_data']:
        server_name = each_event['event_data']['stdout'].split()[1]
        response = each_event['event_data']['stdout_lines'][1]
        nodejs_servers_response[server_name] = response

# # Print the response of NodeJS servers
# print("\nResponse of NodeJS servers:")
# print(json.dumps(nodejs_servers_response, indent=4))
