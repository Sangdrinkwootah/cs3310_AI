from re import A

class BMR:
    def getName():
        f = open("User Info\\name.txt", "r")
        name = f.read()
        f.close()
        return name

    def getAge(self):
        f = open("User Info\\age.txt", "r")
        self.age = f.read()
        f.close()
        return self.age

    def getWeight(self):
        f = open("User Info\\weight.txt", "r")
        self.weight = f.read()
        f.close()
        return self.weight

    def getHeight(self):
        f = open("User Info\\height.txt", "r")
        self.height = f.read()
        f.close()
        return self.height

    def getGender(self):
        f = open("User Info\\gender.txt", "r")
        self.gender = f.read()
        f.close()
        return self.gender

    def calBMR(self, gender, weight, height, age):
        if self.gender == "male":
            bmr = 88.376 + 13*self.weight + 4.799*self.height - 5.677*self.age
        elif self.gender == "female": 
            bmr = 447.593 + 9.247*self.weight + 3.098*self.height - 4.330*self.age

        bmr = round(bmr)
        return bmr
