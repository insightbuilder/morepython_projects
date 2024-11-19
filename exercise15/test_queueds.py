from queueds import QueDS, QueNode
from unittest import TestCase


class TestQueDS(TestCase):
    # def test_quenode(self):
    #     node1 = QueNode(5)
    #     assert repr(node1) == "[None: 5 :None]", repr(node1)

    # def test_enque(self):
    #     colors = QueDS()
    #     assert colors.count() == 0, colors.count()
    #     colors._invariant()
    #     colors.enque("Pthalo Blue")
    #     assert colors.show_back() == "Pthalo Blue"
    #     # print(colors.traverse())
    #     assert colors.count() == 1, colors.count()
    #     colors._invariant()
    #     colors.enque("Ultramarine Blue")
    #     colors.enque("Locomotive Lumen")
    #     assert colors.show_back() == "Locomotive Lumen"
    #     colors.enque("Mercury Grey")
    #     assert colors.show_back() == "Mercury Grey"
    #     # colors._invariant()
    #     print(colors.traverse())
    #     assert colors.count() == 4, colors.count()
    #     # print("reached")

    # def test_deque(self):
    #     colors = QueDS()
    #     assert colors.deque() is None
    #     colors.enque("Magenta")
    #     colors.enque("Alizarin")
    #     colors.enque("Cadmium Yellow")
    #     colors.enque("Torrent Blue")
    #     print(colors.traverse())
    #     assert colors.deque() == "Magenta"
    #     print("After 1st deque", colors.count())
    #     assert colors.deque() == "Alizarin"
    #     print("After 2nd deque", colors.count())
    #     assert colors.deque() == "Cadmium Yellow"

    def test_front_back(self):
        stars = QueDS()
        stars.enque("Super Nova")
        stars.enque("Neutron Star")
        assert stars.show_front() == "Super Nova", stars.show_front()
        stars.deque()
        assert stars.show_back() == "Neutron Star", stars.show_back()
        stars.enque("Worm Hole")
        stars.enque("Asteroids")
        print(stars.traverse())

    # def test_topoff(self):
    #     colors = QueDS()
    #     colors.enque("Magenta")
    #     print(colors.traverse())
    #     print(colors.count())
    #     colors.topoff()
    #     assert colors.topoff() == "Magenta", colors.topoff()
    #     colors.enque("Alizarin")
    #     colors.enque("Cadmium Yellow")
    #     assert colors.topoff() == "Cadmium Yellow"
    #     assert colors.deque() == "Cadmium Yellow"
    #     assert colors.deque() == "Alizarin"
    #     colors.enque("Torrent Blue")
    #     assert colors.topoff() == "Torrent Blue"
