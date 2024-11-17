from queueds import QueDS, QueNode
from unittest import TestCase


class TestQueDS(TestCase):
    def test_quenode(self):
        node1 = QueNode(5)
        assert repr(node1) == "[5: None]", repr(node1)

    def test_enque(self):
        colors = QueDS()
        colors._invariant()
        assert colors.count() == 0
        colors.enque("Pthalo Blue")
        print(colors.traverse())
        assert colors.count() == 1, colors.count()
        colors._invariant()
        colors.enque("Ultramarine Blue")
        colors.enque("Locomotive Lumen")
        colors.enque("Mercury Grey")
        colors._invariant()
        print(colors.traverse())
        assert colors.count() == 4, colors.count()
        print("reached")

    # def test_deque(self):
    #     colors = QueDS()
    #     colors.enque("Magenta")
    #     colors.enque("Alizarin")
    #     colors.enque("Cadmium Yellow")
    #     colors.enque("Torrent Blue")
    #     assert colors.deque() == "Torrent Blue"
    #     print("After 1st deque", colors.count())
    #     assert colors.deque() == "Cadmium Yellow"
    #     print("After 2nd deque", colors.count())
    #     assert colors.deque() == "Alizarin"

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
