from __future__ import annotations
from typing import Optional

# ruff: noqa : F821
# pyright:reportUndefinedVariable=false
# pyright:reportOptionalMemberAccess=false


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
        # if count = 0, the self.begin and self.end is none
        if self.count() == 0:
            print("Empty list")
            assert (
                self.begin is None and self.end is None
            ), "self.begin & self.end is not None when count is 0"
        elif self.count() == 1:
            print("List with 1 count")
            assert (
                self.begin == self.end
            ), "self.begin is not equal to self.end when count 1"
            assert self.begin.prev is None, "self.begin.prev is not None"
            assert self.end.next is None, "self.end.next is not None"
        else:
            print("Checks at other situations")
            assert self.begin.prev is None, "self.begin.prev is not None"
            assert self.end.next is None, "self.end.next is not None"

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
            curr = self.begin
            prev = curr.prev
            while True:
                if curr.next:
                    curr = curr.next
                    prev = curr.prev
                else:
                    break
            # need to assign the prev value of entry to curr
            entry.prev = curr
            # assign entry as next to that current
            curr.next = entry
            # then assign that curr to self.end
            self.end = entry

    def pop(self):
        """Removes the last item and returns it."""
        if self.begin is None and self.end is None:
            return None
        elif self.begin == self.end:
            pnode = self.begin
            self.begin = None
            self.end = None
            return pnode.val
        else:
            # assign last node to pnode
            pnode = self.end
            # get the prev node and assign to end_node
            end_node = self.end.prev
            # make end's next node to None
            end_node.next = None
            # make end node self.end
            self.end = end_node
            return pnode.val

    def shift(self, obj):
        """Actually just another name for push."""
        self.push(obj)

    def unshift(self):
        """Removes the first item (from begin) and returns it."""
        first_node = self.begin

    def detach_node(self, node: DNode):
        """You'll need to use this operation sometimes, but mostly
        inside remove(). It should take a node, and detach it from the
        list, whether the node is at the front, end, or in the middle."""
        if self.begin is None and self.end is None:
            print("Empty List")
            return None

        elif self.count() == 1 and self.begin == node:
            # detach the begin and end nodes
            print("Found node at begin")
            self.begin = None
            self.end = None
            return node

        else:
            # search for the node by travesing the list
            curr = self.begin
            while True:
                if curr.next:
                    if curr == node:
                        print("Found node detaching it")
                        cprev = curr.prev
                        cnext = curr.next
                        cprev.next = cnext
                        cnext.prev = cprev

                        return curr
                    curr = curr.next
                else:
                    # if I did not find the node then return None
                    print("did not find node")
                    return None

    def remove(self, obj: str):
        """Finds a matching item and removes it from the list.
        Returns the index of the removed item"""
        # assert self.count() == 1, self.count()

        if self.begin is None and self.end is None:
            print("Empty List")
            return None

        elif self.begin.val == obj:
            # detach the begin
            print("Found node at begin")
            # check if the begin and end node are same
            if self.begin == self.end:
                self.begin = None
                self.end = None
                return 0
            else:  # else there are more elements,
                # then assign begin to begin.next
                # then return the element index
                self.begin = self.begin.next
                return 0

        elif self.end.val == obj:
            print("Found node at end")
            # assign last node to end_node
            end_node = self.end.prev
            cnt = self.count()
            # make end's next node to None
            end_node.next = None
            # make end node self.end
            self.end = end_node
            return cnt

        else:
            # search for the node by travesing the list
            curr = self.begin
            idx = 0
            while True:
                if curr.next:
                    if curr.val == obj:
                        print("Found node detaching it")
                        cprev = curr.prev
                        cnext = curr.next
                        cprev.next = cnext
                        cnext.prev = cprev

                        return idx

                    curr = curr.next
                    idx += 1
                else:
                    # if I did not find the node then return None
                    print("did not find node")
                    return None

    def first(self):
        """Returns a *reference* to the first item, does not remove."""
        return self.begin.val

    def last(self):
        """Returns a reference to the last item, does not remove."""
        return self.end.val

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
        if self.count() == 0 or index > self.count():
            return None
        elif index == 0:
            return self.begin.val
        elif index == self.count():
            return self.end.val
        else:
            len = 0
            curr = self.begin
            while True:
                if curr.next:
                    curr = curr.next
                    len += 1
                    if len == index:
                        return curr.val
                else:
                    return None

    def dump(self):
        """Debugging function that dumps the contents of the list"""
        outstr = ""
        if self.begin is None and self.end is None:
            return "Empty List"
        elif self.begin == self.end:
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
