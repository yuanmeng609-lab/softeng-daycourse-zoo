
from .animal import Animal

class Beaver(Animal):
    def __init__(self, name="Boo"):
        super().__init__(name, species="Beaver")

    def sound(self):
        return "Meow"

    def action(self):
        return "builds dams like a workaholic."

def test_beaver():
    b =Beaver("Boo")
    assert b.name == "Boo"
    assert b.species == "Beaver"
    assert b.sound() == "Meow"
    assert b.action() == "builds dams like a workaholic."

        