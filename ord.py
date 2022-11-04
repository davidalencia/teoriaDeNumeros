from funcionesAritmeticas import phi

def ord(n, m):
  for i in range(1, phi(m)):
    if pow(n, i)%m ==1:
      return i
    
print(ord(21, 125))
