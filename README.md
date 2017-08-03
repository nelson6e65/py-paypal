# py-paypal

> Note: Only available in Spanish.

## Description

It calculates commissions and actual money received in PayPal transactions.



## Usage

Run `src/paypal.py --help`:

```
usage: paypal.py [-h] [--commision %] [--base BASE] [-e] [-v] amount

Calcular comisiones de transferencias PayPal.

positional arguments:
  amount          Monto

optional arguments:
  -h, --help      show this help message and exit
  --commision %   Porcentaje de comisión. Por defecto: 5.4 porciento.
  --base BASE     Monto base de la tarifa. Por defecto: 0.3 USD.
  -e, --expected  Indica que el monto especificado es el que se espera
                  recibir.
  -v, --verbose   Describe los valores.
```
