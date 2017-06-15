# Odd /Even

def oddEven():
    for i in range (1,2001):
        if i%2==0:
            print "Number is "+str(i)+". This is an even number."
        else:
            print "Number is "+str(i)+". This is an odd number."

oddEven()

# Multiply
def multiply(a, c):
    new=[]
    for i in range (0, len(a)):
        new.append(a[i]*c)
    return new

a = [2,4,10,16]
b = multiply(a, 5)
print b



# Hacker Challenge (!!!Not Finished!!!)
def hackerChanllenge(arr):
    new_array=[]
    for j in range (len(arr)):
        small_list = []
        for k in range (arr[j]):
            small_list.append(1)
        new_array.append(small_list)
    return new_array

x= hackerChanllenge(multiply([2,4,5],3))
print x
