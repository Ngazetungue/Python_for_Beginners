
print('''                                    
                      NGAZETUNGUE MUHEUE
                        P.O BOX 1111111                      
                       +264 81 000 0047                      
                           WINDHOEK                          
                            NAMIBIA                           
        ----------------------------------------------------------''')
#I WANT TO DESIGN THE GUI OF THE FOLLOWING CODE

log=("Y" and "N")# choice between new member and old member
log=input("ARE YOU A NEW MEMBER,ENTER YOUR CHOICE BY PRESSING Y KEY OR N KEY: ")#Enter your choice

while log!=("Y") and log!=("N"):
    print("YOU ENTER AN INVALID OPTION,TRY AGAIN")
    log=input("ARE YOU A NEW MEMBER,ENTER YOUR CHOICE BY PRESSING Y KEY OR N KEY: ")
if log ==("Y"):
    print('''                  WELCOME TO OUR WORLD OF IT              
             ===================================================
                     PERSONAL DETAILS                     
             ===================================================''')
    name=input("ENTER YOUR FIRST NAME:")#name of new member
    Last_name=input("ENTER YOUR LAST NAME:")#Last name
    Sex=input("ENTER GENDER:")#Sex
    Occupation=input("ENTER YOUR OCCUPATION:")#Occupation
    Resident=input("ENTER YOUR RESIDENTIAL ADDRESS:")#where do u stay
    Nationality=input("ENTER COUNTRY OF BIRTH:")#Country of birth
    print("YOU REGISTER",name," YOUR DEFAULT PASSWORD IS:muheue")#Providing a password and storing a new member into the system.
    
    print('''-----------------------------------------------------------------------
                       VERIFY YOUR DETAILS                                 
    -----------------------------------------------------------------------''')#Verifying the new user details
    
    print('''    
    LAST NAME                 :",Last_name)
    GENDER                    :",Sex)
    OCCUPATION                :",Occupation)
    RESIDENTIAL ADDRESS       :",Resident)
    COUNTRY OF BIRTH          :",Nationality)
    -----------------------------------------------------------------------")
    -----------------------------------------------------------------------''')
    
    print("ENTER A PASSWORD THAT WAS PROVIDED TO YOU\n")
    
elif log == ("N"):#name of old member
    print("            LOG INTO THE SYSTEM          ")#prompting old member to login
    name=input("ENTER YOUR NAME:")
    while name!="zizou" and name!="mike" and name!="jessica" :# if name is not zizou the system 
        print("NAME ENTERED NOT RECOGNIZE BY OUR SYSYEM, PLEASE TRY AGAIN:")
        name=input("ENTER YOUR NAME:")#The system will keep asking a user to enter a correct name,if correct name not entered.
    if name=="zizou" and name=="mike" and name=="jessica":#This is a correct name the user should enter into the system
        print("THANK YOU FOR VISITING US AGAIN",name.upper())#Welcoming the user 
        print("ENTER YOUR PASSWORD\n") 
                        
count = 1
password = "muheue"
if name=="zizou":
    password="zizou"
elif name=="mike":
    password="mike"
elif name=="jessica":
    password="jessica"
enter_password = input("ENTER YOUR PASSWORD? ")
while count < 3 and enter_password.lower() != password:    # .lower allows things like muheue to still match, and password should be only entered 3 times.
    print("wrong password!")
    enter_password = input("ENTER YOUR PASSWORD? ")#re-ente the password if,wrong password entered at first attempt.
    count = count + 1#everytime the user enter incorrect password the system will keep count
if enter_password.lower() != password:
    print("Access Denied!") # this message isn't printed in the third chance, so we print it now
    print("You ran out of chances:",name.upper())#Telling the user that s/he ran out of time. the system will quit after third attemp.
else:
    print("                                                   ")
    print(''' |=================================================|)
    | WELCOME TO MUHEUE ELECTRONIC TECHNOLOGY HUB     |
    |=================================================|
    |            SERVICES WE PROVIDE AT OUR HUB       |
    |===============|===============|=================|
    |=================================================|
    |   DEPARTMENTS NAME                NUMBER        |
    |=================================================|
    |   COMPUTER MAINTENANCE         |    1           |
    |=================================================|
    |   GRAPHIC DESIGN               |    2           |
    |=================================================|
    |=================================================|''')

    count = 0
    number = int(input("ENTER NUMBER TO SEE PRODUCTS: "))
    while number < 1 or number > 2:    
        print("wrong number!")
        number= int(input("ENTER NUMBER TO SEE PRODUCTS  "))#re-enter the number if,wrong number entered at first attempt.
        count+=1
    if number == 1:
            print("|=============================================================================|")
            print("|                WELCOME TO MUHEUE ELECTRONIC TECHNOLOGY HUB                  |")
            print("|=============================================================================|")
            print("|                    SERVICES WE PROVIDE AT OUR HUB                           |")
            print("|===============|===============|=============================================|")
            print("|=============================================================================|")
            print("|                        COMPUTER MAINTENANCE DEPARTMENT                      |")
            print("|=============================================================================|")
            print("|       SERVICES                     PRICES              DESCRIPTION          |")
            print("|=============================================================================|")
            print("|   SOFTWARE INSTALLATION    |    N$ 150             |installing new softwares|")
            print("|=============================================================================|")
            print("|   VIRUS REMOVAL            |    N$ 100             |Computer security       |")
            print("|=============================================================================|")
            print("|   HARDWARE TROUBLESHOOTING |    N$ 200             |                        |")
            print("|=============================================================================|")
    
    elif number == 2:

            print("==========================================================================|")
            print('''|               WELCOME TO MUHEUE ELECTRONIC TECHNOLOGY HUB             |")
                 ("|=========================================================================|")
                 ("|                    SERVICES WE PROVIDE AT OUR HUB                       |")
                 ("|===============|===============|=========================================|")
                 ("|=========================================================================|")
                 ("|                         GRAPHIC DESIGN DEPARTMENT                       |")
                 ("|=========================================================================|")
                 ("|     SERVICES                     PRICES              DESCRIPTION        |")
                 ("|=========================================================================|")
                 ("|   LOGO                     |    N$ 90-00       |Designing logo          |")
                 ("|=========================================================================|")
                 ("|   PRINTING                 |    N$ 10-00       |Printing services       |")
                 ("|=========================================================================|")
                 ("|   WEDDING CARD             |    N$ 100-00      |Designing wedding cards |")
                 ("|=======================================================================|''')
     
    print("\n\n")
    
print('''WRITTEN BY  :NGAZETUNGUE MUHEUE
UNIVERSITY  :UNIVERSITY OF NAMIBIA    
COURSE      :COMPUTER SCIENCE (STUDENT)
City        :Windhoek
CELL        :+264 (0) 81 0000000       
YEAR        :2014''')
