from panda3d.core import loadPrcFile

loadPrcFile("config/conf.prc")
from direct.showbase.ShowBase import ShowBase


class GameoWindow(ShowBase):
    def __init__(self):
        super().__init__()
        # disables the default camera control
        # self.disable_mouse()
        scene = self.loader.loadModel("models/environment")
        scene.reparentTo(self.render)


game = GameoWindow()
game.run()
