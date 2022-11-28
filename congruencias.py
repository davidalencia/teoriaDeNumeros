from functools import reduce 

class CI: 
  
  """
  cX=a (mod m)
  """
  def __init__(self, c, a, m):
    self.c = c%m
    self.a = a%m
    self.m = m
    
  def resuelve(self, x):
    return (x*self.c)%self.m == self.a
    
  
def encuentra_congruencia(cil):
  espacio = reduce(lambda acc, ci: acc*ci.m, cil, 1)+1
  for x in range(0, espacio):
    if reduce(lambda acc, ci: acc and ci.resuelve(x), cil, True):
      return x

#print(encuentra_congruencia([CI(101, 2, 103)]))
#print(encuentra_congruencia([CI(1, 5, 7), CI(1, 7, 11), CI(1, 3, 13)]))


def _4():
  print(encuentra_congruencia([CI(8, 14, 24)]))
  print(encuentra_congruencia([CI(57, 108, 4)]))
  print(encuentra_congruencia([CI(27, 1, 51)]))
  print(encuentra_congruencia([CI(980, 1500, 1600)]))

def _5():
  print(encuentra_congruencia([CI(1, 2, 910), CI(1, 80, 350)]))
  print(encuentra_congruencia([CI(3, 2, 4), CI(4, 1, 5), CI(6, 3, 5)]))
  print(encuentra_congruencia([CI(1, 3, 10), CI(1, 8, 15), CI(1, 5, 84)]))
  print(encuentra_congruencia([CI(1, 5, 7), CI(1, 7, 11), CI(1, 3, 13)]))




def _6a():
  for x in range(190, 220+1):
    if CI(1,1,2).resuelve(x) and\
      CI(1,2,3).resuelve(x-12) and\
      CI(1,4,7).resuelve(x-36):
      return x

      

def _6b():
  for x in range(31_500_000, 31_500_500+1):
    if CI(1,7,10).resuelve(x) and\
       CI(1,3,9).resuelve(x) and\
       CI(1,4,7).resuelve(x):
      return x


