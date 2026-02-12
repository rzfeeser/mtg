# rzfeeser.mtg - Magic The Gathering - Ansible Collection
Author: Russell Zachary Feeser  
GitHub: @RZFeeser  
Email: rzfeeser@users.noreply.github.com  
Galaxy: https://galaxy.ansible.com/rzfeeser/mtg

![rzfeeser.mtg Magic The Gathering Banner](https://github.com/rzfeeser/mtg/blob/main/docs/images/rzfeeser_ansible_mtg_collection.png?raw=true)

This repository is an ansible collection, `rzfeeser.mtg`, written by @RZFeeser for the purposes of an Ansible collection containing plugins and playbooks that abstract interaction with Magic the Gather API service @ [MTG API](https://docs.magicthegathering.io/)

### Overview

Welcome! This is an Ansible collection developed for [https://magicthegathering.io](https://magicthegathering.io)

Ansible is a framework that runs Python scripts primarily used for for automating configuration, or Configuration as Code (Caac). So, we'll be the first to admit, it *is* a little silly to have an Ansible collection that interacts with a service to return Magic the Gathering facts. However, it is a wonderfully maintained API, open, has support of a massive community, and ultimately a fun way to learn about coding.

*Note: We are not curators of the MagicTheGathering.io API service. For questions general use questions about the API, see the documentation page at* [docs.magicthegathering.io](https://docs.magicthegathering.io)

### Resources
- [@GitHub - rzfeeser/mtg](https://github.com/rzfeeser/mtg)
- [@GitHub - mtg Ansible Execution Environment](https://github.com/rzfeeser/mtg/pkgs/container/mtg_ee)
- [magicthegathering.io](https://docs.magicthegathering.io/)
- [Ansible Galaxy - rzfeeser.mtg](https://galaxy.ansible.com/rzfeeser/mtg)


### Install Notes
- This Ansible collection is written with the Python standard library, so it has no dependenies beyond itself.
- This is an Ansible collection and may be installed using one of the following methods:
  1. Install directly from source on GitHub
  2. Proxied from ansible.galaxy.com
  3. Bypass a direct install, and instead use the PokeAPI Execution Environment container based solution (suitable for CI engines such as AAP/Tower/AWX, Jenkins, GitLab, and so on)

#### Option 01 - Install directly from source on Github
- Ansible should already be installed
- Install rzfeeser.mtg collection directly from GitHub - `ansible-galaxy collection install git+https://github.com/rzfeeser/mtg`

#### Option 02 - Proxied from ansible.galaxy.com
- Ansible should already be installed
- Install rzfeeser.mtg collection via ansible.galaxy.com - `ansible-galaxy collection install rzfeeser.mtg`

#### Option 03 - Container based solution
- `ansible-runner` needs to be installed, and Docker needs to exist
  - It should be mentioned that `ansible-runner` requires a special project directory layout before executing. See the [ansible-runner Project Homepage](https://ansible.readthedocs.io/projects/runner/en/stable/index.html) for more information
- An Ansible Execution Environment container is maintained by this author, [@GitHub - mtg Ansible Execution Environment](https://github.com/rzfeeser/mtg/pkgs/container/mtg_ee). This solution includes Ansible, Python, Ansible-Runner, and the most recent `rzfeeser.mtg` collection
- Use `ansible-runner` to run a playbook containing references to the `rzfeeser.pokeapi` collection - `ansible-runner run --process-isolation --process-isolation-executable docker --container-image docker pull ghcr.io/rzfeeser/mtg_ee:1.3.3 -p playbook_to_run.yml .`


### How to Use
- The module `rzfeeser.mtg.mtg_card` may be used to make API requests to https://api.magicthegathering.io/<version>/<resource>. This module was written to simplify interaction with https://api.magicthegathering.io/<version>/<resource> API. See https://magicthegathering.io/ for documentation on using the API. 

<!--
- `rzfeeser.pokeapi.pokeapi_info` has the following options:
  - **resource**:
      description: This is the resource to lookup. See pokeapi.co/docs/v2 for all possible values. Values include 'ability', 'berry', 'berry-firmness', 'berry-flavor', 'characteristic', 'contest-effect', 'contest-type', 'egg-group', 'encounter-condition', 'encounter-condition-value', 'encounter-method', 'evolution-chain', 'evolution-trigger', 'gender', 'generation', 'growth-rate', 'item', 'item-attribute', 'item-category', 'item-fling-effect', 'item-pocket', 'language', 'location', 'location-area', 'machine', 'move', 'move-ailment', 'move-battle-style', 'move-category', 'move-damage-class', 'move-learn-method', 'move-target', 'nature', 'pal-park-area', 'pokeathlon-stat', 'pokedex', 'pokemon', 'pokemon-color', 'pokemon-form', 'pokemon-habitat', 'pokemon-shape', 'pokemon-species', 'region', 'stat', 'super-contest-effect', 'type', 'version', 'version-group'
      required: true
      type: str
  - **name**:
      description: The name of the resource to lookup. See pokeapi.co/docs/v2 for all possible values.
      required: false
      type: str
  - **limit**:
      description: The number of results that will be returned with the lookup.
      required: false
      type: int
  - **offset**:
      description: The resource index + 1 to begin at. For example, If 42 is passed, then resource 43 will be the first result returned.
      required: false
      type: int
-->

### About magicthegathering.io REST API
Visit [https://magicthegathering.io](https://magicthegathering.io) for more information about the project.

### About the Author
Russell Zachary Feeser (@RZFeeser) is a consultant and technology trainer focusing on Ansible, Python, AWX/Tower/AAP, Terraform, Go, Databricks, Snowflake, Azure, 5G, SIP and core telecom communications. If you're interested in discussing a consulting or training project, feel free to reach out.  

- [https://youtube.com/@codewithfeeser](https://youtube.com/@codewithfeeser)
- [https://rzfeeser.com](https://rzfeeser.com)  
- [https://iris7.com](https://iris7.com)
