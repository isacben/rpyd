# rpyd

CLI (Command Line Interface) to test Rapyd's Fintech As A Service  API. See the API documentation to better understand and use this tool: https://docs.rapyd.net/build-with-rapyd/reference/api-reference

## Dependencies

This is a Python tool that depends on:

* Python 3
* Python requests library

## Rapyd API Keys

Create environment variables to store the Sandbox and Production Rapyd keys.

Get your keys here -> https://dashboard.rapyd.net/sign-up

For sandbox:

```
export sandbox='YOUR-ACCESS-KEY,YOUR-SECRET-KEY,sandboxapi'
```

For production:

```
export production='YOUR-ACCESS-KEY,YOUR-SECRET-KEY,api'
```

Note that the last parameters in the environment variables are `sandboxapi` for Sandbox and `api` for Production.
The name of the environment variables is irrelevant; however the exact same variable name has to be used to
run the scripts (see example below).

## Usage Example

See how the commands are used:

```console
# python3 create-payment.py -h
usage: create-payment.py [-h] [-a] filename env

Create Payment

positional arguments:
  filename    the json file that contains the body; see https://docs.rapyd.net/build-with-rapyd/reference/payments#create-payment
  env         the rapyd environment

options:
  -h, --help  show this help message and exit
  -a, --all   outputs all rapyd's api response
```

Use the commands:

```console
# python3 create-payment.py usr/mx_spei_bank.json sandbox
Do you want to create this payment? (y/n): y
token: payment_f6c1b515863cba0e21b5be79d75e10c6
amount: 10
currency: MXN
status: ACT
textual_codes: {}
redirect_url:
```

It is possible to combine the output of the scripts with Linux commands. For example:

```console
# python3 ./list-pmts.py 'country=co' pam -f bank | awk -F ',' '{print $1, $7}'
co_bancolombia_bank  'maximum_amount': 40000000
co_bancofalabella_bank  'maximum_amount': 40000000
co_bancocajasocial_lcl_bank  'maximum_amount': None
co_bancodeoccidente_lcl_bank  'maximum_amount': None
```

If you need more support ask your questions in our community -> https://community.rapyd.net