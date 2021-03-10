# Ansible
This repository is created to learn Ansible.

# Fix the below error while installing Ansible on CentOS 7

# This is the error message
[root@ansiblecontroller ~]# sudo yum install ansible
Loaded plugins: fastestmirror, langpacks
Loading mirror speeds from cached hostfile
 * base: centos.excellmedia.net
 * extras: centos.excellmedia.net
 * updates: centos.excellmedia.net
No package ansible available.
Error: Nothing to do
[root@ansiblecontroller ~]# sudo subscription-manager repos --enable rhel-7-server-ansible-2.9-rpms
sudo: subscription-manager: command not found

# Here is the Fix
1. Install the Extra Packages for Enterprise Linux

[root@ansiblecontroller ~]# sudo yum install epel-release -y

2. List the repository to confirm it has been successfully installed

[root@ansiblecontroller ~]# sudo yum repolist

3. Now give a try to install ansible

[root@ansiblecontroller ~]# sudo yum install ansible -y

4. Verify the installation by printing the ansible version

[root@ansiblecontroller ~]# ansible --version
ansible 2.9.16
  config file = /etc/ansible/ansible.cfg
  configured module search path = [u'/root/.ansible/plugins/modules', u'/usr/share/ansible/plugins/modules']
  ansible python module location = /usr/lib/python2.7/site-packages/ansible
  executable location = /bin/ansible
  python version = 2.7.5 (default, Nov 16 2020, 22:23:17) [GCC 4.8.5 20150623 (Red Hat 4.8.5-44)]

# Linux command to connect to a network device automatically
sudo nmcli connection modify "ethernet device name" connection.autoconnect yes

# Ansible inventory file parameters

The default inventory file is /etc/ansible/hosts

Below is the sample inventory file configuration:

Hostname ansible_host=ipAddress ansible_port=port ansible_ssh_pass=Password

# Command to test the connectivity between

ansible hostname -m ping -i inventoryfile

# Enabling SSH Key-Based user authentication
1) Generate public-private key pair

$ssh-keygen

2) Copy the public key to the target servers

$ssh-copy-id ansible1.example.com

$ssh-copy-id ansible2.example.com

3) Test the SSH connectivity and ensure the passwordless authentication is working

$ssh ansible1.example.com

$ssh ansible2.example.com
