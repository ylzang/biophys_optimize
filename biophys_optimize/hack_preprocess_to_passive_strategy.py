#!/usr/bin/env python

import json
import argparse
import os.path
from pkg_resources import resource_filename

parser = argparse.ArgumentParser(description='hack in paths that strategy will do - passive')
parser.add_argument('input', type=str)
parser.add_argument('output', type=str)
args = parser.parse_args()

fit1_handles = [
    "passive_fitting/passive/fixnseg.hoc",
    "passive_fitting/passive/iclamp.ses",
    "passive_fitting/passive/params.hoc",
    "passive_fitting/passive/mrf.ses",
]

fit2_handles = [
    "passive_fitting/passive/fixnseg.hoc",
    "passive_fitting/passive/iclamp.ses",
    "passive_fitting/passive/params.hoc",
    "passive_fitting/passive/mrf2.ses",
]

fit3_handles = [
    "passive_fitting/passive/fixnseg.hoc",
    "passive_fitting/passive/circuit.ses",
    "passive_fitting/passive/params.hoc",
    "passive_fitting/passive/mrf3.ses",
]

with open(args.input, "r") as f:
    data = json.load(f)

new_path_info = {
    "fit1": [resource_filename(__name__, f) for f in fit1_handles],
    "fit2": [resource_filename(__name__, f) for f in fit2_handles],
    "fit3": [resource_filename(__name__, f) for f in fit3_handles],
}

data["paths"].update(new_path_info)

with open(args.output, "w") as f:
    json.dump(data, f, indent=2)