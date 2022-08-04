n = 0

def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
res = fact(n)    
print(res)


# 5!
# 5*24
# 4*6
# 3*2
# 2*1
# 1*1
