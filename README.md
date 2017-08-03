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

Output examples:

```bash
$ src/paypal.py 150
Si se envían $150.00, se recibirán $141.60.
```

```bash
$ src/paypal.py 150 -v
Si se envían $150.00, se recibirán $141.60.

Tarifa base de comisiones PayPal: 5.4% + $0.30 USD
Cálculos:
 Enviado:     150.00
 Comisión:     -8.40
 -------------------
 Recibido:    141.60
```

```bash
$ src/paypal.py 100 -e
Para recibir $100.00, se deben solicitar $106.03.
```

```bash
$ src/paypal.py 100 -ev
Para recibir $100.00, se deben solicitar $106.03.

Tarifa base de comisiones PayPal: 5.4% + $0.30 USD
Cálculos:
 Enviado:     106.03
 Comisión:     -6.03
 -------------------
 Recibido:    100.00
```

```bash
$ src/paypal.py 50 -ev --commision 4.4
Para recibir $50.00, se deben solicitar $52.62.

Tarifa base de comisiones PayPal: 4.4% + $0.30 USD
Cálculos:
 Enviado:     52.62
 Comisión:    -2.62
 ------------------
 Recibido:    50.00
```


