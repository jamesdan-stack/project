#modelling a nigerian sim ussd command(glo) 

data = {100:"80 mb", 200:"160 mb", 500:"800 mb", 1000: "1.6 gb", 2000:"5.8gb", 3000: "9gb",5000:"22gb", 10000:"30gb", 20000:"50gb", 50000:"80gb", 100000:"100gb"}
my_number = "08151460038"
total = 300
balance = 200 



print("W22elcome to glo world")
print("     1 - data")
print("     2 - etopup")
print("     3 - brekete(enjoy 700percent on all reacharge and data)")
print("     4 - my tariff plans")
print("     5- borrow me credit and data")
print("     6 - VAS")
print("     7- exit")
opt = int(input("enter your deired command."))





while opt != "exit":

    #data command
    if opt == 1:

        print("Data")
        print("     1- buy data")
        print("     2- share data")
        print("     3 - gift data")
        print("     4 - check data balance")
        print("     5 - exit")
        opt1 = int(input("enter your choice."))

        while opt1 != "exit":

            if opt1 == 1:
                print("Buy data")
                print("     1 - daily (50, 100)")
                print("     2 - weekly (200, 500)")
                print("     3 - monthly(1000, 2000, 3000, 4500, 5000, 10000)")
                print("     4 - yearly(20000, 50000, 100000)")
                print("     5 - exit")
                opt00 = int(input("enter your like"))

                while opt00 != "exit":

                    if (opt00 == 1 or opt00 ==2 or opt00 == 3 or opt00 ==4):
                        print("data = (100:80 mb, 200:160 mb, 500:800 mb, 1000: 1.6 gb, 2000:5.8gb, 3000: 9gb,5000:, 10000:"", 20000:"", 50000:"", 100000:")
                        amount = int(input("enter the data plan you want to subscribe for."))
                         #checking if the acc bal is enough for data sub.
                        if amount > total:
                            print("your balance is not enough")
                            break

                        else:
                        #using a for loop to check infos in the dict.
                            for key , value in data.items():
                                if amount in data.keys():
                                    print("you have successfully subscribed for ", amount , " data plan")
                                    break
                        break


                    elif opt00 == 5:
                        print("bye")
                        break
                
                break
                    



            elif opt1 == 2:
                num = int(input("enter the number you would like share with?"))
                print("your data request has been sent.")
                break


            elif opt1 == 3:
                num = int(input("enter the number you would like share with?"))
                gift = int(input("enter the amount you would to gift"))

                if gift > balance:
                    print("your balance isnt enough")
                    break

                else:
                    balance = balance - gift
                    print("you have sucessfully gifted ", num, gift, "mb")
                    print("your balance is  ", balance)
                    break
            
            elif opt1 == 4:
                print("data balance is ", balance,"mb")
                break
            
            elif opt1 == 5:
                print("bye")
                break

        break



    #e-top up command
    elif opt == 2:

        print("E-topup")
        print("     1 - airtime")
        print("     2 - data")
        print("     3 - exit")
        opt2 = int(input("pls select"))

        while opt2 != "exit":

            if opt2 == 1:
                print("Airtime")
                print("     1- self")
                print("     2- exit")
                opt22 = int(input("pls make a choice"))
            
                if opt22 == 1:
                    print("5x recharge")
                    print("     1- self")
                    print("     2- third party")
                    print("     3- exit")
                    opt222 = int(input("pls select"))

                    if opt222 == 1:
                        e_recharge = int(input("pls how much do you want to recharge from bank!!"))
                        total_1 = e_recharge + total
                        print("your new balance is ", total_1)

                    elif opt222 == 2:
                        t_num = int(input("pls enter the num you wan recharge for."))
                        t_amt = int(input("pls enter the amount"))
                        print("your recharge request has been sent")

                    elif opt222 == 3:
                        print("bye")
                        break


                elif opt22 == 2:
                    print("bye")
                    break



            elif opt2 == 2:
                print("Data")
                print("     1- self")
                print("     2- third party")
                print("     3- exit")
                opt2222 = int(input("pls make  your choose "))

                if opt2222 == 1:
                    e_data = int(input("pls how much u wan sub from bank!!"))
                    total_2 = e_data + total
                    print("data request sent")

                elif opt2222 == 2:
                    t_number = int(input("pls enter the num you wan recharge for."))
                    t_amount = int(input("pls enter the amount"))
                    print("your recharge request has been sent")

                elif opt2222 == 3:
                    print("bye")
                    break



            elif opt2 == 3:
                break

        break


    #berekete command
    elif opt == 3:
        print(" BREKETE (enjoy 700 percent on all recharge and data.")
        print("     1- migrate now")
        print("     2- exit")
        opt3 = int(input("pls chose"))


        if opt3 == 1:
            print("you have succesfully migrated")
            break
        elif opt3 == 2:
            print("bye")
            break




    #my tarrif information
    elif opt == 4:

        print("MY TARIFF PLANS")
        print("     1- my pacakage")
        print("     2- check balance")
        print("     3- my number")
        print("     4- tarif informaton")
        print("     5- exit")

        opt4 = int(input("pls choose "))

        while opt4 != "exit":

            if opt4 == 1:
                print("you are on glo_yakata")
                break

            elif opt4 ==2:
                print("Check balance")
                print("     1- main account")
                print("     2- promo acccount 1")
                print("     3- promo account 2")
                print("     4- exit")

                opt44 = int(input("pls make a choice"))

                if opt44 == 1:
                    print("account balance is", balance, "mb")

                elif opt44 == 2 or opt44 ==3:
                    print("you dont have a bonus currently")

                elif opt44 == 4:
                    print("bye")
                    break
                break


            elif opt4 == 3:
                print("your number is ", my_number)
                break


            elif opt4 == 4:
                print("Tariff information")
                print("     1- berekete")
                print("     2- 11kobo")
                print("     3- gbam")
                print("     4- exit")

                opt444 = int(input("pls make a choice"))

                if opt444 == 1:
                    print("(enjoy 700 percent on all recharge and data.)")
                    print("     1- migrate now")
                    print("     2- exit")

                    opt4441 = int(input("pls make a decision"))
                    if opt4441 == 1:
                        print("you have migrated.")

                    elif opt4441 == 2:
                        print('bye')
                        break

                elif opt444 == 2:
                    print("     1- migrate now")
                    print("     2- exit")

                    opt4442 = int(input("pls make a decision"))
                    if opt4442 == 1:
                        print("you have migrated.")

                    elif opt4442 == 2:
                        print('bye')
                        break

                elif opt444 == 3:
                    print("(enjoy 700 percent on all recharge and data.)")
                    print("     1- migrate now")
                    print("     2- exit")

                    opt4443 = int(input("pls make a decision"))
                    if opt4443 == 1:
                        print("you have migrated.")

                    elif opt4443 == 2:
                        print('bye')
                        break

                
                elif opt444 == 3:
                    print("bye")
                    break



    #borow me credit and data
    elif opt == 5:
        print("borrow me credit and data ")
        print("     You are not eligible for this service.")
        break


    
    #value added service command.
    elif opt == 6:

        print("VAS")
        print("     1- Bussu language lerning (pay 100 naira to learn french and german.) ")
        print("     2- caller tunes (100 naira monthly for a caller tunes.)")
        print("     4- exit")

        opt7 = int(input("pls choose"))

        while opt7 != "exit":

            if opt7 == 1:
                print("Bussu language lerning (pay 100 naira to learn french and german.")
                print("     1- activate 100naira  weekly")
                print("     2- activate 50naira for every 3 days")
                print("     3- exit")

                opt77 = int(input("pls choose"))

                if opt77 == 1 or opt77 ==2:
                    print("you have succesfully subscribed")
                    break

                elif opt77 == 3:
                    break

                break


            elif opt7 == 2:
                print("caller tunes (100 naira monthly for a caller tunes.)")
                print("     1- activate 100naira  weekly")
                print("     2- activate 50naira for every 3 days")
                print("     3- exit")

                opt771 = int(input("pls choose"))

                if opt771 == 1 or opt771 ==2:
                    print("you have succesfully subscribed")
                    break

                elif opt771 == 3:
                    break
                
                break


            elif opt7 == 3:
                break


    #to exit from the command
    elif opt ==7:
        break

    #to check if the numbers are selected.
    elif opt != 1 or 2 or 3 or 4 or 5 or 6 or 7:
        break