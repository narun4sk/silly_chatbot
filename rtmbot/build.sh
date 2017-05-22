#! /bin/bash --

NAME="${1:-rtmbot}"
REV="${2:-latest}"

docker build\
 --pull\
 --rm\
 --tag "${NAME}:${REV}"\
 .
