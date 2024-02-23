def fibonacciR(n):
    if (n==0 or n==1):
        return n
    else:
        return fibonacciR(n-1)+ fibonacciR(n-2)
n = int(input("Ingrese un número para calcular su fibonacci: "))
print(f"El resultado del fibonacci de {n} es: {fibonacciR(n)}")