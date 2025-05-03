"""решение задачи на Python Напишите программу, на вход которой подаётся прямоугольная матрица в виде последовательности строк. После последней строки матрицы идёт строка,
содержащая только строку "end" (без кавычек, см. Sample Input).

Программа должна вывести матрицу того же размера, у которой каждый элемент в позиции i, j равен сумме элементов первой матрицы на позициях (i-1, j), (i+1, j), (i, j-1), (i, j+1).
У крайних символов соседний элемент находится с противоположной стороны матрицы.

В случае одной строки/столбца элемент сам себе является соседом по соответствующему направлению.

входные данные:

Кейс 1 : Вход - 1 Выход - 4

Кейс 2:(в строку) Вход - 15 -4 8 3 Выход - 29 15 15 29

Кейс 3: Вход - (в столбец) 0\n 7 9 12 Выход -(в столбец) 19 23 37 33

Кейс 4: Вход - 2 2 2 3 0 5 8 -4 3 5 1 0 Выход - 23 -4 11 12 10 2 0 15 5 10 5 19

Кейс 5: Вход - 2 2 3 5 -1 7 0 1 Выход - 7 10 11 15 17 4 3 9

Кейс 6 : Вход - 9 5 3 0 7 -1 -5 2 9 Выход - 3 21 22 10 6 19 20 16 -1 Кейс 1 : Вход - 1 Выход - 4

Кейс 2: Вход - 15 -4 8 3 Выход - 29 15 15 29

Кейс 3: Вход - 0 7 9 12 Выход - 19 23 37 33 Кейс 4: Вход - 2 2 2 3 0 5 8 -4 3 5 1 0 Выход - 23 -4 11 12 10 2 0 15 5 10 5 19

Кейс 5: Вход - 2 2 3 5 -1 7 0 1 Выход - 7 10 11 15 17 4 3 9"""
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
