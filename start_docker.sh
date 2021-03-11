#!/bin/bash


if [ "$1" == "shell" ]
then
  echo "open shell:"
  server_path=$(cd "$(dirname "$0")";pwd)
  echo "$server_path"
  echo "/www/sim-server"
  cd ..
  main_path=$(cd "$(dirname "$0")";pwd)
  docker run -it --rm -p 8000:8000 -v $main_path:/www -v /var/run/docker.sock:/var/run/docker.sock wda-sim/server /bin/bash
else
  echo "run server:"
  server_path=$(cd "$(dirname "$0")";pwd)
  cd ..
  main_path=$(cd "$(dirname "$0")";pwd)
  docker run -it --rm -p 8000:8000 -v $main_path:/www -v /var/run/docker.sock:/var/run/docker.sock wda-sim/server sh -c 'cd /www/sim-server/server && python3 server.py'
fi


