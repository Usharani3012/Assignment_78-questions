# n1=[1,2,3,4]
# n2=[5,6,7,8]
# result=map(lambda x,y:x+y,n1,n2)
# print(list(result))

def fun(n):
    if n%2==0:
        return True   
    else:
        return False 
l=[1,2,3,4,5,6]
filterd=filter(fun,l)
print(list(filterd))