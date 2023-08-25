import sys
f = list(map(str.strip , sys.stdin))
ar=[]
for i in  f[:-1]:
    ar.append(list(map(int,i.split())))
n=[[0]*len(ar[i]) for i in range(len(ar))]
hor=False
if len(ar)==1:
    for i in ar:  
        num=0
        if len(i)>1:
            temp=[]
            for j in range(len(i)):
                if j ==0:
                    num+=i[j]+i[j]+i[len(i)-1]+i[j+1]
                    temp.append(num)
                    num=0
                elif j==len(i)-1:
                    num+=i[j]+i[j]+i[j-1]+i[0]
                    temp.append(num)
                    num=0
                else:
                    num+=i[j]+i[j]+i[j-1]+i[j+1]
                    temp.append(num)
                    num=0
            n=temp
            hor=True
        else: 
            num+=i[0]+i[0]+i[0]+i[0]
            n[0]=num             
else:
    for i in range(len(ar)):
        
        if len(ar[i])==1:
            
            num=0
            if i==0:#i[-1]
                num+=ar[-1][0]+ar[i+1][0]+ar[i][0]+ar[i][0]
            elif i==len(ar)-1:    
                num+=ar[i-1][0]+ar[0][0]+ar[i][0]+ar[i][0] 
            else:     
                num+=ar[i-1][0]+ar[i+1][0]+ar[i][0]+ar[i][0]
            n[i]=num         
        else:
            for j in range(len(ar[i])): 
                num=0
                if i==0:#i[-1]
                    if j ==0:
                        num+=ar[len(ar)-1][j]+ar[i+1][j]+ar[i][len(ar[i])-1]+ar[i][j+1] 
                    elif j==len(ar[i])-1:
 
                        num+=ar[len(ar)-1][j]+ar[i+1][j]+ar[i][j-1]+ar[i][0]
                    else:
                        num+=ar[len(ar)-1][j]+ar[i+1][j]+ar[i][j-1]+ar[i][j+1]
                elif i==len(ar)-1:
                    if j ==0:
                        num+=ar[i-1][j]+ar[0][j]+ar[i][len(ar[i])-1]+ar[i][j+1] 
                    elif j==len(ar[i])-1:
                        num+=ar[i-1][j]+ar[0][j]+ar[i][j-1]+ar[i][0]
                    else:
                        num+=ar[i-1][j]+ar[0][j]+ar[i][j-1]+ar[i][j+1]
                else:
                    if j ==0:
                        num+=ar[i-1][j]+ar[i+1][j]+ar[i][len(ar[i])-1]+ar[i][j+1] 
                    elif j==len(ar[i])-1:
                        num+=ar[i-1][j]+ar[i+1][j]+ar[i][j-1]+ar[i][0]
                    else:
                        num+=ar[i-1][j]+ar[i+1][j]+ar[i][j-1]+ar[i][j+1]
                n[i][j]=num
for i in n:
    if type(i)==int:
        if hor:
            print(i,end =' ')
        else:
            print(i)
    else:
        print(*i)
