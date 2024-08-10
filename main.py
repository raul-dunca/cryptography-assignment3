import random

def binary(x):
    # turns a number in a kind of binary representation as a list: 21 -> [1,-1,4,-1,16]

    power=[]
    cnt=0
    while x>0:
        if x%2==1:
            power.append(2**cnt)
        else:
            power.append(-1)
        x=x//2
        cnt+=1
    return power

def decompose_2(x):
    p=0
    while x%2==0:                               # returns how may times a number is divisible by 2
        x=x//2
        p+=1
    return p

def repeated_squaring(b,n,k):
    a=1
    if k == 0:
        return a
    c=b
    power=binary(k)
    if power[0]==1:                             # if k odd
        a=b                                     #special case: add b^1 to rezult
    for i in range(1, len(power)):
        c =(c**2)%n                             #we calculate b^(2^x)%n
        if power[i]!=-1:                        #if the power of 2 is in k's binary repr save it
            a = (c*a)% n
    return a

def gen_seq():

    b = random.randint(2, n - 1)
    while b in selected_bases:
        b = random.randint(2, n - 1)        #choose a random base 1<b<n
    print("b="+str(b))
    sequence = []
    good_seq = False

    for i in range(0, s + 1):
        sequence.append(repeated_squaring(b, n, 2 ** i * t))            # calculate a sequence using repeated square
                                                                        # [b^t,b^2t,b^(2^2)t,...
    if sequence[0] == 1:
        good_seq=True                                                   #good seq if starts with 1
    else:
        for i in range(len(sequence)):
            if sequence[i] == n - 1 and i != len(sequence) - 1 and sequence[i + 1] == 1:    # or we have -1 followed by 1
                good_seq = True

    print(sequence)

    return good_seq



n=int(input("n= "))
k=int(input("k= "))
prime=True

if n%2==0:
    print ("Not prime")
else:
    selected_bases = []
    s=decompose_2(n-1)
    t=(n-1)//2**s
                            # n is decomposed in n-1=2^s*t
    for i in range(k):

        if gen_seq()==False:
            print(str(n)+" is not a prime")
            prime=False
            break

    if prime:
        probability=1-(1/4**k)
        print(str(n)+" is "+ str(probability) +" prime")


#problmea 1