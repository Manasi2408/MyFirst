# magic ball

import random

message = [
'It is certain',
'It is decidedly so',
'Yes definitely',
'Reply hazy try again',
'Ask again later',
'Concentrate and ask again',
'My reply is no',
'Outlook not so good',
'Very doubtful'
]

print("Stuck? See this message : ")

number = random.randint(1,len(message))

print(message[number])