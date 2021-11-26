#!/usr/env/bin python3
"""
BSON-JSON converter
Requires: py-bson (https://github.com/py-bson/bson)

@Author: Secret <secret@rathena.org>
"""
import argparse
import collections
import bson
import json
from pathlib import Path

def json_to_bson(in_file, out_file):
    f = open(in_file)
    json_data = json.loads(f.read())
    bson_data = bson.encode(json_data)
    out = open(out_file, "wb")
    out.write(bson_data)
    print("Done")

def bson_to_json(in_file, out_file):
    bson_file = open(in_file, "rb")
    bson_bytes = bson_file.read()
    decoded_data = bson.decode(bson_bytes)
    pretty_json = json.dumps(decoded_data, indent=4)
    out = open(out_file, "w")
    out.write(pretty_json)
    print("Done")

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--input", type=str, required=True, help="Input file path")
    ap.add_argument("-o", "--output", type=str, required=True, help="Output file path")
    ap.add_argument("-m", "--mode", choices=["e", "d"], required=True, help="Operation mode (e=encode bson, d=decode bson)")
    args = vars(ap.parse_args())
    if (args["mode"] == "e"):
        json_to_bson(args["input"], args["output"])
    elif (args["mode"] == "d"):
        bson_to_json(args["input"], args["output"])
