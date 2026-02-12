# Magic The Gathering - Ansible Collection

Author: Russell Zachary Feeser  
GitHub: @RZFeeser  
Email: rzfeeser@users.noreply.github.com  

### Overview

Welcome! This is an Ansible collection developed for [https://magicthegathering.io](https://magicthegathering.io)

Ansible is a framework that runs Python scripts primarily used for for automating configuration, or Configuration as Code (Caac). So, we'll be the first to admit, it *is* a little silly to have an Ansible collection that interacts with a service to return Magic the Gathering facts. However, it is a wonderfully maintained API, open, has support of a massive community, and ultimately a fun way to learn about coding.

*Note: We are not curators of the MagicTheGathering.io API service. For questions general use questions about the API, see the documentation page at* [docs.magicthegathering.io](https://docs.magicthegathering.io)


### Ansible Collection - rzfeeser.mtg

This repository has recently been converted to a collection, `rzfeeser.mtg`. To install, use:

    ansible-galaxy collection install git+https://github.com/rzfeeser/mtg-ansible-collection


### Goals

  - Write and maintain Ansible modules for [magicthegathering.io](https://docs.magicthegathering.io)
  - Help other learn about automation and APIs
  - Linkshare with [magicthegathering.io](https://docs.magicthegathering.io)
  - Interact with students interested in learning automation with tools like Ansible and Python, or Terraform and Go


### Getting Started

#### Presteps

1. Install Python
    - Debian / Ubuntu - `sudo apt install python3-pip`
    - Windows - Ansible will only run on Linux. From the Windows Store install **Ubuntu 22.04** as part of the **WSL 2**. Then follow the steps for Debian / Ubuntu.

2. Install Ansible with the Python package installer, pip: `python3 -m pip install ansible`

#### Setup

1. Install the collection:

    `ansible-galaxy collection install git+https://github.com/rzfeeser/mtg-ansible-collection`
    
2. Try out one of the playbooks located in `playbooks/`

    `ansible-playbook playbooks/uri_module/playbook-uri-sets_and_cards.yml`


### Special Thanks

Speical thanks to everyone that particpated in helping shape this collection, including:

  - [Alta3 Research](https://alta3.com/)  
  - [Alta3 Research GitHub](https://github.com/alta3/)  
