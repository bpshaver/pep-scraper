#! /bin/sh
# docker-compose up
docker-compose up -V --abort-on-container-exit
# docker-compose up -d # deteach

# You can have -d or --abort-on-container-exit but not both
# I want abort-on-container-exit while debugging

# -V :  -V, --renew-anon-volumes
# Recreate anonymous volumes instead of retrieving data from the previous containers.
