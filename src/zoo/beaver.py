
from .animal import Animal

class Beaver(Animal):
    def__int__(self, name="Boo"):
        super().__init__(name, species="Beaver")

    def sound(self):
        return "gnaws"

    def action(self):
        return "builds dams like a workaholic."


        