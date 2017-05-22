#! /bin/bash --

NAME="${1:-webui}"
REV="${2:-latest}"

docker build\
 --pull\
 --rm\
 --tag "${NAME}:${REV}"\
 .
