# 0x0A. SSH

## The purpose of this project is to learn the following concepts:
- What is a server
- Where server usually live
- What is SSH
- How to create an SSH RSA key pair
- How to connect to a remote host using an SSH RSA key pair

## Requirements for Tasks:
- Allowed editors: vi, vim, emacs
- All your files will be interpreted on Ubuntu 14.04 LTS
- All your files should end with a new line
- A README.md file, at the root of the folder of the project, is mandatory
- All your Bash script files must be executable
- The first line of all your Bash scripts should be exactly #!/usr/bin/env bash
- The second line of all your Bash scripts should be a comment explaining what is the script doing

---
File | Task
---|---
0-use_a_private_key | A Bash script that uses ```ssh``` to connect to a server using the private key ```~/.ssh/holberton``` with user ```ubuntu```
1-create_ssh_key_pair | A Bash script that creates an RSA key pair
2-ssh_config | An SSH configuration file for the local SSH client

---
Task | Requirements
---|---
0 | Only use ```ssh``` single-character flags; Cannot use ```-l```; Do not need to handle case of a private key protected by a passphrase
1 | Name of created private key must be ```holberton```; Number of bits in the created key is 4096; The created key must be protected by specified passphrase
2 | SSH configuration must be configured to use the private key ```~/.ssh/holberton```; SSH client configuration must be configured to refuse to authenticate using a password

## Author
Francesca Cantor
