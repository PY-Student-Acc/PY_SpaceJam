from direct.task import Task
from direct.showbase.ShowBase import ShowBase
from panda3d.core import *
from CollideObjectBase import *
from typing import Callable
from panda3d.core import CollisionHandlerEvent
from direct.interval.LerpInterval import LerpFunc
from direct.particles.ParticleEffect import ParticleEffect
import re


class Universe(InverseSphereCollideObject):
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, texPath: str, posVec: Vec3, scaleVec: float):
        super(Universe, self).__init__(loader, modelPath, parentNode, nodeName, Vec3(0, 0, 0), 0.9)
        #self.modelNode = loader.loadModel(modelPath)
        self.modelNode.reparentTo(parentNode)
        self.modelNode.setPos(posVec)
        self.modelNode.setScale(scaleVec)

        self.modelNode.setName(nodeName)
        tex = loader.loadTexture(texPath)
        self.modelNode.setTexture(tex, 1)

class SpaceStation(CapsuleCollidableObject):
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, texPath: str, posVec: Vec3, scaleVec: float):
        super(SpaceStation, self).__init__(loader, modelPath, parentNode, nodeName, 1, -1, 5, 1, -1, -5, 10)
        self.modelNode = loader.loadModel(modelPath)
        #self.modelNode.reparentTo(parentNode)
        self.modelNode.setPos(posVec)
        self.modelNode.setScale(scaleVec)

        self.modelNode.setName(nodeName)
        tex = loader.loadTexture(texPath)
        self.modelNode.setTexture(tex, 1)

class Spaceship(SphereCollideObject): # I couldn't figure out how to make this a seperate file without it breaking -_-
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, texPath: str, posVec: Vec3, scaleVec: float, traverser:str, manager: Task, render: Camera, accept: Callable[[str, Callable], None]):
        super(Spaceship, self).__init__(loader, modelPath, parentNode, nodeName, posVec, scaleVec)
        self.accept = accept
        self.render = render
        self.taskMgr = manager
        self.loader = loader
        #self.modelNode = loader.loadModel(modelPath)
        self.modelNode.reparentTo(parentNode)
        self.modelNode.setPos(posVec)
        self.modelNode.setScale(scaleVec)

        self.cntExplode = 0
        self.explodeIntervals = {}

        self.traverser = traverser  ##### fix this

        self.handler = CollisionHandlerEvent()


        self.handler.addInPattern('into')
        self.accept('into', self.HandleInto) ##### double check to make sure it turns yellow down the line

        self.modelNode.setName(nodeName)
        tex = loader.loadTexture(texPath)
        self.modelNode.setTexture(tex, 1)
        self.reloadTime = .25
        self.missileDistance = 4000     # distance until it explodes
        self.missileBay = 1     # how many missiles we can load at once

        self.taskMgr.add(self.CheckIntervals, 'checkMissiles', 34)

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

        self.accept('f', self.Fire) # f key fires missile

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
        self.modelNode.setR(0)
        return task.cont
    
    def Fire(self): 
        if self.missileBay:   # checks if there is a missile in the missile bay
            travRate = self.missileDistance   # so we know when to make the missile disappear
            aim = self.render.getRelativeVector(self.modelNode, Vec3.forward())   # the direction the spaceship is facing when missile is fired
            #   we convert to .egg files because it makes models consistent with their coordinate systems
            aim.normalize()     #normalize the vector to keep it consistent
            fireSolution = aim * travRate     # make a vector line using these variables
            inFront = aim * 150       # the 150 is just putting the missile some ditance in front of the ship
            travVec = fireSolution + self.modelNode.getPos()      # the line the missile travels when fired
            self.missileBay -= 1 # removes a missile
            tag = 'Missile' + str(Missile.missileCount) # each missile has a unique name, and the tag identifies it as a missile
            posVec = self.modelNode.getPos() + inFront # puts missile in front of ship nose
            currentMissile = Missile(self.loader, './Assets/Phaser/phaser.egg', self.render, tag, posVec, 4.0) # creates the missile
            Missile.Intervals[tag] = currentMissile.modelNode.posInterval(2.0, travVec, startPos = posVec, fluid = 1)
            Missile.Intervals[tag].start() # starts interval to make missile fire
                # until more is added, the missile should stop then stay in place
            self.traverser.addCollider(currentMissile.collisionNode, self.handler) ##### double check
        else:
            if not self.taskMgr.hasTaskNamed('reload'):
                print('Initializing reload...')
                    # call reload method with no delay
                self.taskMgr.doMethodLater(0, self.Reload, 'reload')
                return Task.cont

    def Reload(self, task):
        if task.time > self.reloadTime:
            self.missileBay += 1
            print("Reload complete.")
            return Task.done
        elif task.time < self.reloadTime:
            print("Reload proceeding...") 
            return Task.cont
        if self.missileBay > 1:   # Makes sure we don't have more than 1 if there's a glitch
            self.missileBay = 1

    def CheckIntervals (self, task):
        for i in Missile.Intervals:
            if not Missile.Intervals[i].isPlaying():
                Missile.cnodes[i].detachNode()
                Missile.fireModels[i].detachNode()
                del Missile.Intervals[i]
                del Missile.fireModels[i]
                del Missile.cNodes[i]
                del Missile.collisionSolids[i]
                return Task.cont
            
    def HandleInto(self, entry):
        fromNode = entry.getFromNodePath().getName()
        print("fromNode: " + fromNode)
        intoNode = entry.getIntoNodePath().getName()
        print("intoNode: " + intoNode)

        intoPosition = Vec3(entry.getSurfacePoint(self.render))

        tempVar = fromNode.split('_')
        print("tempVar: " + str(tempVar))
        shooter = tempVar[0]
        print("Shooter: " + str(shooter))
        tempVar = intoNode.split('_')
        print("tempVar1: " + str(tempVar))
        tempVar = intoNode.split('_')
        print("tempVar2: " + str(tempVar))
        victim = tempVar[0]
        print("Victim: " + str(victim))

        pattern = r'[0-9]'
        strippedString = re.sub(pattern, '', victim)

        if (strippedString == "Drone" or strippedString == "Planet" or strippedString == "Space Station"): ##### make sure this lines up with how my objects are named
            print(victim, ' hit at ', intoPosition)
            self.DestroyObject(victim, intoPosition) ##### make sure it calls right when I make ObjectDestroy() method

        print (shooter + ' is DONE.')
        Missile.Intervals[shooter].finish()

    def DestroyObject(self, hitID, hitPosition):
        nodeID = self.render.find(hitID)
        nodeID.detachNode()

        self.explodeNode.setPos(hitPosition)
        self.Explode()

    def Explode(self):
        self.cntExplode += 1
        tag = 'particles-' + str(self.cntExplode)

        self.explodeIntervals[tag] = LerpFunc(self.explodeLight, duration = 4.0)
        self.explodeIntervals[tag].start()

    def ExplodeLight(self, t):
        if t == 1.0 and self.explodeEffect:
            self.explodeEffect.disable()

        elif t == 0: 
            self.explodeEffect.start(self.explodeNode)

    def SetParticles(self):
        self.enableParticles()
        self.explodeEffect = ParticleEffect()
        self.explodeEffect.loadConfig() ##### add the asset path in
        self.explodeEffect.setScale(20)
        self.explodeNode = self.render.attachNewNode('ExplosionEffects') ##### double check

