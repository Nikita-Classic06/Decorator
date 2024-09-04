

def is_prime(func):
    def wraper(*args, **kwargs):
        rez = func(*args, **kwargs)
        for i in range(2,rez):
            if rez % i == 0:
                print( "Составное")
                return rez
        print("Простое")
        return rez
    return wraper

@is_prime
def sum_three(*args):
    s = 0
    for i in args:
        s+=i
    return s



result = sum_three(2, 3, 6)
print(result)