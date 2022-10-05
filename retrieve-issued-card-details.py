#!/usr/bin/env python3
from utilities import make_request
import json
import argparse 

parser = argparse.ArgumentParser(description="Retrieve Issued Card Details")
parser.add_argument("card", help="id of the issued card; string starting with ci_ or card_")
parser.add_argument("env", help="the rapyd environment")
parser.add_argument("-a", "--all", help="outputs all rapyd's api response", action="store_true")

args = parser.parse_args()

path = f'/v1/issuing/cards/{args.card}'

response = make_request(env=args.env, method='get', path=path)
    
if args.all:
    print(json.dumps(response, indent=4))
else:
    s = f"card: {response['data']['id']}\n" \
        f"status: {response['data']['status']}\n" \
        f"card_number: {response['data']['card_number']}\n" \
        f"cvv: {response['data']['cvv']}\n" \
        f"expiration_month: {response['data']['expiration_month']}\n" \
        f"expiration_year: {response['data']['expiration_year']}"
    print(s)
