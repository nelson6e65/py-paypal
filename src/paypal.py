#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import argparse


class Console:
    COLORS = {
        'normal':  '\33[0m',
        'info':    '\33[36m',
        'success': '\33[32m',
        'warning': '\33[33m',
        'danger':  '\33[31m',
        'cyan':    '\33[96m',
        'green':   '\33[92m',
        'red':     '\33[91m',
    }

    STYLES = {
        'normal':   '\33[0m',
        'bold':     '\33[1m',
        'underline': '\33[4m'
    }

    def f(text: str, color: str = '', style: str = '', reset: bool = True):
        formated = text

        if len(color) > 1:
            formated = Console.COLORS[color] + formated

        if len(style) > 1:
            formated = Console.STYLES[style] + formated

        if reset:
            formated = formated + '\33[0m'

        return formated

    def bold(text: str, color: str = '', reset: bool = True):
        return Console.f(text, color, 'bold', reset)

    def underline(text: str, color: str = '', reset: bool = True):
        return Console.f(text, color, 'underline', reset)


def getTransactionInfo(
    value: float,
    commision: float = 5.4,
    base: float = 0.3,
    expected: bool = False
):
    # Si es menor a 1, es poque indica un porcentaje y no necesita convertirse
    if commision >= 1:
        commision /= 100

    info = {
        'amount': 0,
        'tax': 0,
        'real': 0,
    }

    if expected:  # Si 'value' representa al monto esperado
        info['real'] = value
        info['amount'] = (info['real'] + base) / (1 - commision)
        info['tax'] = (info['amount'] * commision) + base

    else:  # Si 'value' representa al monto enviado
        info['amount'] = value
        info['tax'] = (info['amount'] * commision) + base
        info['real'] = info['amount'] - info['tax']

    info['tax'] *= -1

    return info


def main():
    parser = argparse.ArgumentParser(
        description='Calcular comisiones de transferencias PayPal.'
    )
    parser.add_argument(
        'amount',
        type=float,
        help='Monto'
    )

    parser.add_argument(
        '--commision',
        metavar="%",
        type=float,
        default=5.4,
        help='Porcentaje de comisión. Por defecto: 5.4 porciento.'
    )

    parser.add_argument(
        '--base',
        type=float,
        default=0.3,
        help='Monto base de la tarifa. Por defecto: {0:.2n} USD.'.format(0.3)
    )

    parser.add_argument(
        '-e',
        '--expected',
        action='store_true',
        help='Indica que el monto especificado es el que se espera recibir.'
    )

    parser.add_argument(
        '-v',
        '--verbose',
        action='store_true',
        help='Describe los valores.'
    )

    args = parser.parse_args()

    info = getTransactionInfo(
        args.amount,
        args.commision,
        args.base,
        args.expected
    )

    if args.expected:
        print((
            'Para recibir ' + Console.bold('${real:,.2f}', 'success')
            + ', se deben solicitar ' + Console.bold('${amount:,.2f}', 'info')
            + '.'
        ).format(**info))
    else:
        print((
            'Si se envían ' + Console.bold('${amount:,.2f}', 'info')
            + ', se recibirán ' + Console.bold('${real:,.2f}', 'success') + '.'
        ).format(**info))

    if args.verbose:
        wide = len('{amount: ,.2f}'.format(**info)) + 1

        print()

        print((
            'Tarifa base de comisiones PayPal: '
            + Console.bold('{0}%')
            + ' + ${1:.2f} USD'
        ).format(
            args.commision,
            args.base
        ))

        print(Console.bold('Cálculos:'))
        print((
            ' Enviado:  '
            + Console.f(' {amount: #' + str(wide) + ',.2f}', 'cyan')
        ).format(**info))
        print((
            ' Comisión: '
            + Console.f(' {tax: #' + str(wide) + ',.2f}', 'red')
        ).format(**info))
        print((' {0:->' + str(wide + 11) + '}').format(''))
        print((
            ' Recibido: '
            + Console.bold(' {real: #' + str(wide) + ',.2f}', 'green')
        ).format(**info))


if __name__ == "__main__":
    main()
