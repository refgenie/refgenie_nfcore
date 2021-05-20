import refgenconf
from warnings import warn

nf_cfg_template = """
params {{
  genomes {{
{content}
  }}
}}
"""


def print_nf_config(rgc):
    try:
        abg = rgc.list_assets_by_genome()
    except:
        return nf_cfg_template.format(content="")
    genomes_str = ""
    for genome, asset_list in abg.items():
        genomes_str += "    '{}' {{\n".format(genome)
        for asset in asset_list:
            try:
                pth = rgc.seek(genome, asset)
            except refgenconf.exceptions.MissingSeekKeyError:
                warn("{}/{} is incomplete, ignoring...".format(genome, asset))
            else:
                genomes_str += \
                    "      {} = \"{}\"\n".format(asset.ljust(20, " "), pth)

    return nf_cfg_template.format(content=genomes_str)


def update_nfcore_config(rgc):
    nf_cfg_str = print_nf_config(rgc)
    if hasattr(rgc, "nextflow_config"):
        print("Writing nextflow config file: {}".format(rgc.nextflow_config))
        with open(rgc.nextflow_config, 'w') as f:
            f.write(nf_cfg_str)
    else:
        print("Add a 'nextflow_config' attribute to your refgenie config file"
        " and it will be automatically updated with this content:")
        print(nf_cfg_str)



# rgc = refgenconf.RefGenConf("/home/nsheff/pCloudSync/env/refgenie_config/zither.yaml")
# print_nf_config(rgc)
