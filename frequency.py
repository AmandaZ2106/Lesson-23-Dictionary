test={'A':23,'B':23,'C':41,'D':23,'E':23}
print("The original dictionary:",test)
num=23
res=0
for key in test:
    if test[key]==num:
        res+=1
print(res)