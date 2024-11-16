#!/bin/python3

# ruff: noqa : F821
# pyright:reportUndefinedVariable=false
# pyright:reportOptionalMemberAccess=false
# pyright:reportAttributeAccessIssue=false
# pyright:reportFunctionMemberAccess=false


class StackNode(object):

    def __init__(self, val, nxt=None):
        self.val = val
        self.next = nxt

    def __repr__(self) -> str:
        nval = self.next and self.next.val or None
        return f"[{self.val}: {repr(nval)}]"


# - Are there zero elements? self.top has to be None.
# - If there is one element, then self.top.next must be none
# - The ﬁrst element must always have a prev
#   that is None.


class DStack(object):

    def __init__(self):
        self.top = None

    def _invariant(self):
        if self.count() == 0:
            assert self.top is None, "count 0 invariant failed"
        if self.count() == 1:
            assert self.top is not None, "count 1 invariant failed"
        if self.count() == 2:
            assert self.top.next is not None, "count 2 invariant failed"

    def push(self, val):
        """Pushes new value to the top"""
        snode = StackNode(val)
        # if list empty, then place node at top
        if self.top is None:
            self.top = snode
            return
        # else there is a top node, then make
        # it as a snode's next
        snode.next = self.top
        self.top = snode

    def pop(self):
        """Pop the value at the top"""
        # return none if list is empty
        if self.top is None:
            return None
        else:
            curr = self.top
            self.top = curr.next
            return curr.val

    def top(self):
        """Returns the reference to the top value"""
        return self.top.val

    def dump(self):
        """Prints the value of all the elements"""

    def count(self):
        """Count the elements in the stack"""
        if self.top is None:
            return 0
        cnt = 1
        curr = self.top
        while True:
            if curr.next:
                cnt += 1
                curr = curr.next
            else:
                return cnt
