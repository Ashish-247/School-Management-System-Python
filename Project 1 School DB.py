# Project 1 - School Database Management System

studentDict = dict.fromkeys(['Student Name','Student Father Name','Student Mother Name','Phone No.','Address','Card No.','Class'])

studentList = []

while True:
    print("""
    Welcome to WsCube Tech - E School

    1. Student's Admission
    2. Student's Fee
    3. Principal Access
    4. Exit
    """)

    noOfCommand = int(input("Press number to select the command : "))
    if noOfCommand == 1:
        print("Welcome to Student Admission")

        studentName = input("Student Name: ")
        studentDict['Student Name'] = studentName
        studentFatherName = input("Student Father Name: ")
        studentDict['Student Father Name'] = studentFatherName
        studentMotherName = input("Student Mother Name: ")
        studentDict['Student Mother Name'] = studentMotherName
        phoneNo = int(input("Phone No.: "))
        studentDict['Phone No.'] = phoneNo
        address = input("Address : ")
        studentDict['Address'] = address
        cardNo = int(input("Enter Card No.: "))
        studentDict['Card No.'] = cardNo
        Class = input("Class: ")
        studentDict['Class'] = Class

        copyOfDict = studentDict.copy()
        studentList.append(copyOfDict)
        listLength = (len(studentList))

        for i in studentList[:-1]:
            if i['Card No.'] == cardNo:
                studentList.pop()
        postListLength = (len(studentList))

        if listLength == postListLength:
            print("Admission successful")
        else:
            print("Student Already Exist")

        for i in studentList:
            print(i)

    if noOfCommand == 2:

        print("** Student Fee **")
        studentName = input("Student Name : ")
        cardNo = int(input("Enter Card No. : "))
        fee = int(input("Enter Fee Amount :"))

        boolVal = False
        for i in studentList:
            if studentName == i['Student Name'] and cardNo == i['Card No.']:
                print("Successfully Fee Submitted")
                i['fee'] = fee
                boolVal = True

        if boolVal == False:
            print("Card No. Did  not match")

        for i in studentList:
            print(i)

    if noOfCommand == 3:
        print("** Principal Access **")
        principalCode = "mypassword123"
        password = input("Enter credentials to get Principal's Access : ")
        #boolPass = False
        while True:
            if password == principalCode:
                cardNo = int(input("Enter card number of the student : "))
                for i in studentList:
                    if cardNo == 0:
                        pass
                    elif cardNo == i['Card No.']:
                        for element in i:
                            print(element, " : ", i[element])
                        print("Press 0 to go to Main Menu OR")
                        break

                else:
                    if cardNo != 0:
                        print("Wrong Id")
                if cardNo == 0:
                    break
            else:
                print("Wrong Password")
                password = input("Enter credentials to get Principal's Access : ")

    if noOfCommand == 4:
        break
