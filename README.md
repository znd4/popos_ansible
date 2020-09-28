# Zane's pop!_os config

I'm tired of installing everything I need on variaous computers, so I'm going to try configuring everything with ansible

- [The article series this is inspired from](https://opensource.com/article/18/3/manage-workstation-ansible)

## Installing Ansible

```bash
sudo apt-get install software-properties-common
sudo apt-add-repository ppa:ansible/ansible
sudo apt-get update
sudo apt-get install ansible
```

## Installing invoke

```bash
sudo apt install python3-pip

sudo apt install python3-venv

pip3 install --user invoke
```

## Set up ansible job

```bash
python3 -m invoke pull
```

## Todo

- [ ] loop usernames
- [ ] parametrize usernames
- [ ] Add fira code font
- [ ] gnome customization
- [ ] install visual studio code
