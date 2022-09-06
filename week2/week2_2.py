from math import pi
class Spherical :
    
    def __init__(self,r):
        self.radius = r

    def changeR(self,Radius):
        self.radius = Radius

    def findVolume(self):
        return pi * self.radius * self.radius * self.radius * (4/3)     #เวลาคำนวณ เอา pi ขึ้นก่อน

    def findArea(self):
        return pi * self.radius * self.radius * 4

    def __str__(self):
        ans = "Radius =" + str(int(self.radius))
        ans = ans + " Volumn = " + str(self.findVolume())
        ans = ans + " Area = " + str(self.findArea())
        return ans


r1, r2 = input("Enter R : ").split()
R1 = Spherical(int(r1))
print(type(R1))
print(dir(R1))
print(R1)
R1.changeR(int(r2))
print(R1)
