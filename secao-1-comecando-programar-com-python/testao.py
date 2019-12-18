def conta2(n):
  s = ''
  for i in range(n):
    s = s + str(i)
  return s.count('2')

print(conta2(30))