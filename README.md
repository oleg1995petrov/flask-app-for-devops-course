
# How to:  

1. If you're using a desktop (not server) image of virtualbox go to the 2nd step.

    Inside virtual machine install `openssl-server` package:

```bash
$ apt install openssl-server
```  

2. Set up `sshd_config` on remote machine by editing `/etc/ssh/sshd_config` file. Uncomment the next lines with the next values:
    * *Port 22*
    * *HostKey /etc/ssh/ssh_host_rsa_key*
    * *AuthorizedKeysFile .ssh/authorized_keys *
    * *PubkeyAuthentication yes*
    * *PasswordAuthentication yes*

    After that restart ssh service:

```bash 
$ sudo service ssh restart
```
3. Copy from local machine your pub rsa key to remote: 

```bash
$ ssh-copy-id -i [path to your pub key | usually locates at /home/[your username\]/.id_rsa.pub or other name which you set ] [username on remote machine]@[hostname or ip address]
```

If you have no rsa-keys yet, first install a cuple:

```bash
$ ssh-keygen -t rsa -f /home/[username]/.ssh/id_rsa[here may be a prefix] 
```
    And now copy pub key as was written above.

3. Set up ansible vars for your VM. Edit `roles/common/vars/main.yml` file and set the next variables:

* **project_name:** [a name of your project]
* **ansible_user:** [your VM's account username]

4. Put your VM's ip address to **inventory** file.

5. Create an encrypted file with your VM's account password:

```bash
$ ansible-vault create [password_file_name.yml | for example: passwd.yml]
```
Enter a password for that file. Inside it put `ansible_become_pass` variable with your VM account password:

```bash
$ ansible_become_pass: [your VM account password]
```

6. Now you are ready to start `ansible-playbook`:

```bash
$ ansible-playbook -i inventory -e @passwd.yml --ask-vault-pas deploy.yml
```

    Enter the password of your encrypted passwd.yml file and wait while Ansible will execute playbook.
