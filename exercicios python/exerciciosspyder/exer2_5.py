# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 22:31:14 2019

@author: rudim
"""

# importar função pow
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
print ()
print ('a_raiz_quadrada = ',a_raiz_quadrada)
print ('a_raiz_cubica = ',a_raiz_cubica)
print ('a_raiz_quarta = ',a_raiz_quarta)
print ('a_raiz_b = ',a_raiz_b)
print ()
print ('obrigado')
