[![Pypi Status](https://img.shields.io/badge/pypi-v0.1.6-green)](https://pypi.org/project/art-engine/)

# agentfud-art-engine
Art engine which helps you to generate thousands of beautiful images for the NFT market.

## Install
```
bash$ mkdir myproject
bash$ cd myproject
bash$ virtualenv env
bash$ source ./env/bin/activate
bash$ pip install artengine
bash$ artengine init my_project
bash$ cd my_project
```
Now we can edit **instance_config.py**

If you want to fully test it, remove **layers** folder, then clone a prepared layers folder like this
```
bash$ git clone git@github.com:AgentFUD/layers.git
```
Run **artengine info**, then follow the tutorials.

## Development install

```
git clone https://github.com/AgentFUDagentfud-art-engine.git

cd agentfud-art-engine

virtualenv env

source ./env/bin/activate

pip install --editable .
```
type agentfud, you should see something very similar

```
(env) agentfud@Legion-Y540:/tmp/agentfud-art-engine$ artengine
Usage: artengine [OPTIONS] COMMAND [ARGS]...

  Welcome to Agent FUD ArtEngine! An all-in-one cli tool for NFT artists!

Options:
  --help  Show this message and exit.

Commands:
  bake          Bakes images and metadata files
  info          Gathers and prints out information about your project
  init          Initializes a new Art Engine project
  rarityconfig  Generates rarity config json file
  run           Runs any python script
```
