from invoke import task
import getpass


@task
def get_sudo_password(c):
    """Prompt user for their sudo password, then try to set the sudo password"""
    c.config.sudo.password = getpass.getpass("sudo password: ")

@task(get_sudo_password)
def dependencies(c, force=False):
    c.sudo("sudo apt-get update")
    c.sudo("sudo apt-get install -y ansible")
    packages = ["oefenweb.slack", "stephdewit.nvm"]
    for package in packages:
        c.sudo(f"/usr/bin/ansible-galaxy install {package}")
    collections = ["community.general"]
    for collection in collections:
        c.sudo(f"/usr/bin/ansible-galaxy collection install {collection}")

@task(dependencies)
def run(c, force=False):
    c.sudo(
        "/usr/bin/ansible-playbook local.yml"
    )

@task(dependencies)
def pull(c, force=False):
    """run ansible pull to sync"""
    c.sudo(
        "/usr/bin/ansible-pull "
        f"{'--force' if force else ''} "
        "--accept-host-key "
        "--private-key=/home/zanedufour/.ssh/id_rsa "
        "-U "
        "git@github.com:zdog234/popos_ansible.git"
    )
