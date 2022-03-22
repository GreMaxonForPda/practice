wordList = []
textList = []
textWord = ''
counter = [0, 0, 0]
temp = 0
wordCount = 3

def textAdd():
    global textWord
    textWord = input('Слово из текста: ')
    textList.append(textWord)

for i in range(wordCount):
    print('Введите', i + 1, 'слово: ', end = '')
    wordList.append(input())

print()

textAdd()
while textWord != 'end':
    textAdd()

for i in wordList:
    for x in textList:
        if i == x:
           counter[temp] += 1
    temp += 1

print()

for i in range(wordCount):
    print(wordList[i] + ':', counter[i])
