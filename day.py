def even_od(num):
    if num%2==0:
        print("even")
    else:
        print("odd")
even_od (5)     

def number(a,n):
    for i in range(a,n-1,-1):
        print(i)
number(10,1)

def year(n):
    if n%4==0 and n%100!=0 or n%400==0:
        print("leap year")
    else:
        print("not leap year")
year(2020)            
