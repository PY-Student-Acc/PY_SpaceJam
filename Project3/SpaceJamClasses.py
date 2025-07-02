from direct.task import Task
from direct.showbase.ShowBase import ShowBase
from panda3d.core import *


class Universe(ShowBase):
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, texPath: str, posVec: Vec3, scaleVec: float):
        self.modelNode = loader.loadModel(modelPath)
        self.modelNode.reparentTo(parentNode)
        self.modelNode.setPos(posVec)
        self.modelNode.setScale(scaleVec)

        self.modelNode.setName(nodeName)
        tex = loader.loadTexture(texPath)
        self.modelNode.setTexture(tex, 1)

class SpaceStation(ShowBase):
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, texPath: str, posVec: Vec3, scaleVec: float):
        self.modelNode = loader.loadModel(modelPath)
        self.modelNode.reparentTo(parentNode)
        self.modelNode.setPos(posVec)
        self.modelNode.setScale(scaleVec)

        self.modelNode.setName(nodeName)
        tex = loader.loadTexture(texPath)
        self.modelNode.setTexture(tex, 1)

class Spaceship(ShowBase):
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, texPath: str, posVec: Vec3, scaleVec: float, manager: Task, render: Camera):
        self.render = render
        self.taskMgr = manager
        self.modelNode = loader.loadModel(modelPath)
        self.modelNode.reparentTo(parentNode)
        self.modelNode.setPos(posVec)
        self.modelNode.setScale(scaleVec)

        self.modelNode.setName(nodeName)
        tex = loader.loadTexture(texPath)
        self.modelNode.setTexture(tex, 1)

    def Thrust(self, keyDown):
        if (keyDown):
            self.taskMgr.add(self.ApplyThrust, 'forward-thrust')
        else:
            self.taskMgr.remove('forward-thrust')

    def ApplyThrust(self, task):
        rate = 5
        trajectory = self.render.getRelativeVector(self.modelNode, Vec3.forward())
        trajectory.normalize()
        self.modelNode.setFluidPos(self.modelNode.getPos() + trajectory * rate)
        return task.cont

    def SetKeyBindings(self):
        # Movement for the spaceship
        self.accept('space', self.Thrust, [1]) # space moves us forward
        self.accept('space-up', self.Thrust, [0])

        self.accept('arrow_left', self.LeftTurn, [1]) # left arrow key turns us left
        self.accept('arrow_left-up', self.LeftTurn, [0])

        self.accept('arrow_right', self.RightTurn, [1]) # right arrow key turns us right
        self.accept('arrow_right-up', self.RightTurn, [0])

        self.accept('arrow_up', self.UpTurn, [1]) # up arrow key turns us up
        self.accept('arrow_up-up', self.UpTurn, [0]) 

        self.accept('arrow_down', self.DownTurn, [1]) # down arrow key turns us down
        self.accept('arrow_down-up', self.DownTurn, [0])

        self.accept('a', self.LeftRoll, [1]) # a key rolls us left
        self.accept('a-up', self.LeftRoll, [0])

        self.accept('d', self.RightRoll, [1]) # d key rolls us right
        self.accept('d-up', self.RightRoll, [0])

        self.accept('r', self.ResetRoll, [1]) 
        self.accept('r-up', self.ResetRoll, [0])

    def LeftTurn(self, keyDown):
        if (keyDown):
            self.taskMgr.add(self.ApplyLeftTurn, 'left-turn')
        else: 
            self.taskMgr.remove('left-turn')
    def ApplyLeftTurn(self, task):
        # turn half a degree every frame
        rate = 0.5
        self.modelNode.setH(self.modelNode.getH() + rate)
        return task.cont
    
    def RightTurn(self, keyDown):
        if (keyDown):
            self.taskMgr.add(self.ApplyRightTurn, 'right-turn')
        else: 
            self.taskMgr.remove('right-turn')
    def ApplyRightTurn(self, task):
        rate = 0.5
        self.modelNode.setH(self.modelNode.getH() - rate)
        return task.cont
    
    def UpTurn(self, keyDown):
        if (keyDown):
            self.taskMgr.add(self.ApplyUpTurn, 'up-turn')
        else: 
            self.taskMgr.remove('up-turn')
    def ApplyUpTurn(self, task):
        rate = 0.5
        self.modelNode.setP(self.modelNode.getP() + rate)
        return task.cont
    
    def DownTurn(self, keyDown):
        if (keyDown):
            self.taskMgr.add(self.ApplyDownTurn, 'down-turn')
        else: 
            self.taskMgr.remove('down-turn')
    def ApplyDownTurn(self, task):
        rate = 0.5
        self.modelNode.setP(self.modelNode.getP() - rate)
        return task.cont
    
    def LeftRoll(self, keyDown):
        if (keyDown):
            self.taskMgr.add(self.ApplyLeftRoll, 'left-roll')
        else: 
            self.taskMgr.remove('left-roll')
    def ApplyLeftRoll(self, task):
        rate = 0.5
        self.modelNode.setR(self.modelNode.getR() + rate)
        return task.cont
    
    def RightRoll(self, keyDown):
        if (keyDown):
            self.taskMgr.add(self.ApplyRightRoll, 'right-roll')
        else: 
            self.taskMgr.remove('right-roll')
    def ApplyRightRoll(self, task):
        rate = 0.5
        self.modelNode.setR(self.modelNode.getR() - rate)
        return task.cont
    
    def ResetRoll(self, keyDown):
        if (keyDown):
            self.taskMgr.add(self.ApplyResetRoll, 'reset-roll')
        else: 
            self.taskMgr.remove('reset-roll')
    def ApplyResetRoll(self, task):
        rate = 0.5
        self.modelNode.setR(0)
        return task.cont
    
    
    

class Planet(ShowBase):
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, texPath: str, posVec: Vec3, scaleVec: float):
        self.modelNode = loader.loadModel(modelPath)
        self.modelNode.reparentTo(parentNode)
        self.modelNode.setPos(posVec)
        self.modelNode.setScale(scaleVec)

        self.modelNode.setName(nodeName)
        tex = loader.loadTexture(texPath)
        self.modelNode.setTexture(tex, 1)
        
class Drone(ShowBase):
    droneCount = 0 # How many drones have been spawned
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, texPath: str, posVec: Vec3, scaleVec: float):
        self.modelNode = loader.loadModel(modelPath)
        self.modelNode.reparentTo(parentNode)
        self.modelNode.setPos(posVec)
        self.modelNode.setScale(scaleVec)

        self.modelNode.setName(nodeName)
        tex = loader.loadTexture(texPath)
        self.modelNode.setTexture(tex, 1)