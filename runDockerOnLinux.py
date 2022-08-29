# Linux commands for running docker on Virtual Machine
import os

# get latest packages
os.system('sudo apt update')

# starts docker system, but its not enabled
os.system('sudo apt install -y docker.io')

# enable docker automatically after reboot
os.system('sudo systemctl enable docker --now')

# add non-root user to docker group, so we can use docker without sudo
os.system('')

# now restart system to apply permissions change
# additionally, can just log out -> log in again

# docker is not installed

# run docker & port
os.system('docker run --rm -it -p 80:80 vulnerables/web-dvwa')

# open browser and go to -> 127.0.0.1
# username: admin
# password: password