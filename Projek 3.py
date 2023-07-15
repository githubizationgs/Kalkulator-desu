def calculator ():
    print ('Basic Calculator')
    print ('')

    while True:
        n1 = float(input('Insert a number: '))
        n2 = float(input('Insert other number: '))

        sum = n1+n2
        sub = n1-n2
        multi = n1*n2
        div = n1/n2

        print("Menu:")
        print("1. Addition")
        print("2. Substraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. None of them")

        option = input("Enter option: ")


        if option == '1':
            print(sum)
        elif option == '2':
            print(sub)
        elif option == '3':
            print(multi)
        elif option == '4':
            print(div)
        elif option == '5':
            print("Sadly, the current operation you've chosen is not available. Thanks for trying! :)")
        else:
            print("Invalid")
            continue

calculator()



