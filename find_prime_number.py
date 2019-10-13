import argparse


def is_prime_number(x):
    if x >= 2:
        for y in range(2,x):
            if not ( x % y ):
                return False
    else:
        return False
    return True

if __name__ =="__main__":
    inp = argparse.ArgumentParser(description='Until what number do you wish to check?')
    inp.add_argument('integer', metavar='N', type=int, nargs='+',
                     help='the integer to check')
    args = inp.parse_args()


    primes = 0

    if args.integer[0] > 100000:
        print('This is a very large number, it will take a while...')
            
    for i in range(args.integer[0]):
        if is_prime_number(i):
            primes += 1
            print(i)

    print("We found " + str(primes) + " prime numbers.")