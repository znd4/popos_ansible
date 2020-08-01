from invoke import task, Context
import getpass


@task
def get_sudo_password(c):
    """Prompt user for their sudo password, then try to set the sudo password"""
    c.config.sudo.password = getpass.getpass("sudo password: ")


@task(get_sudo_password)
def pull(c):
    """run ansible pull to sync"""
    c.sudo(
        "/usr/bin/ansible-pull --accept-host-key --private-key=/home/zanedufour/.ssh/id_rsa -U git@github.com:zdog234/popos_ansible.git"
    )
