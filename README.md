# rpyd

CLI (Command Line Interface) to test Rapyd's Fintech As A Service  API. See the API documentation to better understand and use this tool: https://docs.rapyd.net/build-with-rapyd/reference/api-reference

## Dependencies

This is a Python tool that depends on:

* Python 3
* Python requests lybrary

## Usage Example

See how the commands are used:

```
# python3 create-payment.py -h
usage: create-payment.py [-h] [-a] filename env

Create Payment

positional arguments:
  filename    the json file that contains the body
  env         the rapyd environment

options:
  -h, --help  show this help message and exit
  -a, --all   outputs all rapyd's api response
```

Use the commands:

```
# python3 create-payment.py mx_spei_bank.json sandbox
Do you want to create this payment? (y/n): y
token: payment_f6c1b515863cba0e21b5be79d75e10c6
amount: 10
currency: MXN
status: ACT
textual_codes: {}
redirect_url:
```
