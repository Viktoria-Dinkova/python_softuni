# Напишете програма, която чете текст от конзолата(стринг) и го принтира, докато не получи командата "Stop".

text = ''

while 1:
    text = input()

    if text == 'Stop':
        break
        
    print(f'{text}')