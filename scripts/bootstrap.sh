#!/bin/sh

#
# Start traderbot
# Call __init__.py if params is ok

VER="0.0.1@ALFA"
INIT_PATH="../jezebel/__init__.py"

function echo_usage {
  echo -e "Jezebel $VER"
  echo -e "\tUsage example: jezebel [exchange] [currencie] [capital-to-operate]"
  echo -e ""
}

function bootstrap {
  /usr/bin/python3 -B $INIT_PATH # param '-B' to not create __pycache__ 
}

function check_params {
  if [ $@ != 0 ]; then
    bootstrap
  else
    echo_usage $VER
  fi
}

function start {
  check_params $@ 
}


