def exploder(string,n):
    print(string*n)
def myfun(function,*args,**kwargs):
    function(*args,**kwargs)
myfun(exploder,'guvi',3)
