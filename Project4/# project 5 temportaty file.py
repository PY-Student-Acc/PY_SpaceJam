# project 5 temportaty file
# this is a temporary file to hold the code we go over in class for project 5 
# so I can implement it when I finish project 4

# missiles firing out of the spaceship
# they will travel for a bit then disappear
# the missiles won't have collision yet
# that'll be project 6

# this lab has a lot to do with intervals
# this is how we'll make the missiles
# an interval has something keep going without player input

# each missile willbe fired and reach the end of the path

# Missile class

#class Missile(SphereCollideObject):    # just a mark we're making the class

# add 3 variables to spaceship class

# self.reloadTime = .25
# self.missileDistance = 4000 # distance until it explodes
# self.missileBay = 1 # how many missiles we can load at once

# add a keybind in SetKeyBindings()
    #self.accept('f', self.Fire) # accept for firing

# def Fire(self): 
    # if self.missileBay:   # checks if there is a missile in the missile bay

        # travRate = self.missileDistance   # so we know when to make the missile disappear

     # aim = self.render.getRelativeVector(self.modelNode, Vec3.forward())   # the direction the spaceship is facing when missile is fired

     #   we convert to .egg files because it makes models consistent with their coordinate systems

      # aim.normalize     #normalize the vector to keep it consistent

     # fireSolution = aim * travRate     # make a vector line using these variables

     # inFront = aim * 150       # the 150 is just putting the missile some ditance in front of the ship

     # travVec = fireSolution + self.modelNode.getPos()      # the line the missile travels when fired

     # self.missileBay -= 1      # removes a missile

      # tag = 'Missile' + str(Missile.missileCount)       # each missile has a unique name, and the tag identifies it as a missile
    
     # posVec = self.modelNode.getPos() + inFront        # puts missile in front of ship nose

      # currentMissile = Missile(self.loader, './Assets/Phaser/phaser.egg', self.render, tag, posVec, 4.0)        # creates the missile

      # Missile.Intervals[tag] = currentMissile.modelNode.posInterval(2.0, travVec, startPos = posVec, fluid = 1)

     # Missile.Intervals[tag].start() # starts interval to make missile fire
            # until more is added, the missile should stop then stay in place
    # else:
        # if not self.taskMger.hasTaskNamed('reload'):
            # print('Initializing reload...')
                # call reload method with no delay
            # self.taskMgr.doMethodLater(0, self.Reload, 'reload')
            # return Task.cont

# def Reload(self, task):
    # if task.time > self.reloadTime:
        # self.missileBay += 1
        # print("Reload complete.")
        # return Task.done
    # elif task.time < self.reloadTime:
        # print("Reload proceeding...") 
        # return Task.cont
    # if self.missileBay > 1:   # Makes sure we don't have more than 1 if there's a glitch
        # self.missileBay = 1
        


# back to missile class

# class Missile(SphereCollideObject):

    # fireModels = {}       #you can make them dictionaries or lists. Doesn't matter as long as it works
    # cNodes = {}
    # collisionSolids = {}
    # Intervals = {}
    # missileCount = 0
    
    # def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, posVec: Vec3, scaleVec: float = 1.0):
        # super(Missile, self).__init__(loader, modelPath, parentNode, nodeName, Vec3(0, 0, 0), 3.0)
        # self.modelNode.setScale(scaleVec)
        # self.modelNode.setPos(posVec)
        # Missile.missileCount += 1     # increment for every time a missile is created

        # Missile.fireModels[nodeName] = self.modelNode
        # Missile.cNodes[nodeName] = self.collisionNode

        # missile.collisionSolids[nodeName] = self.collisionNode.node().getSolid(0)     # for debugging
        # missile.cNodes[nodeName].show()   # for debugging
        # print("Fire torpedo #" + str(Missile.missileCount))   # debug line to show which missile is being printfired

# addition to player class constructor
    # self.taskMger.add(self.CheckIntervals, 'checkMissile', 34)

# def CheckIntervals (self, task):
    # for i in MissileIntervals:
        # if not Missile.Intervals[i].isPlaying():
            # Missile.cnodes[i].detachNode()
            # Missile.fireModels[i].detachNode()
            # del Missile.Intervals[i]
            # del Missile.fireModels[i]
            # del Missile.cNodes[i]
            # del Missile.collisionSolids[i]
            # return Task.cont

# def EnableHUD(self):
    # in the file this is in, import the following: from direct.gui.OnscreenImage importOnscreenImage

    # self.Hud = OnScreenImage(image = "./Assets/Hud/Reticle3b.png", pos = vec3(0, 0, 0), scale = 0.1)
    # self.Hud.setTransparencyAttrib.MAlpha


# TO DO:

    # add misile firing to spacejam
    # make sure missiles disappear after a certain amount of time down their path
    # make sure reload works as well
    # make sure hud is also there
    # upload to github and submit