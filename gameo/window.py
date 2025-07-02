from panda3d.core import loadPrcFile
loadPrcFile("config/conf.prc")
from direct.showbase.ShowBase import ShowBase


class GameoWindow(ShowBase):
    def __init__(self):
        super().__init__()


game = GameoWindow()
game.run()
