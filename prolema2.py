c=eval(input('dati numarul de numere='))
b=str(input('Dati numerele='))
d=[]
d=b.split('\n')
y=[]
y.extend(d)
i=0
while i<=c :
    i+=1

    if (((y[0]+y[1])==13 )and((y[2]+y[3]))==13):
        print ('numar norocos')
    elif(((y[0]+y[1])!=13 )and((y[2]+y[3]))!=13) :
        print('numar ne norocos')