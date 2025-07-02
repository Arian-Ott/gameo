from panda3d.core import loadPrcFile

loadPrcFile("config/conf.prc")
from direct.showbase.ShowBase import ShowBase


class GameoWindow(ShowBase):
    def __init__(self):
        super().__init__()
        # disables the default camera control
        self.disable_mouse()
        scene = self.loader.loadModel("models/box")
        scene.setPos(0, 10, 0)

        scene.reparentTo(self.render)
        panda = self.loader.loadModel("models/panda")
        panda.setPos(-2, 10, 0)
        panda.setScale(0.2, 0.2, 0.2)
        panda.reparentTo(self.render)


game = GameoWindow()
game.run()
