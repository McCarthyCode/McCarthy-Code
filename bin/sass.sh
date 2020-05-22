#!/bin/bash

project_dir="$HOME/Repositories/McCarthy-Web-Design"

sass_input_home="$project_dir/home/static/home/sass/base.sass"
sass_output_home="$project_dir/home/static/home/css/home.css"
sass_output_home_compressed="$project_dir/home/static/home/css/home.min.css"

declare -a args=(
  "$sass_input_home:$sass_output_home"
  "--style=compressed $sass_input_home:$sass_output_home_compressed"
)

for i in "${args[@]}"; do
  sass --watch $i &
done

clear
