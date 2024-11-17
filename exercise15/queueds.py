#!/bin/python3

# ruff: noqa : F821
# pyright:reportUndefinedVariable=false
# pyright:reportOptionalMemberAccess=false
# pyright:reportAttributeAccessIssue=false
# pyright:reportFunctionMemberAccess=false


class QueNode(object):

    def __init__(self, val, nxt=None) -> None:
        self.val = val
        self.next = nxt

    def __repr__(self) -> str:
        nval = self.next and self.next.val
        return f"[{self.val}: {repr(nval)}]"


class QueDS(object):
    def __init__(self) -> None:
        self.front = None
        self.back = None

    def enque(self, queval):
        pass

    def deque(self):
        pass

    def traverse(self):
        pass

    def show_front(self):
        return self.front.val

    def show_back(self):
        return self.back.val

    def count(self):
        pass
