print ("Home Work 2")
print ("Ex_1")
a=10
a+=len(str(a))
a=str(a)
print("a=", a)

print ("Ex_2")
b=2
print(f"In padurea cu alune aveau casa {b} pitici")

print ("Ex_3")
a=10
a+1
print("a=", a)

print ("Ex_4")
a = input ("Valorea a=")
a += str(1)
print (a)
print ("Intr-o oarecare masura eroare nu apare) ")

print ("Ex_5")
txt = input("Denumire fisier:   ")
c = txt.split(".")
print("Extensia.",c[1])

print ("Ex_6")
a=['a','b','c','d']
print ("6.1 Valoarea expresiei este",a[int(int('3' * 2)) // 11] )
a.insert(0, 'n')
print (a)
del a[-2:]
print (a)
a.sort(reverse=True)
print(a)
b =a.copy()
del b[:2]
print (a)
print (b)

print ("Ex_7")
c={'scaune': 33, 'mese':22, 'mere':3}
total=sum(c.values())
elemente = ','.join(c)
print('Lista elemente:', elemente)
print('Numar total elemente:',total)