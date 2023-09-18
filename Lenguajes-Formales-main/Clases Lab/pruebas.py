### para mostrar la palabra más larga en una cadena
# txt = input()

# #your code goes here
# txt2=None
# for i in txt.split(' '):
    
#     if txt2==None:
#         txt2=i
#     elif len(i)>len(txt2):
#         txt2=i

# print (txt2)

### Generar una lista de una palabra
# def make_word():
#   word = ""
#   for ch in "spam":
#     word +=ch
#     yield word

# print(list(make_word()))

### Ejemplo recursividad 1
# def fib(x):
#   if x == 0 or x == 1:
#     return 1
#   else: 
#     return fib(x-1) + fib(x-2)
# print(fib(4))

### ejemplo de filter y lambda
# nums = {1, 2, 3, 4, 5, 6}
# nums = {0, 1, 2, 3} & nums
# nums = filter(lambda x: x > 1, nums)
# print(len(list(nums)))

### ejempl recursividad 2
# def power(x, y):
#   if y == 0:
#     return 1
#   else:
#     return x * power(x, y-1)
		
# print(power(2, 3))

### fibonacci secuencia
# num = int(input())


# def fibonacci(n):
#     if n <= 1:
#         return n
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)


# for i in range(num):
#     print(fibonacci(i))

###
# def func(**kwargs):
#   print(kwargs["zero"])

# func(a = 0, zero = 8)

###
for i in range(10):
  try: 
    if 10 / i == 2.0:
      break
  except ZeroDivisionError:
    print(1)
  else:
    print(2)