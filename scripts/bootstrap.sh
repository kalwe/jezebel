# Start traderbot
# Call __init__.py if params is ok

VER="0.0.1@ALFA"
INIT_PATH="../jezebel/__init__.py"

function usage {
  echo -e "Jezebel $VER"
  echo -e "\tUsage example: jezebel [exchange] [currencie] [capital-to-operate]"
  echo -e "  -e/--exchange: bitfinex, bittrex"
  echo -e "  -c/--currencie: btc, ltc, xrp..."
  echo -e "  -v/--capital: 100, 150, 250...[n] (optional)"
}

function bootstrap {
  /usr/bin/python3 -B $INIT_PATH # param '-B' to not create __pycache__ 
}

function check_params {
  if [ "$1" == "--help" ]; then
    usage
  else
    # bootstrap
    echo "Jezebel is working to you get rich, bitch!!!"
    echo "In exchange $1" 
  fi
}

function startj {
  check_params $@ 
}


