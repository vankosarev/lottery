import json

with open('all_ticket_numbers.json', 'r', encoding='utf-8') as file:
    numbers = json.load(file)

nomera = numbers.keys()
print(nomera)

a = input('номер: ')
#for i in nomera:
 #   for item in numbers[i]:
 #       for p in numbers[i]:  
  #          if p == a:
 #               print(item, numbers[i])
