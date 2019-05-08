from sys import argv
from os import system
from time import sleep
import MeCab

speed = 0.05
m = MeCab.Tagger('-Ochasen')

with open(argv[1]) as file:
    text = m.parse(file.read()).split('\n')

total = len(text)
counter = 0

system('clear')
print(f'{total} words, {int(speed * total)} seconds')
print('ready...')
sleep(3)

for line in  text:
    
    system('clear')
    
    if line:
        word = line.split()[0]

    if word != 'EOS':
        print(word)
        print(f'{total - counter} words\n{int(speed * (total - counter))} seconds remain')

    counter = counter + 1
    sleep(speed)
    

