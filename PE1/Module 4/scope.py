def mult(x):
    var = 7
    return x * var

var = 3
print(mult(7))    # outputs: 49
#######################################
var = 2

def mult_by_var(x):
    return x * var

print(mult_by_var(7))    # outputs: 14
#######################################
a = 1

def fun():
    global a
    a = 2
    print(a)

fun()
a = 3
print(a)    # outputs: 2, 3
#############
a = 1

def fun():
    global a
    a = 2
    print(a)

a = 3
fun()
print(a)    # outputs: 2
############# 2
