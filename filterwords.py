def filter_long_words(wordList,length):
    print(wordList)
    list=[]
    for i in wordList:
        if len(i) >= length:
          list.append(i)

    return list

def main():
    inputNumber=eval(input('How many number of words you want to enter:'))
    inputWordList=[]
    for i in range(0,inputNumber):
        inputWordList.append(input('Enter Word :'))
    filterLength=eval(input('Enter Word filter length:'))
    print('Filterd words are: ',filter_long_words(inputWordList,filterLength))

if __name__ == '__main__':
    main()