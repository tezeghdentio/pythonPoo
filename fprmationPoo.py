class client:
    numClient=0
    

    
    def __init__(self,civilite,nom,prenom,age,email) -> None:
        self.civilite=civilite
        self.nom=nom
        self.prenom=prenom
        self.age=age
        self.email=email
        client.numClient+=1
    def getFullName(self):
        return f"{self.prenom} {self.nom}"
    def getFullInfo(self):
        return f"{self.civilite} {self.getFullName()} {self.age} {self.email}"
    def getAge(self):
        return f"{self.age}"
    def getemail(self):
        return f"{self.email}"
    def deleteUser(self):
        client.numClient-=1
        return f"User {self.getFullName} deleted"
print(client.numClient)
c1=client("Mr","TEZEHDENTI","Oussama",39,"tezeghdenti@gmail.com")
c2=client("Mr","TOUNSI","Salah",40,"Tounsi@gmail.com")
print(client.numClient)
print(c2.deleteUser())
print(client.numClient)
#print(c1.__class__)
#print(c1.nom+" "+c1.prenom+" "+str(c1.age)+" "+c1.email)
print(c1.getFullName())  
print(c1.getFullInfo())     
