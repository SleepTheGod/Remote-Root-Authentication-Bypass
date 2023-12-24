"""
Script Name: System File Check Script
Author: Taylor Christian Newsome
Date: December 23, 2023

Description:
This script performs a check on system files related to sudo configuration configures it sets the user ID then grabs the shadow configuration.

Usage:
Run the script to check the permissions of sudo configuration files and display the contents of the shadow file remote root authentication bypass.
"""

# ASCII Art
ascii_text = '''
███████╗██╗  ██╗███████╗██╗     ██╗                  
██╔════╝██║  ██║██╔════╝██║     ██║                  
███████╗███████║█████╗  ██║     ██║                  
╚════██║██╔══██║██╔══╝  ██║     ██║                  
███████║██║  ██║███████╗███████╗███████╗             
╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝             
                                                     
███████╗████████╗ ██████╗ ██████╗ ███╗   ███╗        
██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗████╗ ████║        
███████╗   ██║   ██║   ██║██████╔╝██╔████╔██║        
╚════██║   ██║   ██║   ██║██╔══██╗██║╚██╔╝██║        
███████║   ██║   ╚██████╔╝██║  ██║██║ ╚═╝ ██║        
╚══════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝        
                                                     
          ██████╗ ██╗   ██╗                                
          ██╔══██╗╚██╗ ██╔╝                                
          ██████╔╝ ╚████╔╝                                 
          ██╔══██╗  ╚██╔╝                                  
          ██████╔╝   ██║                                   
          ╚═════╝    ╚═╝                                   
                                                     
 ██████╗██╗     ██╗   ██╗███╗   ███╗███████╗██╗   ██╗
██╔════╝██║     ██║   ██║████╗ ████║██╔════╝╚██╗ ██╔╝
██║     ██║     ██║   ██║██╔████╔██║███████╗ ╚████╔╝ 
██║     ██║     ██║   ██║██║╚██╔╝██║╚════██║  ╚██╔╝  
╚██████╗███████╗╚██████╔╝██║ ╚═╝ ██║███████║   ██║   
 ╚═════╝╚══════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝   ╚═╝'''

print(ascii_text)

import subprocess

# Commands
commands = [
    ("ls -l /etc/sudo.conf", "ls -l /usr/bin/sudo", "cat /etc/shadow"),
    ("'ls -l /etc/sudo.conf'", "'ls -l /usr/bin/sudo'", "'cat /etc/shadow'")
]

for idx, (cmd, desc) in enumerate(zip(commands[0], commands[1])):
    print(f"\nCommand {idx + 1}: {desc}")
    result = subprocess.run(cmd.split(), capture_output=True, text=True)
    print(result.stdout)

print("Script execution completed.")
