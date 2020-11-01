#!/bin/bash

project_dir="$HOME/Repositories/McCarthy-Code"

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

declare -a path=(
  "home/static/global/sass"
  "node_modules/bootstrap/scss"
  "home/static/home/sass"
  "legal/static/legal/sass"
)

includes=$(printf -- " -I $project_dir/%s" ${path[@]})
includes=${includes:1}

cd $project_dir

for i in "${args[@]}"; do
  cmd="sass --watch $includes $i"

  echo $cmd >&2
  $cmd &
done

trap 'echo -e "\nExiting…" >&2; pkill $$' SIGINT

wait
