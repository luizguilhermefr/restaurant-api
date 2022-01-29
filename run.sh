#!/bin/bash
USER_ID=$(id -u)
GROUP_ID=$(id -g)

docker compose run -p 8000:8000 --rm --user ${USER_ID}:${GROUP_ID} web "$@"
