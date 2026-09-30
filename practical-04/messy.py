# messy.py
def p(a,b,c):
    x=a*b
    if c == 1:
        y=x+a
        z=y*2
    else:
        y=x-a
        z=y*3
    if z>50:
        r=z-10
    else:
        r=z+10
    return r

print (p (4,6,1))