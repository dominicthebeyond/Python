def gen(n):
  for i in range(n):
    yield i ** 2 # yield keyword is like a pause / yellow light / yeild sign
  
g = gen(1000000)

for i in g: 
  print(i)