#!/bin/bash

project_dir="$HOME/Repositories/McCarthy-Web-Design"

sass_input_home="$project_dir/home/static/home/sass/base.sass"
sass_output_home="$project_dir/home/static/home/css/home.css"
sass_output_home_compressed="$project_dir/home/static/home/css/home.min.css"

sass_input_legal="$project_dir/legal/static/legal/sass/base.sass"
sass_output_legal="$project_dir/legal/static/legal/css/legal.css"
sass_output_legal_compressed="$project_dir/legal/static/legal/css/legal.min.css"

declare -a args=(
  "$sass_input_home:$sass_output_home"
  "--style=compressed $sass_input_home:$sass_output_home_compressed"
  "$sass_input_legal:$sass_output_legal"
  "--style=compressed $sass_input_legal:$sass_output_legal_compressed"
)

for i in "${args[@]}"; do
  sass --watch $i &
done

clear
