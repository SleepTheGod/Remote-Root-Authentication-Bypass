# Remote-Root-Authentication-Bypass
Made By Taylor Christian Newsome

This script is designed to perform a system file check primarily focused on sudo-related configurations and the shadow file. It begins with an impressive ASCII art display and then executes a series of commands using Python's subprocess module. These commands involve checking the permissions of /etc/sudo.conf and /usr/bin/sudo files and displaying the contents of the sensitive /etc/shadow file. The purpose seems to be ensuring proper permissions for sudo configuration files and possibly identifying any potential issues related to the shadow file, such as remote root authentication bypass. Upon completion, the script provides an "Script execution completed." message. However, note that accessing sensitive system files like /etc/shadow should be handled carefully and ideally only by authorized personnel due to security concerns.

Proof of concept:![image](https://github.com/SleepTheGod/Remote-Root-Authentication-Bypass/assets/86472964/efa6adcf-5460-4a5a-b374-3b9fd8a53e88)
