#!/bin/sh
# Usage:
#   build.sh [browser] [outfile]

jsonnet \
    -A version=$(cat package.json | jq -r .version) \
    -A browser=$1 \
    manifest.jsonnet > manifest.json

zip -r -FS $2 $(cat package.json | jq -r .files[])
