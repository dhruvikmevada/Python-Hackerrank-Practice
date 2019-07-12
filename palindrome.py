def palindromeRecognizer(str1):
    strRev=''
    str=''
    for s in str1:
        if s.isalnum():
            str+=''.join(s)

    for s in str:
        strRev=s+strRev

    if str == strRev:
        print('palindrome')
    else:
        print('Not palindrome')

def main():
    str=input('Enter String to verify:')
    palindromeRecognizer(str.lower())

if __name__ == '__main__':
    main()