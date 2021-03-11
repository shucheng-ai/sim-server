#!/bin/bash
# bash build_docker.sh
# bash build_docker.sh en
# bash build_docker.sh ali
# bash build_docker.sh ustc
# bash build_docker.sh tsinghua

cd docker
image="sim/server"
echo "build $image"

if [ "$1" == "" ]
then
  echo "build cn(default ustc) docker:"
  cp source/sources.ustc.list sources.list
  cp source/pip.ustc.conf pip.conf
  docker build --no-cache -f Dockerfile -t "$image" .
elif [ "$1" == "en" ]
then
  echo "build en docker:"
  docker build --no-cache -f Dockerfile.en -t "$image" .
else
  echo "build cn($1) docker:"
  cp source/sources."$1".list sources.list
  cp source/pip."$1".conf pip.conf
  docker build --no-cache -f Dockerfile -t "$image" .
fi

echo "build docker ok!"
