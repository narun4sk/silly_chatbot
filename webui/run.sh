#! /bin/bash --

NAME="${1:-webui}"
REV="${2:-latest}"

docker run\
 --init\
 --rm\
 --publish 8000:8000\
 --volume app:/opt/"${NAME}"\
 --interactive\
 --tty\
 "${NAME}:${REV}"
