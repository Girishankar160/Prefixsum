a=list(map(int,input().split()))
prefixsum=[]
sum=0
for i in a:
    sum+=i
    prefixsum.append(sum)
print(prefixsum)
