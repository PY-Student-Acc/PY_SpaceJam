import DefensePaths as defensePaths
import SpaceJamClasses as spaceJamClasses
from math import pi, sin, cos
from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor
from direct.interval.IntervalGlobal import Sequence
from panda3d.core import Point3
from panda3d.core import *

class MyApp(ShowBase):


    def __init__(self):
        ShowBase.__init__(self)
        
        self.SetupScene()
        
    def SetupScene(self):
        
        self.Universe = spaceJamClasses.Universe(self.loader, './Assets/Universe/Universe.x', self.render, 'Universe', './Assets/Universe/Universe.jpg', (0, 0, 0), 15000)
        
        self.Planet1 = spaceJamClasses.Planet(self.loader, "./Assets/Planets/protoPlanet.x", self.render, "Planet1", "./Assets/Planets/Grass_Block_JE2.png", (-250, 1200, 54), 190)
        self.Planet2 = spaceJamClasses.Planet(self.loader, "./Assets/Planets/protoPlanet.x", self.render, "Planet2", "./Assets/Planets/KSA_Popstar.jpg", (250, 1000, 67), 220)
        self.Planet3 = spaceJamClasses.Planet(self.loader, "./Assets/Planets/protoPlanet.x", self.render, "Planet3", "./Assets/Planets/Lego_ego.jpg", (150, -1200, 67), 340)
        self.Planet4 = spaceJamClasses.Planet(self.loader, "./Assets/Planets/protoPlanet.x", self.render, "Planet4", "./Assets/Planets/Meap_Planet.jpg", (-150, 1500, 67), 109)
        self.Planet5 = spaceJamClasses.Planet(self.loader, "./Assets/Planets/protoPlanet.x", self.render, "Planet5", "./Assets/Planets/small_cube__24639.jpg", (150, 4200, 69), 490)
        self.Planet6 = spaceJamClasses.Planet(self.loader, "./Assets/Planets/protoPlanet.x", self.render, "Planet6", "./Assets/Planets/SSBU_spirit_Moon.png", (10, 330, 67), 124)
        self.SpaceStation1 = spaceJamClasses.SpaceStation(self.loader, "./Assets/SpaceStation1B/spaceStation.x", self.render, "Space Station", "./Assets/SpaceStation1B/SpaceStation1_Dif2.png", (25, 25, 25), 5)
        self.Hero = spaceJamClasses.Spaceship(self.loader, "./Assets/Spaceships/PercyJacksonIsBetter/PercyJacksonIsBetter.x", self.render, "Hero", "./Assets/Spaceships/PercyJacksonIsBetter/spacejet_C.png", (0, 0, 0), 1, self.taskMgr, self.render)

        self.SetCamera()
        

        fullCycle = 60

        for j in range(fullCycle):
            spaceJamClasses.Drone.droneCount += 1
            nickName = "Drone" + str(spaceJamClasses.Drone.droneCount)

            self.DrawCloudDefense(self.Planet1, nickName)
            self.DrawBaseballSeams(self.SpaceStation1, nickName, j, fullCycle, 2)
            #self.DrawCircleX(self.Planet2, nickName, fullCycle)

    def SetCamera(self): # makes the camera the player
        self.disableMouse()
        self.Hero.SetKeyBindings()
       
        self.camera.reparentTo(self.Hero.modelNode)
        self.camera.setFluidPos(0, 1, 0)

    def DrawBaseballSeams(self, centralObject, droneName, step, numSeams, radius = 1):
        unitVec = defensePaths.BaseballSeams(step, numSeams, B = 0.4)
        unitVec.normalize()
        position = unitVec * radius * 250 + centralObject.modelNode.getPos()
        spaceJamClasses.Drone(self.loader, "./Assets/DroneDefender/DroneDefender.obj", self.render, droneName, "./Assets/DroneDefender/octotoad1_auv.png", position, 5)

    def DrawCloudDefense(self, centralObject, droneName):
        unitVec = defensePaths.Cloud()
        unitVec.normalize()
        position = unitVec * 500 + centralObject.modelNode.getPos()
        spaceJamClasses.Drone(self.loader, "./Assets/DroneDefender/DroneDefender.obj", self.render, droneName, "./Assets/DroneDefender/octotoad1_auv.png", position, 10)

    def DrawCircleX(self, centralObject, droneName, step):
        unitVec = defensePaths.CircleX(step, B = 0.4)
        unitVec.normalize()
        position = unitVec * 750 + centralObject.modelNode.getPos()
        spaceJamClasses.Drone(self.loader, "./Assets/DroneDefender/DroneDefender.obj", self.render, droneName, "./Assets/DroneDefender/octotoad1_auv.png", position, 15)

#    def DrawCircleY(self, centralObject, droneName):
#        unitVec = defensePaths.CircleY()
#        unitVec.normalize()
#        position = unitVec * 1000 + centralObject.modelNode.getPos()
#        spaceJamClasses.Drone(self.loader, "./Assets/DroneDefender/DroneDefender.obj", self.render, droneName, "./Assets/DroneDefender/octotoad1_auv.png", position, 20)

#    def DrawCircleZ(self, centralObject, droneName):
#        unitVec = defensePaths.CircleZ()
#        unitVec.normalize()
#        position = unitVec * 500 + centralObject.modelNode.getPos()
#        spaceJamClasses.Drone(self.loader, "./Assets/DroneDefender/DroneDefender.obj", self.render, droneName, "./Assets/DroneDefender/octotoad1_auv.png", position, 25)
app = MyApp()
app.run()