from dllist import Dlist
from unittest import TestCase


class Sllist_Test(TestCase):
    # def test_push(self):
    #     colors = Dlist()
    #     colors._invariant()
    #     assert colors.count() == 0
    #     colors.push("Pthalo Blue")
    #     colors._invariant()
    #     assert colors.count() == 1, colors.count()
    #     colors.push("Ultramarine Blue")
    #     colors.push("Locomotive Lumen")
    #     colors.push("Mercury Grey")
    #     colors._invariant()
    #     print(colors.dump())
    #     assert colors.count() == 3, colors.count()
    #     print("reached")

    def test_pop(self):
        colors = Dlist()
        colors.push("Magenta")
        # print("After 1", colors.count())
        colors.push("Alizarin")
        colors.push("Cadmium Yellow")
        colors.push("Torrent Blue")
        # print("After 3", colors.count())
        assert colors.pop() == "Torrent Blue"
        print("After 1st pop", colors.count())
        assert colors.pop() == "Cadmium Yellow"
        print("After 2nd pop", colors.count())
        assert colors.pop() == "Alizarin"

    def test_unshift(self):
        colors = Dlist()
        colors.push("Viridian")
        colors.push("Sap Green")
        colors.push("Van Dyke")
        assert colors.unshift() == "Viridian"
        assert colors.unshift() == "Sap Green"
        assert colors.unshift() == "Van Dyke"
        assert colors.unshift() is None

    def test_shift(self):
        colors = Dlist()
        colors.shift("Cadmium Orange")
        assert colors.count() == 1
        colors.shift("Carbazole Violet")
        assert colors.count() == 2
        assert colors.pop() == "Carbazole Violet"
        assert colors.count() == 1
        assert colors.pop() == "Cadmium Orange"
        assert colors.count() == 0

    def test_dump(self):
        colors = Dlist()
        assert colors.dump() == "Empty List"
        colors.push("Ultramarine Blue")
        # assert colors.dump() == "Ultramarine Blue"
        colors.push("Basilisk Brown")
        # assert colors.dump() == "Ultramarine Blue | Basilisk Brown"
        colors.push("MassEffect Magenta")
        # assert colors.dump() == "Ultramarine Blue | Basilisk Brown | MassEffect Magenta"
        assert colors.pop() == "MassEffect Magenta", colors.pop()
        print(colors.dump())
        assert colors.pop() == "Basilisk Brown", colors.pop()
        print(colors.dump())
        assert colors.dump() == "Ultramarine Blue", colors.dump()

    def test_remove(self):
        colors = Dlist()
        colors.push("Cobalt")
        colors.push("Zinc White")
        colors.push("Nickle Yellow")
        colors.push("Perinone")
        print(colors.dump())
        assert colors.remove("Cobalt") == 0
        print(colors.dump())
        assert colors.remove("Perinone") == 2
        # colors.dump("after perinone")
        colors.dump()
        assert colors.remove("Nickle Yellow") == 1
        assert colors.remove("Zinc White") == 0

    def test_first(self):
        colors = Dlist()
        colors.push("Cadmium Red Light")
        assert colors.first() == "Cadmium Red Light"
        colors.push("Hansa Yellow")
        assert colors.first() == "Cadmium Red Light"
        colors.shift("Pthalo Green")
        assert colors.first() == "Cadmium Red Light"

    def test_last(self):
        colors = Dlist()
        colors.push("Cadmium Red Light")
        assert colors.last() == "Cadmium Red Light"
        colors.push("Hansa Yellow")
        assert colors.last() == "Hansa Yellow"
        colors.shift("Pthalo Green")
        assert colors.last() == "Pthalo Green"

    # def test_get(self):
    #     colors = Dlist()
    #     colors.push("Vermillion")
    #     # print(colors.get(0))
    #     assert colors.get(0) == "Vermillion"
    #     colors.push("Sap Green")
    #     assert colors.get(0) == "Vermillion"
    #     assert colors.get(1) == "Sap Green"
    #     colors.push("Cadmium Yellow Light")
    #     assert colors.get(0) == "Vermillion"
    #     assert colors.get(1) == "Sap Green"
    #     assert colors.get(2) == "Cadmium Yellow Light"
    #     print(colors.dump())
    #     assert colors.pop() == "Cadmium Yellow Light"
    #     assert colors.get(0) == "Vermillion"
    #     assert colors.get(1) == "Sap Green"
    #     print(colors.dump())
    #     assert colors.get(2) is None, colors.get(2)
    #     colors.pop()
    #     assert colors.get(0) == "Vermillion"
    #     colors.pop()
    #     print(colors.dump())
    #     assert colors.get(0) is None
