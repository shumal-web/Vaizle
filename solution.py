import datetime


def solution():
    isValid = False
    while not isValid:
        date_1 = input("Type first Date dd-mm-yyyy: ")
        value_1 = input("Enter first value: ")
        date_2 = input("Type second Date dd-mm-yyyy: ")
        value_2 = input("Enter second value: ")
        try:  # strptime throw an exception if input date doesn't match the pattern
            d1 = datetime.datetime.strptime(date_1, "%d-%m-%Y")
            d2 = datetime.datetime.strptime(date_2, "%d-%m-%Y")
            isValid = True

        except:
            print("Try again in dd-mm-yyyy pattern\n")
        if (isValid == True):
            if (d1.year == d2.year and d1.month == d2.month):
                # checking for value which is greater then 0 and less than 1000000
                # checking for valid years
                if (int(value_1) < 1000000 and int(value_2) < 1000000 and int(value_1) > 0 and int(value_2) > 0):
                    if (d1.year > 1970 and d1.year < 2100 and d2.year > 1970 and d2.year < 2100):
                        if (d2.day != d1.day):  # checking for same days
                            k = int(d2.day) - int(d1.day)
                        else:
                            k = 1
                        v = int(value_2) - int(value_1)

                        avrg = v / k
                        val = int(value_1)
                        dec_final = {}  # final empty dict

                        for day in range(int(d1.day), int(d2.day) + 1):

                            if (day != d1.day):  # checking if days are same
                                val = val + avrg
                            vall1 = str(day) + "-" + str(d1.month) + "-" + str(d1.year)

                            dec_final[vall1] = int(val)
                        print(dec_final)
                    else:
                        print("enter valid years 1970 < year < 2020")
                        solution()


                else:
                    print("Enter valid values(0 > value > 1000000)")
                    solution()


            else:
                print("year and month must be same")
                solution()

        


solution()
