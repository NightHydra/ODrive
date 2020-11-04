import math
class KEquations:
    def findC1(self, L1, L3, theta3, x0, theta0):
        part1 = 2*L1*L3*math.cos(theta3)
        part2 = (2*x0*L1)/(math.cos(theta0))

        return part1 - part2
    
    def findC2(self, H, L1, L3, theta3, y0):
        part1 = 2*H*L1
        part2 = 2*L1*L3*math.sin(theta3)
        part3 = 2*y0*L1

        return part1 + part2 - part3

    def findC3(self, x0, theta0, y0, H, L1, L3, L2, theta3):
        part1 = (x0**2)/math.cos(theta0)**2
        part2 = y0**2
        part3 = H**2
        part4 = L1**2
        part5 = L3**2
        part6 = L2**2
        part7 = (2*x0*L3*math.cos(theta3))/(math.cos(theta0))
        part8 = 2*y0*H
        part9 = 2*L3*math.sin(theta3)*(H-y0)

        return part1+part2+part3+part4+part5-part6-part7-part8+part9

    def theta1(self, C2, C3, C1):
        return 
    


    

    
        
    

        
