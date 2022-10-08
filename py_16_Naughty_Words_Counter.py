# Counting the juicy word in Django / any text added in line 12.

MovieLength_WholeHour = 2     # Django 2h 45m long
MovieLength_RestMinutes = 45
MovieLength = MovieLength_WholeHour * 60 + MovieLength_RestMinutes

wordList = ['motherfucker', 'fucker', 'fuck', 'bitch', 'shit', 'nigger', 'damn', 'asshole', 'dick', 'cunt']
subtitleList = []
dicky = {}

try:
    file = open(r'py_16_Naughty_Words_Counter_Django.Unchained.2012.sub.txt','r+') 
    fileList = list(file)
    slicedList = []

    for i in range(len(fileList)):    # cutting up the text, making all the items lowercase
        sliced = fileList[i].split()
        for k in sliced:
            k = k.lower()
            slicedList.append(k)      # collecting the new/transformed items in a new list

    for i in wordList:                # counting the words / beware the "fuck" appearances in words like "fucker", "motherfucker"
        counter = 0
        for k in range(len(slicedList)):
            if i in slicedList[k]:
                counter += 1
        dicky[i] = counter

    dicky['fucker'] = dicky['fucker'] - dicky['motherfucker']
    dicky['fuck'] = dicky['fuck'] - dicky['fucker'] - dicky['motherfucker']
    dicky['n**ger'] = dicky.pop('nigger')

    allSum = 0                    # sum all the naughty words
    for i in dicky.keys():
        allSum = allSum + dicky[i]

    score = allSum / MovieLength
    scoreF = format (score, '.0%')

    print()
    print('-' * 10 + ' The Naughty Report ' + 10 * '-')
    print()
    for k, v in dicky.items():
        print(k + ': ' + str(v))

    print()
    print('Your movie`s Tarantinometer score: ' + scoreF)
    print()
    file.close()

except FileNotFoundError:
    print()
    print('The path is incorrect.')
    print()
