import redis
r = {}
def hit(usr):
  if usr not in r:
     r[usr] = 0
  r[usr] = r[usr] + 1

def getHit(usr):
  return (r[usr])

