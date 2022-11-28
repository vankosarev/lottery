from PIL import Image, ImageDraw, ImageFont
import lotery_v2
import random
import json


ticket = Image.open("ticket.png")  
idraw = ImageDraw.Draw(ticket)

font = ImageFont.truetype('Tsarevich.ttf', size=80,)
# idraw.text((855,436), text, font=font, fill = "#000000cc" )

all_ticket_No = []
for i in range(1,1000):
    a = i
    if a < 10:
        txt = f"0000{a}"
    elif a >= 10 and a < 100:
        txt = f"000{a}"
    elif a >= 10 and a < 1000:
        txt = f"00{a}"
    all_ticket_No.append(txt)

key_all_ticket_numbers = []
for i in range(1,1000):
    key_all_ticket_numbers.append(i)


all_ticket_numbers = {}
def print_number():
    ticket = Image.open("ticket.png")
    idraw = ImageDraw.Draw(ticket)
    with open('all_ticket_numbers.json', 'r', encoding='utf-8') as file:
        all_ticket_numbers = json.load(file)
        b = dict.keys(all_ticket_numbers)

    for i in b:
        key = i
        if key < i:
            pass
        elif key > i:
            key= i


    number_text = f"номер: {all_ticket_No[int(key)]}"
    lotery_v2.numbers.clear()
    lotery_v2.number.clear()
    lotery_v2.get_numbers()
    y = [436,516,596,436,516,596,436,516,596,436,516,596,436,516,596]
    y1 = [516,436,596,516,436,596,516,436,596,516,436,596,516,436,596]
    y2 = [596,436,516,596,436,516,596,436,516,596,436,516,596,436,516]
    ys = [y,y1,y2]
    yy = random.sample(ys,1)
    a = 0
    for i in lotery_v2.numbers:
        x = 855
        text = f'{i}'
        pos = i//10
        if pos >= 1:
            x += pos*80
        else:
            pass

        
        idraw.text((x,yy[0][a]), text, font=font, fill = "#000000cc")
        a += 1
    idraw.text((230,750), number_text, font=font, fill="#ffffff")
    ticket.save("ticket_try.png")


    all_ticket_numbers[key_all_ticket_numbers[int(key)]] = lotery_v2.numbers
    
    with open('all_ticket_numbers.json', 'w', encoding='utf-8') as file:
        json.dump(all_ticket_numbers,file,indent=4,ensure_ascii=False)

    lotery_v2.numbers.clear()
    print(f'выдал билет №{int(key) + 1}')



        
            
                 

