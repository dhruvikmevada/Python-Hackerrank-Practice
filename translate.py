def translate(inputStr):
    #translate text into swedish
    outputStr=''
    vowelStr='aeiouAEIOU'
    consonanatStr='bcdfghjklmnpqrstvwzyzBCDFGHJKLMNPQRSTVWXYZ'
    for str in inputStr:
        if str in vowelStr:
            outputStr+=''.join(str)
        elif str in consonanatStr:
            outputStr+=''.join(str+'o'+str)
        else:
            outputStr += ''.join(str)
    return outputStr

def main():
    inputStr=input('Enter String :')
    print(translate(inputStr))

if __name__ == '__main__':
    main()
