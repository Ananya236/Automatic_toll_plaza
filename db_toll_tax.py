from rfid_prog import *
from xl_write_prog import *

r_list=[]

def db():



    way = int(input("Press\n1) For One Way\n2) For Two Way"))
    v_type = int(input("Press\n1) For Trucks/Buses\n2)Heavy Vehicles\n3)Cars"))


    if way==1:
        print("ONE WAY..!!!")
        name = input("Enter your Name")
        v_no = input("Enter Vehicle No")
        if v_type==1:
            amt=80
            print("Amt Payable:=",amt)

        elif v_type==2:
            amt=100
            print("Amt Payable:=",amt)

        elif v_type==3:
            amt=60
            print("Amt Payable:=",amt)
        rfid_no=0


    elif way==2:
        print("TWO WAY..!!!")
        ch = int(input("Press 1)First Round\n2)Way Back"))
        if ch == 1:
            name = input("Enter your Name")
            v_no = input("Enter Vehicle No")
            if v_type==1:
                amt=80
                print("Amt Payable:=",amt)

            elif v_type==2:
                amt=100
                print("Amt Payable:=",amt)

            elif v_type==3:
                amt=60
                print("Amt Payable:=",amt)
            rfid_no=rfid()
            print("Card says: {}".format(rfid_no))
            return name,v_no,amt,rfid_no

        elif ch == 2:
            rfid_no = rfid()
            r_list=xl_read()
            print("R_List:",r_list)
            if rfid_no in r_list:
                print("Gotcha..!!")
                for i in range(len(r_list)):
                    if rfid_no==r_list[i]:
                        print("Welcome Back\n Kindly Submit Your Tag.!!")
            else:
                print("NOT AUTHORIZED..!!!")


