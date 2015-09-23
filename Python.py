m=[0,0,0,0,0,0,0]
summ=0
for a in range(0,len(m)):
        m[a]=int(input("Enter number "+str(a+1)+": "))
        summ+=m[a]
avg=summ/len(m)

print("Average is "+str(avg))
