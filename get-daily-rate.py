#!/usr/bin/env python3

from utilities import make_request
import json
import argparse 

parser = argparse.ArgumentParser(description="Get Daily Rate")
parser.add_argument("params", help="the url parameters between quotes, for example 'action_type=payment&buy_currency=USD&sell_currency=EUR'; params: action_type, amount, buy_currency, date, fixed_side, sell_currency; documentation: https://docs.rapyd.net/build-with-rapyd/reference/daily-rates#get-daily-rate")
parser.add_argument("env", help="the rapyd environment")

args = parser.parse_args()

path = f'/v1/rates/daily?{args.params}'

response = make_request(env=args.env, method='get', path=path)

print(json.dumps(response, indent=2))
