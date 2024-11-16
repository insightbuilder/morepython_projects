from stack import DStack, StackNode
from unittest import TestCase


class TestDStack(TestCase):
    def test_stack_node(self):
        node1 = StackNode(5)
        assert repr(node1) == "[5: None]", repr(node1)

    def test_push(self):
        colors = DStack()
        colors._invariant()
        assert colors.count() == 0
        colors.push("Pthalo Blue")
        assert colors.count() == 1, colors.count()
        colors._invariant()
        colors.push("Ultramarine Blue")
        colors.push("Locomotive Lumen")
        colors.push("Mercury Grey")
        colors._invariant()
        print(colors.dump())
        assert colors.count() == 4, colors.count()
        print("reached")

    def test_pop(self):
        colors = DStack()
        colors.push("Magenta")
        colors.push("Alizarin")
        colors.push("Cadmium Yellow")
        colors.push("Torrent Blue")
        assert colors.pop() == "Torrent Blue"
        print("After 1st pop", colors.count())
        assert colors.pop() == "Cadmium Yellow"
        print("After 2nd pop", colors.count())
        assert colors.pop() == "Alizarin"

    def test_top(self):
        colors = DStack()
        colors.push("Magenta")
        assert colors.top() == "Magenta"
        colors.push("Alizarin")
        colors.push("Cadmium Yellow")
        assert colors.top() == "Cadmium Yellow"
        assert colors.pop() == "Cadmium Yellow"
        assert colors.pop() == "Alizarin"
        colors.push("Torrent Blue")
        assert colors.top() == "Torrent Blue"
