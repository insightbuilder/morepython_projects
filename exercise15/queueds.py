#!/bin/python3

# ruff: noqa : F821
# pyright:reportUndefinedVariable=false
# pyright:reportOptionalMemberAccess=false
# pyright:reportAttributeAccessIssue=false
# pyright:reportFunctionMemberAccess=false


class QueNode(object):

    def __init__(self, val, nxt=None, prv=None) -> None:
        self.val = val
        self.next = nxt
        self.prev = prv

    def __repr__(self) -> str:
        nval = self.next and self.next.val
        pval = self.prev and self.prev.val
        return f"[{repr(pval)}: {self.val} :{repr(nval)}]"


class QueDS(object):
    def __init__(self) -> None:
        self.front = None
        self.back = None

    def _invariant(self):
        pass

    def enque(self, queval):
        toque = QueNode(queval)
        if self.front is None and self.back is None:
            self.front = toque
            self.back = self.front
            return
        # if self.front is self.back
        # then assign node to back
        # not the case then enque to back, remember
        # qnode is dbl_link list
        else:
            # print("else in enque", self.back)
            bnode = self.back
            bnode.next = toque
            toque.prev = bnode
            self.back = toque

    def deque(self):
        if self.front is None and self.back is None:
            return None
        # check if self.front is back
        elif self.front is self.back:
            deq = self.front
            self.front = None
            self.back = None
            return deq.val

        elif self.front:
            deq = self.front
            next = self.front.next
            next.prev = None
            self.front = next
            return deq.val
        else:
            print("place holder")

    def traverse(self):
        if self.front is None and self.back is None:
            return "Empty List"
        else:
            curr = self.front
            out = repr(curr)
            while True:
                if curr.next:
                    curr = curr.next
                    out += repr(curr)
                else:
                    return out

    def show_front(self):
        return self.front.val

    def show_back(self):
        return self.back.val

    def count(self):
        # print("front", self.front)
        # print("back", self.back)
        if self.front is None and self.back is None:
            return 0
        elif self.back is self.front:
            return 1
        else:
            cnt = 1
            curr = self.front
            while True:
                if curr.next:
                    print("in count while", curr)
                    cnt += 1
                    curr = curr.next
                else:
                    return cnt
