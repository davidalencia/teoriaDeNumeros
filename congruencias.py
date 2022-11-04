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

print(encuentra_congruencia([CI(101, 2, 103)]))
#print(encuentra_congruencia([CI(1, 5, 7), CI(1, 7, 11), CI(1, 3, 13)]))

def _6a():
  for x in range(31_500_000, 31_500_500+1):
    if CI(1,7,10).resuelve(x) and\
       CI(1,3,9).resuelve(x) and\
       CI(1,4,7).resuelve(x):
      return x

print(2175%7)
