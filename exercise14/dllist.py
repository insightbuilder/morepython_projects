from __future__ import annotations
from typing import Optional

# ruff: noqa : F821
# pyright:reportUndefinedVariable=false


class DNode(object):
    def __init__(
        self,
        val: int | str,
        next: Optional[Dnode] = None,
        prev: Optional[Dnode] = None,
    ) -> None:
        self.val = val
        self.next = next
        self.prev = prev

    def __repr__(self) -> str:
        nval = self.next and self.next.val or None
        pval = self.prev and self.prev.val or None
        return f"[{repr(pval)} -> {self.val} <- {repr(nval)}]"


# - Are there zero elements? Then self.begin
#   and self.end need to be None.
# - If there is one element, then self.begin
#   and self.end have to be equal (point at
#   same node).
# - The ﬁrst element must always have a prev
#   that is None.
# - The last element must always have a next
#   that is None.


class Dlist(object):

    def __init__(self) -> None:
        self.begin = None
        self.end = None

    def _invariant(self):
        """Checks if the structure is working correctly by
        ensuring all the invariants mentioned are met"""

    def push(self, obj: str):
        """Appends a new value on the end of the list."""
        # create Dnode from obj
        entry = DNode(obj)
        # if self.begin is none, then assign entry to it
        if self.begin is None:
            self.begin = entry
            self.end = self.begin
        # else go to the end of the list
        # keep track of prev also
        else:
            # print(f"Obj is {obj}")
            curr = self.begin
            prev = curr.prev
            while True:
                if curr.next:
                    curr = curr.next
                    prev = curr.prev
                else:
                    break
            # need to assign the prev value to curr
            entry.prev = prev
            # assign entry as next to that current
            curr.next = entry
            # then assign that curr to self.end
            self.end = entry

    def pop(self):
        """Removes the last item and returns it."""

    def shift(self, obj):
        """Actually just another name for push."""

    def unshift(self):
        """Removes the first item (from begin) and returns it."""

    def detach_node(self, node):
        """You'll need to use this operation sometimes, but mostly
        inside remove(). It should take a node, and detach it from the
        list, whether the node is at the front, end, or in the middle."""

    def remove(self, obj):
        """Finds a matching item and removes it from the list."""

    def first(self):
        """Returns a *reference* to the first item, does not remove."""

    def last(self):
        """Returns a reference to the last item, does not remove."""

    def count(self):
        """Counts the number of elements in the list."""
        # if self.begin and end are none, then 0
        if self.begin is None or self.end is None:
            return 0
        # if begin and end are same then 1
        elif self.begin == self.end:
            return 1
        else:
            # count each element till end of the list
            curr = self.begin
            count = 0
            while True:
                if curr.next:
                    curr = curr.next
                    count += 1
                else:
                    return count

    def get(self, index):
        """Get the value at index."""

    def dump(self):
        """Debugging function that dumps the contents of the list"""
        outstr = ""
        if self.begin is None and self.end is None:
            return "Empty List"
        elif self.begin:
            return str(self.begin)
        else:
            curr = self.begin
            while True:
                if curr.next:
                    outstr += str(curr)
                    curr = curr.next
                else:
                    break
        return outstr
