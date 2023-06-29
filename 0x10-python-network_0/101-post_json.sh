#!/bin/bash
# curl a json file
curl -sd "$(cat "$2")" -H 'Content-Type: application/json' "$1"
