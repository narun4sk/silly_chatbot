#! /bin/bash --

NAME="${1:-webui}"
REV="${2:-latest}"
APP="$(dirname $(readlink -e $0))/app"

docker run\
 --init\
 --rm\
 --publish 8000:8000\
 --volume "${APP}:/opt/${NAME}"\
 --interactive\
 --tty\
 "${NAME}:${REV}"
