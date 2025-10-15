def digitize(n):
  n = str(n)
  list_n = []
  for i in n:
    list_n.append(int(i))
  list_n.reverse()
  return list_n
  
print(digitize(1234))
