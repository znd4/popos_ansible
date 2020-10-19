from invoke import task
import getpass
import json
import sys


@task
def get_sudo_password(c):
    """Prompt user for their sudo password, then try to set the sudo password"""
    c.config.sudo.password = getpass.getpass("sudo password: ")


@task(get_sudo_password)
def dependencies(c, force=False):
    c.run(f"{sys.executable} -m pip install inquirer")
    import inquirer

    c.config.personal_users = inquirer.checkbox(
        message="Which users should the setup process be run for?",
        choices=["zdufour", "zanedufour"],
    )

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
        f"/usr/bin/ansible-playbook "
        f"--extra-vars='{json.dumps(dict(personal_users=c.config.personal_users))}' "
        "local.yml"
    )


@task(dependencies)
def pull(c, force=False):
    """run ansible pull to sync"""
    c.sudo(
        "/usr/bin/ansible-pull "
        f"{'--force' if force else ''} "
        "--accept-host-key "
        f"--extra-vars='{json.dumps(dict(personal_users=c.config.personal_users))}' "
        "--private-key=/home/zanedufour/.ssh/id_rsa "
        "-U "
        "git@github.com:zdog234/popos_ansible.git"
    )
