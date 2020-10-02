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
print ()
print ('Resultado operações')
print ()
print ('a= ',a,' b= ',b)
print ('a ao quadrado = ',a_quadrado)
print ('a ao cubo = ',a_cubo)
print ('a a quarta = ',a_quarta)
print ('a elevado a b = ',a_elevado_b)
print ()
print ('obrigado')