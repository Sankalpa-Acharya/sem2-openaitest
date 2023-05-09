

cnt=0
cnt1=0
l=['meera','tom','jerry',('max','bob')]
for ele in l:
 if isinstance(ele,tuple):
  cnt+=1
 else:
  cnt1+=1
print("no of boys:",cnt)
print("no of girls:",cnt1)