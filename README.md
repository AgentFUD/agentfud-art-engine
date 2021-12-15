# agentfud-art-engine
Art engine which helps you to generate thousands of beautiful images for the NFT market.

## Features

- Configurable layers
- Configurable rarity weights
- Information about your project
- Metadata and image generation based on pre-generated DNAs
- Excluding traits from metadata

## Installation

### via `pip`

All the artengine projects could be in a single directory

```bash
mkdir artengine_projects
cd artengine_projects
```

Creating and activating virtual environment

```bash
virtualenv env
source ./env/bin/activate
```

Install agentfud-art-engine

```bash
pip install agentfud-art-engine
```

Create first project in my_project directory

```bash
artengine init my_project
```

Enter into the directory, start configure and build

```bash
cd my_project
```

Now we can edit **instance_config.py**

If you want to fully test it, remove **layers** folder, then clone a prepared layers folder like this

```bash
rm -rf layers
```

```bash
git clone git@github.com:AgentFUD/layers.git
```

Run **artengine info**, then follow the tutorials.

## Usage

Create your own layers.

Edit **instance_config.py**, set up your layers, DNA generation type, etc.

Generate rarity configuration file with
```bash
artengine rarity generateconfig
```

Edit rarity-config.json as you like. Please keep in mind artengine info will tell you the maximum possible combinations so do not try generate more than you possibly could.

Generate DNA database. 
```bash
artengine dna --collection_size 30 -retries 10
```

Check generated rarities with
```bash
artengine rarity check
```

Bake your images
```bash
artengine bake both/metadata/images [--clean-up]
```

## Development install

```
git clone https://github.com/AgentFUDagentfud-art-engine.git

cd agentfud-art-engine

virtualenv env

source ./env/bin/activate

pip install --editable .
```
type artengine, you should see something very similar

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
