# Refgenie Nextflow plugin

This plugin links Refgenie and Nextflow. It will make all your refgenie-managed assets available to your nextflow pipelines. 

## Install

Install with some flavor of:

```
pip install --user --upgrade https://github.com/refgenie/refgenie_nfcore.git
```

## Point refgenie to the nextflow config file you want to manage

Add this line to your `$REFGENIE` config file:

```
nextflow_config: /abs/path/to/nextflow.config
```


That's it! Now whenever you update any assets with refgenie, your nextflow config file will be updated. Keep in mind: if using this plugin, your nextflow config file will now be managed by refgenie, so changes you introduce into the file directly will be overwritten by the next refgenie update.

## Tutorial

```
# Set up venv
python3 -m venv env
source env/bin/activate

# Install
pip install refgenie
pip install https://github.com/databio/refgenie_nfcore/archive/master.zip

# Initialize
mkdir refgenie_test
cd refgenie_test
refgenie init -c refgenie.yaml
touch nextflow.config
echo "nextflow_config: `pwd`/nextflow.config" >> refgenie.yaml

# Test
cat nextflow.config
refgenie pull -c refgenie.yaml rCRSd/fasta
cat nextflow.config
```
