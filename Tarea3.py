from ord import *

def _4():
  print("4")
  print(f"a) 13: {raices_primitivas(13)}")
  print(f"b) 58: {raices_primitivas(58)}")
  print(f"c) 202: {raices_primitivas(202)}")
  print(f"d) 625: {raices_primitivas(625)}")
  print(f"e) 1458: {raices_primitivas(1458)}")

def _8():
  print("Script para ayudar ej8")
  print(raices_primitivas(17))
  print(raices_primitivas(23))

def _10():
  print("función auxiliar para ej 10")
  print("buscamos la raiz 15 mod 29")
  print(root(15, 29, True))
  print("buscamos la raiz 20 mod 127")
  print(root(20, 127, True))
  print("buscamos la raiz 11 mod 31")
  print(root(11, 31, True))
  

_4()
_8()
_10()

