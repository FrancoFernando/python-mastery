def else_loop(n):

   is_prime(n)

   print('Prime') if is_prime_2(n) else print('Not prime')

   print('Prime') if is_prime_3(n) else print('Not prime')

# with else -> confusing
def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            print('Not prime')
            break
    else:
        print('Prime')

# without else
def is_prime_2(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def is_prime_3(n):
    is_prime = True
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break
    return is_prime