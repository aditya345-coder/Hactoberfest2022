# Python Program For Print multiplication table of any number
num = int(input("Enter the number whose multiplication table you want: "))
for i in range(1,11):
    print(num," * ",i," = ",num*i)