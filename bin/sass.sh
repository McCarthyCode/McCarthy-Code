#!/bin/bash

project_dir="$HOME/Repositories/McCarthy-Code"
sass="$HOME/.npm-global/bin/sass"

sass_input_home="$project_dir/home/static/home/sass/base.sass"
sass_output_home="$project_dir/home/static/home/css/home.css"
sass_output_home_compressed="$project_dir/home/static/home/css/home.min.css"

sass_input_legal="$project_dir/legal/static/legal/sass/base.sass"
sass_output_legal="$project_dir/legal/static/legal/css/legal.css"
sass_output_legal_compressed="$project_dir/legal/static/legal/css/legal.min.css"

declare -a args=(
  "$sass_input_home:$sass_output_home"
  "--style=compressed $sass_input_home:$sass_output_home_compressed"
  # "$sass_input_legal:$sass_output_legal"
  # "--style=compressed $sass_input_legal:$sass_output_legal_compressed"
)

cd $project_dir

for i in "${args[@]}"; do
  cmd="$sass --watch -I home/static/ads/sass -I home/static/lib/sass -I node_modules/bootstrap/scss $i"
  echo $cmd
  $cmd &
done