class Planet(SphereCollideObject):
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, texPath: str, posVec: Vec3, scaleVec: float):
        super(Planet, self).__init__(loader, modelPath, parentNode, nodeName, posVec, scaleVec)
        
        self.modelNode = loader.loadModel(modelPath)
        self.modelNode.reparentTo(parentNode)
        self.modelNode.setPos(posVec)
        self.modelNode.setScale(scaleVec)

        self.modelNode.setName(nodeName)
        tex = loader.loadTexture(texPath)
        self.modelNode.setTexture(tex, 1)
        
class Drone(SphereCollideObject):
    droneCount = 0 # How many drones have been spawned
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, texPath: str, posVec: Vec3, scaleVec: float):
        super(Drone, self).__init__(loader, modelPath, parentNode, nodeName, posVec, scaleVec)

        self.modelNode = loader.loadModel(modelPath)
        self.modelNode.reparentTo(parentNode)
        self.modelNode.setPos(posVec)
        self.modelNode.setScale(scaleVec)

        self.modelNode.setName(nodeName)
        tex = loader.loadTexture(texPath)
        self.modelNode.setTexture(tex, 1)

class Missile(SphereCollideObject):    # just a mark we're making the class
    fireModels = {}       #you can make them dictionaries or lists. Doesn't matter as long as it works
    cNodes = {}
    collisionSolids = {}
    Intervals = {}
    missileCount = 0
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, posVec: Vec3, scaleVec: float = 1.0):
        super(Missile, self).__init__(loader, modelPath, parentNode, nodeName, Vec3(0, 0, 0), 3.0)
        self.modelNode.setScale(scaleVec)
        self.modelNode.setPos(posVec)
        Missile.missileCount += 1     # increment for every time a missile is created

        Missile.fireModels[nodeName] = self.modelNode
        Missile.cNodes[nodeName] = self.collisionNode

        Missile.collisionSolids[nodeName] = self.collisionNode.node().getSolid(0)     # for debugging
        Missile.cNodes[nodeName].show()   # for debugging
        print("Fire torpedo #" + str(Missile.missileCount))   # debug line to show which missile is being printfired

    