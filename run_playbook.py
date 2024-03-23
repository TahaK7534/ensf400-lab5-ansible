import ansible_runner
import os

# Set the ANSIBLE_CONFIG environment variable to point to the ansible.cfg file
os.environ['ANSIBLE_CONFIG'] = os.path.join(os.getcwd(), 'ansible.cfg')

# Run the hello.yml playbook using ansible-playbook command
result = ansible_runner.run_command(executable_cmd='ansible-playbook', cmdline_args=['hello.yml'])

start_pos = result[0].find("TASK [Check list of Node.js apps running.]")
end_pos = result[0].find("TASK [Start example Node.js app.]")
output_section = result[0][start_pos:end_pos]
# Count the occurrences of "ok" in the output section
ok_count = output_section.count("ok")

# Check if the count is equal to 3
if ok_count == 3:
    print("All three the NodeJS servers  are OK for the specified task.")
else:
    print("Not all three the NodeJS servers are OK for the specified task.")

