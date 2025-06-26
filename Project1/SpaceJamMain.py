from math import pi, sin, cos
from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor
from direct.interval.IntervalGlobal import Sequence
from panda3d.core import Point3


class MyApp(ShowBase):
    

    def __init__(self):
        ShowBase.__init__(self)
        self.SetupScene()

    def SetupScene(self):
       
        self.Universe = self.loader.loadModel('./Assets/Universe/Universe.x') # puts universe together
        self.Universe.reparentTo(self.render)
        self.Universe.setPos(-8, 42, 0)
        tex = self.loader.loadTexture('./Assets/Universe/Universe.jpg')
        self.Universe.setTexture(tex, 1)
        self.Universe.setScale(15000)
        
        self.Planet1 = self.loader.loadModel("./Assets/Planets/protoPlanet.x")
        texPlanet1 = self.loader.loadTexture('./Assets/Planets/Grass_Block_JE2.png')
        self.Planet1.setTexture(texPlanet1, 1)
        self.Planet1.reparentTo(self.render)
        self.Planet1.setPos(-250, 1200, 54)
        self.Planet1.setScale(190)

        self.Planet2 = self.loader.loadModel("./Assets/Planets/protoPlanet.x")
        texPlanet2 = self.loader.loadTexture('./Assets/Planets/KSA_Popstar.jpg')
        self.Planet2.setTexture(texPlanet2, 1)
        self.Planet2.reparentTo(self.render)
        self.Planet2.setPos(250, 1000, 67)
        self.Planet2.setScale(220)

        self.Planet3 = self.loader.loadModel("./Assets/Planets/protoPlanet.x")
        texPlanet3 = self.loader.loadTexture("./Assets/Planets/Lego_ego.jpg")
        self.Planet3.setTexture(texPlanet3, 1)
        self.Planet3.reparentTo(self.render)
        self.Planet3.setPos(150, -1200, 67)
        self.Planet3.setScale(340)

        self.Planet4 = self.loader.loadModel("./Assets/Planets/protoPlanet.x")
        texPlanet4 = self.loader.loadTexture("./Assets/Planets/Meap_Planet.jpg")
        self.Planet4.setTexture(texPlanet4, 1)
        self.Planet4.reparentTo(self.render)
        self.Planet4.setPos(-150, 1500, 67)
        self.Planet4.setScale(109)

        self.Planet5 = self.loader.loadModel("./Assets/Planets/protoPlanet.x")
        texPlanet5 = self.loader.loadTexture("./Assets/Planets/small_cube__24639.jpg")
        self.Planet5.setTexture(texPlanet5, 1)
        self.Planet5.reparentTo(self.render)
        self.Planet5.setPos(150, 4200, 69)
        self.Planet5.setScale(490)

        self.Planet6 = self.loader.loadModel("./Assets/Planets/protoPlanet.x")
        texPlanet6 = self.loader.loadTexture("./Assets/Planets/SSBU_spirit_Moon.png")
        self.Planet6.setTexture(texPlanet6, 1)
        self.Planet6.reparentTo(self.render)
        self.Planet6.setPos(10, 330, 67)
        self.Planet6.setScale(124)

        self.Spaceship = self.loader.loadModel("./Assets/Spaceships/PercyJacksonIsBetter/PercyJacksonIsBetter.x")
        self.Spaceship.reparentTo(self.render) 
        self.Spaceship.setPos(0, 0, 0)
        self.Spaceship.setScale(5)

        self.SpaceStation = self.loader.loadModel("./Assets/SpaceStation1B/spaceStation.x")
        self.SpaceStation.reparentTo(self.render)
        self.SpaceStation.setPos(25, 25, 25)
        self.SpaceStation.setScale(5)

app = MyApp()
app.run()