def squareOfEvenNumber(list):
    result = [i**2 for i in list if i%2==0]
    print(result)

def main():
    totalInput=int(input('How many number you want to enter:'))
    inputList=[]
    for i in range(0,totalInput):
        inputList.append(int(input('Enter Number:')))
    squareOfEvenNumber(inputList)

if __name__ == '__main__':
    main()
