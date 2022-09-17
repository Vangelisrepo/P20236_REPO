import numpy as np

a=np.arange(1,1000)
my_list = []
c =""
def gargamel(b):
    for i  in b :
        r=0
        result = 0
        for x in str(i):
            my_list.append(int(x))

        for f in range(len(my_list)):
            result = (my_list[r] ** (r + 1)) + result
            r = r + 1
            if result == i:
               c = "SMURF"
                



        my_list.clear()
    return c
gargamel(a)


