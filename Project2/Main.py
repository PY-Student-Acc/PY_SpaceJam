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
    def SetupScene(self):
        ShowBase.__init__(self)
       


        self.Universe.setColorScale(1.0, 0.0, 0.0, 1.0)
        self.Universe.reparentTo(self.render)
        self.Universe.setScale(0.25, 0.25, 0.25)
        self.Universe.setPos(-8, 42, 0)
       
        self.Universe.setScale(15000)
        
        self.Universe = self.loader.loadModel("./Assets/Universe/Universe.x")
        self.Universe.reparentTo(self.render)

        tex = self.loader.loadTexture("./Assets/Universe/starfield-in-blue")

        self.Universe.setTexture(tex, 1)
        
        self.Planet1 = self.loader.loadModel("./Assets/Planets/protoPlanet.x")
        self.Planet1.reparentTo(self.render)
        self.Planet1.setPos(150, 5000, 67)
        self.Planet1.setScale(69)

        self.Planet2 = self.loader.loadModel("./Assets/Planets/protoPlanet.x")
        self.Planet2.reparentTo(self.render)
        self.Planet2.setPos(250, 5000, 67)
        self.Planet2.setScale(420)

        self.Planet3 = self.loader.loadModel("./Assets/Planets/protoPlanet.x")
        self.Planet3.reparentTo(self.render)
        self.Planet3.setPos(150, 6000, 67)
        self.Planet3.setScale(34)

        self.Planet4 = self.loader.loadModel("./Assets/Planets/protoPlanet.x")
        self.Planet4.reparentTo(self.render)
        self.Planet4.setPos(190, 5000, 67)
        self.Planet4.setScale(29)

        self.Planet5 = self.loader.loadModel("./Assets/Planets/protoPlanet.x")
        self.Planet5.reparentTo(self.render)
        self.Planet5.setPos(150, 4200, 69)
        self.Planet5.setScale(490)

        self.Planet6 = self.loader.loadModel("./Assets/Planets/protoPlanet.x")
        self.Planet6.reparentTo(self.render)
        self.Planet6.setPos(10, 0, 67)
        self.Planet6.setScale(24)

        self.Spaceship = self.loader.loadmodel("./Assets/Spaceships/PercyJacksonIsBetter/PercyJacksonIsBetter.x")
        self.Spaceship.reparentTo(self.render) 
        self.Spaceship.setPos(0, 0, 0)
        self.Spaceship.serScale(1)

        self.SpaceStation = self.loader.loadmodel("./Assets/SpaceStation1B/spaceStation.x")

        fullCycle = 60

        for j in range(fullCycle):
            spaceJamClasses.Drone.droneCount += 1
            nickName = "Drone" + str(spaceJamClasses.Drone.droneCount)

            self.DrawCloudDefense(self.Planet1, nickName)
            self.DrawBaseballSeams(self.SpaceStation1, nickName, j, fullCycle, 2)


def DrawBaseballSeams(self, centralObject, droneName, step, numSeams, radius = 1):
    unitVec = defensePaths.BaseballSeams(step, numSeams, B = 0.4)
    unitVec.normalize()
    position = unitVec * radius * 250 + centralObject.modelNode.getPos()
    spaceJamClasses.Drone(self.loader, "./Assets/DroneDefender.obj", self.render, droneName, "./Assets/DroneDefender/octotoad1_auv.png", position, 5)

def DrawCloudDefense(self, centralObject, droneName):
    unitVec = defensePaths.Cloud()
    unitVec.normalize()
    position = unitVec * 500 + centralObject.modelNode.getPos()
    spaceJamClasses.Drone(self.loader, "./Assets/DroneDefender.obj", self.render, droneName, "./Assets/DroneDefender/octotoad1_auv.png", position, 10)


app = MyApp()
app.run()