a = []

def primes_sieve2(limit):
    a = [True] * limit                          # Initialize the primality list
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in range(i*i, limit, i):     # Mark factors non-prime
                a[n] = False

def check_arrange(prime_array, a):
    for x in range(0, len(prime_array)):
        for y in range(x+1, len(prime_array)):
            ##check combos for prime
            print(a[x], prime_array[y])



prime_list = list(primes_sieve2(20))


for x in range(0, len(prime_list)):
    for j in range(x+1, len(prime_list)):
        for l in range(j+1, len(prime_list)):
            for m in range(l+1, len(prime_list)):
                prime_check_list = [prime_list[x], prime_list[j], prime_list[l], prime_list[m]]
                print(check_arrange(prime_check_list, a))

            