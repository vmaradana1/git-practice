milkshakes ={'1':'Banana', '2': 'strawberry'}
sam_money= float(input("how much do you have ? "))
while True:
    waiter = input("what can i fix for you? : ")
    if waiter.lower() == 'q':
        print("GOOD LUCK !")
        break
    if waiter == '1':
            newlist= milkshakes.get(waiter)
            print (f"you have selected {newlist}")
            if sam_money < 1.5:
                print("No Money GET OUT !!!!!")
                break
            else:
                print (f"Here is your {newlist} drink ")
                sam_money -= 1.5
                print (f"Here is your balance {sam_money:.2f}")
    elif waiter == '2':
            newlist= milkshakes.get(waiter)
            print (f"you have selected {newlist}")
            if sam_money < 1.65:
                print("No Money GET OUT !!!!!")
                break
            else:
                print (f"Here is your {newlist} drink ")
                sam_money -= 1.65
                print (f"Here is your balance {sam_money:.2f}")
    else:
        print ("WRONG OPTION!!!!")