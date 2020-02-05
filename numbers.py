def numint(x):
    return int(x) + n

def numfloat(x):
    return float(x) + n

def numcomplex(x):
    return float(x) + n


print("X will be 5.254878")
n = input("Enter any number:")
if n.is_integer():
    print("Integer:", numint(5.254878))
else:
    print("Not an Integer:", numcomplex(5.254878))
