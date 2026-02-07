import json
import random
import string
from pathlib import Path


class Bank:
    database = 'data.json'
    data = []

    try:
        if Path(database).exists():
            with open(database) as fs:
                data = json.loads(fs.read())
        else:
            print("No such File exists ")

    except Exception as err:
        print(f"An exception occured as {err}")
    
    @classmethod
    def __update(cls):
        with open(cls.database,'w') as fs:
            fs.write(json.dumps(Bank.data))
    
    @classmethod
    def __accountgenerate(cls):
        alpha = random.choices(string.ascii_letters,k=3)
        num = random.choices(string.digits,k=3)
        spchar=random.choices("!@#$%^&*",k=1)
        id= alpha + num + spchar
        random.shuffle(id)
        return"".join(id)




    def Createaccount(self):
        info = {
            "name": input("Tell your name :- "),
            "age" : int(input("Tell you age :- ")),
            "email": input("Tell you email :- "),
            "pin": int(input("Tell your pin :-")),
            "accountNo.":Bank.__accountgenerate(),
            "balance": 0
        }
        if info['age'] < 18 or len(str(info['pin']))!=4:
            print("Sorry you cannot create your account")
        else:
            print("Account has been created Successfully!!")

            for i in info:
                print(f"{i} : {info[i]}")
            print("please note down your account number")

            Bank.data.append(info)
            Bank.__update()
    
    def depositmoney(self):
        accnumber = input("Please enter your account number :- ")
        pin = int(input("Please tell your pin as well :- "))
        
        userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin]

        if not userdata:
            print("Sorry, no data found. Please check your account number or PIN.")
        else:
            amount = int(input("How much you want to deposit? :- "))
            if amount > 10000 or amount < 0:
                print("SORRY the amount is too much!! You can deposit below 10,000 and above 0.")
            else:
                userdata[0]['balance'] += amount
                Bank.__update()
                print("Amount deposited successfully!!")
    

    def withdrawmoney(self):
        accnumber = input("Please enter your account number :- ")
        pin = int(input("Please tell your pin as well :- "))
        
        userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin]

        if not userdata:
            print("Sorry, no data found. Please check your account number or PIN.")
        else:
            amount = int(input("How much you want to Withdraw ? :- "))
            if userdata[0]['balance'] < amount :
                print("SORRY you don't have that much money .")
            else:
                userdata[0]['balance'] -= amount
                Bank.__update()
                print("Amount withdrawn successfully!!")
    
    def showdetails(self):
        accnumber = input("Please enter your account number :- ")
        pin = int(input("Please tell your pin as well :- "))
        
        userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin]
        print("Your Information are : \n\n ")

        for i in userdata[0]:
            print(f"{i} : {userdata[0][i]}")
    
    def updatedetails(self):
        accnumber = input("Please enter your account number :- ")
        pin = int(input("Please tell your pin as well :- "))
        
        userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin]

        if userdata ==False:
            print("NO such data found. ")
        else:
            print("You cannot the age, account number, balance. ")
            print("Fill the detials for change , and leave empty if no change. ")

            newdata = {
            "name": input("Tell your name or press enter to skip :- "),
            "email": input("Tell you email or press enter to skip :- "),
            "pin": int(input("Tell your pin or press enter  to skip :-")),

            }
            if newdata["name"]== "":
                newdata["name"] = userdata[0]['name']

            if newdata["email"]== "":
                newdata["email"] = userdata[0]['email']

            if newdata["pin"]== "":
                newdata["pin"] = userdata[0]['pin']

            newdata['age'] = userdata[0]['age']

            newdata['accountNo.'] = userdata[0]['accountNo.']
            newdata['balance'] = userdata[0]['balance']

            if type(newdata['pin']) == str:
                newdata['pin'] = int(newdata['pin'])


            for i in newdata:
                if newdata[i] == userdata[0][i]:
                    continue
                else:
                    userdata[0][i]=newdata[i]

            Bank.__update()
            print("Details Updated Successfully !!")
    
    def Delete(self):
        accnumber = input("Please enter your account number :- ")
        pin = int(input("Please tell your pin as well :- "))
        
        userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin]

        if userdata ==False:
            print("NO such data exists. ")
        else:
            print("Press y if you actually want to delete the account or press n. ")

            if check =='n' or check =="N":
                print("Bypassed")
            else:
                index = Bank.data.index(userdata[0])
                Bank.data.pop(index)

                print("Account Deleted Successfully !!")

                Bank.__update

user = Bank()
print("Press 1 for creating an account:")
print("Press 2 for Depositing the money in the Bank:")
print("Press 3 for Withdrwaing the Money:")
print("Press 4 for Details:")
print("Press 5 for Updating the Details:")
print("Press 6 for Deleting your Account:")

check =int(input("Tell your Response :- "))

if check == 1:
    user.Createaccount()

if check == 2:
    user.depositmoney()
if check ==3:
    user.withdrawmoney()
if check ==4:
    user.showdetails()
if check ==5:
    user.updatedetails()

if check ==6:
    user.Delete()
