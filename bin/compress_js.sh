#!/bin/bash

closure_compiler="/opt/closure-compiler/closure-compiler-v20190929.jar"

js_input_global="home/static/home/js/global.js"
js_output_global="home/static/home/js/global.min.js"

js_input_index="home/static/home/js/index.js"
js_output_index="home/static/home/js/index.min.js"

js_input_portfolio="home/static/home/js/portfolio.js"
js_output_portfolio="home/static/home/js/portfolio.min.js"

declare -a commands=(
  # "java -jar $closure_compiler --js $js_input_global --js_output_file $js_output_global"
  # "java -jar $closure_compiler --js $js_input_index --js_output_file $js_output_index"
  # "java -jar $closure_compiler --js $js_input_portfolio --js_output_file $js_output_portfolio"
)

for i in "${commands[@]}"; do
  echo "$i"
  $i
done
