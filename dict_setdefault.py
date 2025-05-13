'''


В программе существует переменная employees, которая хранит список словарей (переменная уже существует, создавать ее не надо). 
Напишите программу, которая создает словарь, где ключами будут должности, а значениями — количество сотрудников на этой должности.
Получившийся словарь необходимо сохранить в переменной positions.

Sample Input:

[
   {"name": "Bob", "age": 24, "position": "Designer"},
   {"name": "Alice", "age": 30, "position": "Developer"},
   {"name": "Charlie", "age": 28, "position": "Manager"}
]

Sample Output:

{'Designer': 1, 'Developer': 1, 'Manager': 1}


'''
positions=dict()
for i in employees:
    positions[i['position']]=positions.setdefault(i['position'],0)+1
