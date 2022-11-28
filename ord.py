from funcionesAritmeticas import phi

"""
ord_{m}(n)
"""
def ord(n, m, verbose=False):
  for i in range(1, phi(m)+1):
    if verbose:
      print(f"{n}^{i}%{m}={pow(n, i)%m}")
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
 regresa kin
"""
def ind(g , a, m):
  for i in range(1, phi(m)+1):
    if pow(g, i)%m == a:
      return i

def root(a, m, verbose=False):
  for i in range(m):
    if verbose:
      print(f"({i}*{i})%{m} = {(i*i)%m}")
    if (i*i)%m == a:
      return i




