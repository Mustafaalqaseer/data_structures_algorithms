def fibonnaci(n):
    assert n>=0 and int(n) == n, 'integer has to be a positibe number'
    if n  in [0,1]:
        return n
    else:
        return fibonnaci(n-1) +fibonnaci(n-2)


def sumOfDigits(n):


    if n <=9:
        return n
    else:
        return sumOfDigits(int(n/10) + int(n%10))



def GCD(a,b):
    if b == 0:
        return a
    elif a == 0:
        return b
    else:
        return GCD(b,a % b)
    

print(GCD(20,-45))


def decimalToBinary(n):
     assert n>=0 and int(n) == n, 'Error cannot have a '
     if n == 0:
         return 0
     else:
         return n %2 + 10 * decimalToBinary(int(n/2))


print(decimalToBinary(75))



def recursiveRange(num):
    if num == 0:
        return num
    else:
        return num + recursiveRange(num-1)
    
print(recursiveRange(0))

def isPalindrome(strng):
    if len(strng) in [0,1]:
        return True
    if strng[0] != strng[-1]:
        return False
    return isPalindrome(strng[1:-1])


def isOdd(num):
    if num%2==0:
        return False
    else:
        return True

def someRecursive(arr, cb):
    if len(arr) == 0:
        return False
    if cb(arr[0]):
        return True
    
    return someRecursive(arr[1:], cb)


arr = [1,4,6,8]
print(someRecursive(arr,isOdd))



array2 = [10,23,23,23]

print(arr + array2)