#!/bin/bash

closure_compiler="bin/closure-compiler-v20200504.jar"

declare -a files=(
  "home/static/lib/js/global"
  "home/static/home/js/index"
  "home/static/home/js/portfolio"
  "home/static/home/js/reorder_screenshots"
  "legal/static/legal/js/tabs"
)

for i in "${files[@]}" ; do
  input="$i.js"
  output="$i.min.js"

  cmd="java -jar $closure_compiler --language_in=STABLE --js $input --js_output_file $output"

  if [ $input -nt $output ] ; then
    echo "$cmd"
    $cmd
  fi
done
