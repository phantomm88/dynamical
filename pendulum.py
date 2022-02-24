# N-pendulum source file
import numpy as np

class Joint:
    def __init__(self, x, y, fix=False):
        self.x = x
        self.y = y
        self.forces = []
        self.fixValue = fix
        self.beamCodes = []
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def getForces(self):
        return self.forces
    def getFixValue(self):
        return self.fixValue
    def setFixValue(self, newFix):
        self.fixValue = newFix
    def setX(self, newX):
        self.x = newX
    def setY(self, newY):
        self.y = newY
    def getBeamCodes(self):
        return self.beamCodes
    def addBeamCode(self, code):
        self.beamCodes.append(code)
    def addForce(self, newForce):
        self.forces.append(newForce)
    def removeForce(self, index=None):
        if index is None:
            self.force.pop()
        else:
            self.force.pop(index)
    def dist(self, joint2):
        return np.sqrt((joint2.getX() - self.x)**2 + (joint2.getY() - self.y)**2)

class Beam:
    # joint1 and joint2 are linked, with joint2 being further away from base. constants are made of K and rest length, in order
    def __init__(self, k, restLength):
        self.k, self.restLength = k, restLength
    def link(self, joint1, joint2):
        joint1.addBeamCode((id(self), self.k, self.restLength))
        joint2.addBeamCode((id(self), self.k, self.restLength))
        joint2.addForce((-self.k * (joint1.dist(joint2) - self.restLength), id(self)))
    def getJoint1(self):
        return self.joint1
    def setJoint1(self, newJoint1):
        self.joint1 = newJoint1
    def getJoint2(self):
        return self.joint2
    def setJoint2(self, newJoint2):
        self.joint2 = newJoint2
    def getK(self):
        return self.k
    def setK(self, newK):
        self.k = newK

a = Joint(3, 4)
b = Joint(5, 10)
c = Beam(3, 10)
c.link(a, b)
