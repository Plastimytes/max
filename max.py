#max consecutive char.s
str=input("Give a string: ")

counter={}
for i in str:
    if i in counter:
        counter[i]+=1
    else:
        counter[i]=1

mx=max(counter,key=counter.get)  
print(f"character: {mx}")          