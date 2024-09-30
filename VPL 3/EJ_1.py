"""
Debido a la ambigüedad en el enunciado, el presente código
tiene en cuenta que: en las combinaciones de letras y dígitos,
estos puedan repetir valores, de manera que puede haber códigos
PAS-AA444444-00:00, PAS-AB414414-00:00, PAS-AC444444-00:00, etc.
Debido a esto, el número total de códigos generados es de 562500000.
(5^2 letras * 5^6 dígitos * 24 horas * 60 minutos = 562500000 códigos)
Como es un número bastante grande, el código puede tardar en ejecutarse.
Gracias por su comprensión :)
"""

import re
import itertools

def generar_combinaciones(caracteres, longitud):
    return [''.join(comb) for comb in itertools.product(caracteres, repeat=longitud)]

def generar_horas():
    return ['{:02d}:{:02d}'.format(hh, mm) for hh, mm in itertools.product(range(24), range(60))]

patron_letras = re.compile(r'[ABCDE]{2}')
patron_digitos = re.compile(r'[01234]{6}')

letras = generar_combinaciones('ABCDE', 2)
digitos = generar_combinaciones('01234', 6)
horas = generar_horas()

def generar_codigos(letras, digitos, horas):
    for ll, dd, hh in itertools.product(letras, digitos, horas):
        yield f'PAS-{ll}{dd}-{hh}'

total_codigos = sum(1 for _ in generar_codigos(letras, digitos, horas))

print(total_codigos)