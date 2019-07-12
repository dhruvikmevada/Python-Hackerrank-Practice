import string

def spellCorrect(str):
    j=0
    for i in str:
        if i.isalpha() or i in string.punctuation and i!='.':
            print(i,end="")
        elif i=='.' and str[j+1].isalpha():
            print(". ", end="")
        elif i.isspace() and  str[j+1].isalpha():
            print(" ",end="")
        j+=1

def main():
    inputStr=input('Enter Sentence:')
    spellCorrect(inputStr)

if __name__ == '__main__':
    main()