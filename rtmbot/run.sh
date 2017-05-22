#! /bin/bash --

NAME="${1:-rtmbot}"
REV="${2:-latest}"
APP="$(dirname $(readlink -e $0))/app"

docker run\
 --init\
 --rm\
 --volume "${APP}:/opt/${NAME}"\
 --interactive\
 --tty\
 "${NAME}:${REV}"
