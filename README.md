# Refgenie Nextflow plugin

This plugin links Refgenie and Nextflow. It will make all your refgenie-managed assets available to your nextflow pipelines. 

## Install

Install with some flavor of:

```
pip install --user --upgrade https://github.com/databio/refgenie_nfcore.git
```

## Point refgenie to the nextflow config file you want to manage

Add this line to your `$REFGENIE` config file:

```
nextflow_config: /abs/path/to/nextflow.config
```


That's it! Now whenever you update any assets with refgenie, your nextflow config file will be updated. Keep in mind: if using this plugin, your nextflow config file will now be managed by refgenie, so changes you introduce into the file directly will be overwritten by the next refgenie update.