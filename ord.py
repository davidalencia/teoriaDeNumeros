from funcionesAritmeticas import phi

"""
ord_{m}(n)
"""
def ord(n, m):
  for i in range(1, phi(m)+1):
    if pow(n, i)%m ==1:
      return i
  
"""
  Raices primitivas de m
"""
def raices_primitivas(m):
  raices = []
  _phi = phi(m)
  for i in range(m):
    if ord(i,m) == _phi:
      raices.append(i)
  return raices

"""
 ind_g(a) = k (mod m)
 regresa k
"""
def ind(g , a, m):
  for i in range(1, phi(m)+1):
    if pow(g, i)%m == a:
      return i

print(ind(2, 3, 5))


