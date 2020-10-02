# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 22:31:14 2019

@author: rudim
"""

# importar função pow
from math import pow, floor, ceil
# limpa área
print ('\n'*100)
print ('operações potenciação e radiciação')
a = float(input ('Entre com o valor de a:'))
b = float(input ('Entre com o valor de b:'))

#operações com pow

a_quadrado = pow (a,2)
a_cubo = pow (a,3)
a_quarta = pow (a,4)
a_elevado_b = pow (a,b)
a_raiz_quadrada = a**(1/2)
a_raiz_cubica = a**(1/3)
a_raiz_quarta = a**(1/4)
a_raiz_b = a**(1/b)
print ()
print ('Resultado operações potenciação')
print ()
print ('a= ',a,' b= ',b)
print ()
print ('a ao quadrado = ',a_quadrado)
print ('a ao cubo = ',a_cubo)
print ('a a quarta = ',a_quarta)
print ('a elevado a b = ',a_elevado_b)
print ()
print ('Resultado operações radiciação')
print ('piso')
print ('a_raiz_quadrada = ',floor(a_raiz_quadrada))
print ('a_raiz_cubica = ',floor(a_raiz_cubica))
print ('a_raiz_quarta = ',floor(a_raiz_quarta))
print ('a_raiz_b = ',floor(a_raiz_b))
print ()
print ('teto')
print ('a_raiz_quadrada = ',ceil(a_raiz_quadrada))
print ('a_raiz_cubica = ',ceil(a_raiz_cubica))
print ('a_raiz_quarta = ',ceil(a_raiz_quarta))
print ('a_raiz_b = ',ceil(a_raiz_b))
print ()
print ('arredondamento')
print ('a_raiz_quadrada = ',round(a_raiz_quadrada,2))
print ('a_raiz_cubica = ',round(a_raiz_cubica,2))
print ('a_raiz_quarta = ',round(a_raiz_quarta,2))
print ('a_raiz_b = ',round(a_raiz_b,2))
print ()