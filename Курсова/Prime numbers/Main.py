import Fermat
import Miller_Rabin
import Solovay_Strassen
import random
import time


# A function that checks the time required for initialization of necessary elements
# such as list of numbers which we test and a matrix of numbers generated randomly
# in order to have same random numbers in each algorithm and
# the time for completion of each probabilistic primality test's algorithms
# They are Fermat's, Miller_Rabin's and Solovay_Strassen's algorithms
def Time_test():
    print("Input the integer quantity of numbers ")
    n = int(input())
    print("Input the quantity of times to check the primality of numbers")
    # a value that defines how much random numbers we use
    # to improve the correctness of probabilistic algorithms
    k = int(input())
    if k <= 0:
        print("k must be > 0")
        Time_test()
        return
    random_list_of_nums = []
    r = []
    a = []
    start = time.time()
    for i in range(0, n):
        random_list_of_nums.append(random.randint(1, 1000000))
        for j in range(0, k):
            a.append(random.randint(1, random_list_of_nums[i]))
        r.append(a)
        a = []
    end = time.time()
    print("Initialization ", end - start)
    start = time.time()
    for i in range(n):
        Fermat.isPrime(random_list_of_nums[i], k, r[i])
    end = time.time()
    print("Fermat's time is - ", end - start)
    start = time.time()
    for i in range(n):
        Miller_Rabin.isPrime(random_list_of_nums[i], k, r[i])
    end = time.time()
    print("Miller_Rabin's time - ", end - start)
    start = time.time()
    for i in range(n):
        Solovay_Strassen.isPrime(random_list_of_nums[i], k, r[i])
    end = time.time()
    print("Solovay_Strassen's time - ", end - start)


# A function that allows us to determine whether or not
# a given number is prime using all 3 algorithms;
# True - Prime; False - Composite;
def test():
    print("Input k>0 (probability has a direct dependency on k)")
    k = int(input())
    if k <= 0:
        print("k must be > 0")
        test()
        return
    print("Input number to check if it's prime or not")
    n = int(input())
    r = []
    if n <= 0:
        return print("A number can't be prime if it's <= 0")
    for i in range(k):
        r.append(random.randint(1, n))
    print("Fermat's algorithm ", Fermat.isPrime(n, k, r))
    print("Miller_Rabin's algorithm", Miller_Rabin.isPrime(n, k, r))
    print("Solovay_Strassen's algorithm", Solovay_Strassen.isPrime(n, k, r))


func = input("Input 'test' to check if a number is prime or 'time' to check the performance of methods\n")
if func == "test":
    test()
elif func == "time":
    Time_test()
else:
    print("Wrong input")
