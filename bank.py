class Bank:
    def __init__(self,acno):
        self.acno=acno
        self.bal={"8341996346":100000,"7207295142":6000,"6300369651":50000}
        self.ac={"8341996346":"Naveen Reddy Kothakapu","7207295142":"kalyan Junju","6300369651":"Samara kishore Deshi"}
        if self.acno not in self.ac.keys():
            print("Invalid account number")
        else:
            print("{} Welcome back..".format(self.ac[self.acno]))
    def withdraw(self,amount):
        if self.bal[self.acno]>=amount:
            self.bal[self.acno] -= amount
        else:
            print("Insuficient balance")
    def credit(self,amount):
        self.bal[self.acno] += amount
    def transaction(self,to_user_ac,amount):
        if to_user_ac not in self.ac.keys():
            print("User not found")
        else:
            if self.bal[self.acno]>=amount:
                print("{}>>>>>>>{}".format(self.ac[self.acno],self.ac[to_user_ac]))
                self.bal[self.acno] -= amount
                self.bal[to_user_ac] += amount
            else:
                print("Insufficient Balance")

    def balances(self):
        print("Balance: {}".format(self.bal[self.acno]))

obj1=Bank("8341996346")
obj1.balances()
obj1.transaction("7207295142",1100)
obj1.balances()
obj2=Bank("7207295142")
obj2.balances()
obj2.transaction("8341996346",5000)
obj2.balances()
obj2.transaction("6300369651",1100)
obj2.balances()