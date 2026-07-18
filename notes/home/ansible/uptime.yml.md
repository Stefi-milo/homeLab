---
- name: Gather uptime from myservers
  hosts: myservers
  gather_facts: no

  tasks:
    - name: Run uptime command
      ansible.builtin.shell: uptime
      register: uptime_output

    - name: Show uptime result
      ansible.builtin.debug:
        var: uptime_output.stdout

