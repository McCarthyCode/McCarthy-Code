#!/bin/bash

declare -a apps=(
  "mwd"
  "home"
)

for i in "${apps[@]}"; do
  echo "rm ./$i/__pycache__/*.pyc"
  rm ./$i/__pycache__/*.pyc
done
