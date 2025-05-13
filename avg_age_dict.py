'''


В программе существует переменная employees, которая хранит список словарей (переменная уже существует, создавать ее не надо).
Напишите программу, которая находит и выводит в терминал средний возраст сотрудников. Если у сотрудника возраст не указан, его учитывать не нужно.

Sample Input:

[
   {"name": "Tom", "age": 24, "position": "Designer"},
   {"name": "Alice", "position": "Developer"},
   {"name": "Charlie", "age": 28, "position": "Designer"}
]

Sample Output:

26.0


'''
s=0
c=0
for i in employees:
    s+=i.get("age",0)
    c+=1 if i.get("age",0) else 0
print(s/c)
