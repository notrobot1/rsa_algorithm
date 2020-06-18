from gmpy import invert

#простое число
def prime(num):
   if num >1:
      for i in range(2, num):
         if(num % i)==0:
            return False
      else:
         return True
   else:
      return False

#взаимо простое число
def gcd(a, b):
    if b == 0: return a
    return gcd(b, a % b)

def gcdex(a, b):
   print('')

##############################################################################
arr=[]

p=999613

q=7
n=p*q
print(n)
eu = (p-1)*(q-1)

for i in range(100):
   if prime(i) and i < eu:
      arr.append(i)

#составляем список взаимо простых чисел eu
wprime = list(filter(lambda a: gcd(a, eu) == 1, [x for x in arr]))

e = wprime[0] 
publickkey = {e,n} #публичный ключ
d = invert(e,eu)

secretkey = {d,n}#секретный ключ
######################################шифруем
p = int(input()) #сообщение не может быть больше n
cripto = pow(p, e,n)
print(cripto)
######################################дешифруем
decripto = pow(cripto, d,n)
print(decripto)

