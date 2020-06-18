Задаем два простых числа (для примера: p=999613, q=7)
<a href=" https://ru.wikipedia.org/wiki/Список_простых_чисел" >Список_простых_чисел </a>

Простое ли число проверка при помощи python
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
