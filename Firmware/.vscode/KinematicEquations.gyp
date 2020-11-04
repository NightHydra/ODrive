import math
class KEquations:
    def findC1(self, L1, L3, theta3, x0, theta0):
        part1 = 2*L1*L3*math.cos(theta3)
        part2 = (2*x0*L1)/(math.cos(theta0))

        return part1 - part2
    
    def findC2(self, H, L1, L3, theta3, y0):
        part1 = 2*H*L1
        
    

        
