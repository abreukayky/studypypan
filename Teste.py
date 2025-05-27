import pandas as pd

a = int(10)
b = float(2.2)
c = 45
d = "testando"

print (a+b)
print (a + c)
print (b + c)

if (a>c):
    print(d)
else: print(a)

for i in range (0,10):
    print(i)

while a>b:
    print (b)
    b+=1

cont = 1

while cont <10:
    idade = int(input("Insira sua idade:"))


    if idade < 12:
        print ("crianca")
elif 12<= idade < 18:
    print ("aborrecentge")
elif 18 <= idade < 60:
    print("adulto")
else:
    print("IDOSO")

cont= cont +1 
    