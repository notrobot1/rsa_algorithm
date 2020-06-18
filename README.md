Задаем два простых числа (для примера: p=999613, q=7)
<a href=" https://ru.wikipedia.org/wiki/Список_простых_чисел" >Список_простых_чисел </a>

Простое ли число проверка при помощи python:
  <pre>
<code>
  def prime(num):
   if num >1:
      for i in range(2, num):
         if(num % i)==0:
            return False
      else:
         return True
   else:
      return False
  </code>
   </pre>
   
Получаем публичный, приватный ключ:
<pre>
publickkey = {e,n} #публичный ключ
secretkey = {d,n}#секретный ключ
<pre>

Вводим число которое необходимо зашифровать:
<code> p = int(input()) </code>

<h3> Внимание!! </h3>

<code>p</code> не может быть больше <code>n=p*q</code> 
