#!/usr/bin/env python3
# sp20-516-220 E.Cloudmesh.Common.3

from cloudmesh.common.FlatDict import FlatDict
from pprint import pprint

if __name__ == "__main__":
    gene = {
        "symbol": "gro",
        "proteins": {
            "symbol": "gro-PA"
        },
        "transcripts": {
            "symbol": "gro-RA"
        }
    }
    gene = FlatDict(gene, sep='.')

    pprint(gene)


