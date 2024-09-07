def func1():
  try:
    num = int(input("Enter the number: "))

    for i in range(1,11):
     print(f"{num}X{i}={num*i}")
     return 0
  except :
   print("this not integer")
   print("this is the end")
   return 1

  finally:
    print("Always Runss")
x = func1()
print(x)
