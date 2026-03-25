#THIS IS SYSTEM FOR THE TABLE BOOKING MANAGEMENT 
"""
def displayTable(tablesvalue):
    i=0
    for x in table:
        i+=1
        print (str(i)+". " +str(x))
"""
#---------Function----------------------------------

def DisplayTable(item):
    for (i, item) in enumerate (table, start =1):
        print (i, item)

def DisplayNama(item):
    for (i, item) in enumerate (name, start =1):
        print (i, item)

#-----------Main Code-------------------------------
name = []
table = ["Table 1", "Table 2", "Table 3", "Table 4"]



while True: 
    print ("======================Table Booking==========================")
    choice = int(input("Enter your choice:\n1. Booking table\n2. View Availble Table\n3. View Customer\n4. Exit\n"))
    if choice == 1: 
        nama = input("Enter Your name for Reservation: ")
        contact = input ("Enter your number phone: ")
        email= input ("Enter Your Email Address: ")
        tableinfo = input("Enter table number: ")

        user_list= {
            "Name" : nama,
            "Contact" : contact,
            "Email" : email,
            "Table" : tableinfo
        }

        name.append(user_list)
        table.remove(tableinfo)
        DisplayNama(name)
        continue

    elif choice ==2:
        print("==============VIEW AVAILABLE TABLE======================")
        DisplayTable(table)
        
    elif choice == 3:
        print ("=============VIEW CUSTOMER INFORMATION=================")
        for users in name:
            print (f"Name: {users['Name']}| Email: {users['Email']}| Table: {users['Table']}")
        
    else:
        print ("Thank You!")
        break





    







