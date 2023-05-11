#2
def fact(func):
    def warapper(*args,**kwargs):
        print(24+100)
    return warapper
@fact
def fuction(a,b,c):
    return a*b*c
fuction(1,2,1)
