# Task
# You need to return a string that looks like a diamond shape when printed on the screen, using asterisk (*) characters. Trailing spaces should be removed, and every line must be terminated with a newline character (\n).

# Return null/nil/None/... if the input is an even number or negative, as it is not possible to print a diamond of even or negative size.

from functools import reduce
def diamond(n):
    # Make some diamonds!
    data = []
    if n%2 == 0 or n<1 : 
        return None
    else: 
        for i in range(1,n+1,2):
            data.append("*"*i+"\n")
    
    for i in range(len(data)):
        data[i] = data[i][::-1] + " "*(len(data)-i)
        data[i] = data[i][::-1]

    return reduce(lambda strok, sim:strok + sim[1:],data + data[-2::-1], "") 
print(diamond(13))
print('      *\n     ***\n    *****\n   *******\n  *********\n ***********\n*************\n ***********\n  *********\n   *******\n    *****\n     ***\n      *\n')