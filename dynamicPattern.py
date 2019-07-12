"""

Description: This program takes numeric input and prints the * pattern accordingly.

"""


def main():
    totalNo = int(input('How many line you have to enter:'))

    if totalNo != 0:
        mylist = []
        for i in range(0, totalNo):
            number = int(input('Enter number:'))
            mylist.append(number)

        # print(list)

        for i in range(0, totalNo):
            for j in range(0, mylist[i]):
                print('*', end='')
            print('')

    else:
        print("Invalid Input")


if __name__ == '__main__':
    main()
