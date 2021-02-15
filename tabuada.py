n = int(input())

def tabuada(n):
    for i in range(1, 11):
        print('{} x {} = {}'.format(i , n , i * n))

tabuada(n)        