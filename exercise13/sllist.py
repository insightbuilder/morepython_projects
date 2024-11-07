class Node(object):
    def __init__(self, val, next=None) -> None:
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        nval = self.next and self.next.val or None
        return f"[{self.val}:{repr(nval)}]"


class SingleLinkedList(object):
    def __init__(self):
        self.begin: Node | None = None
        self.end: Node | None = None

    def push(self, obj):
        """Appends a new value on the end of the list."""
        obj = Node(val=obj)
        if self.begin is None:
            self.begin = obj
            self.end = self.begin
            # both the nodes the next is none
            return
        curr = self.begin
        while True:
            if curr.next:
                curr = curr.next
            else:  # by end of the while loop we are
                curr.next = obj  # at the end of the list
                self.end = obj  # assign the curr to s.end too
                break

    def pop(self):
        """Removes the last item and returns it."""
        if self.end is None or self.begin is None:
            return None
        elif self.begin == self.end:
            remove = self.begin
            self.begin = None
            self.end = None
            return remove.val
        else:
            # self.end doesn't know who is before it
            # that means need to traverse from the start
            # with the objective of capturing the node prev 2 last
            curr = self.begin

            while True:
                # print("while in pop")
                prev = curr
                if curr.next:
                    next = curr.next
                    curr = next
                remove = prev.next
                prev.next = None
                self.end = prev
                return remove.val

    def shift(self, obj):
        """Another name for push."""
        self.push(obj)
        return

    def unshift(self):
        """Removes the first item and returns it."""
        if self.begin is None:
            return None
        elif self.begin == self.end:
            popout = self.begin
            self.begin = None
            self.end = None
            return popout.val
        else:
            popout = self.begin
            self.begin = self.begin.next
            return popout.val

    def remove(self, obj):
        """Finds a matching item and removes it from the list.
        Returns the position from which it was removed."""
        # if list is empty return None
        if self.begin is None or self.end is None:
            return None
        # if begin == end and equal to obj, return it and clean list
        elif self.begin == self.end:
            if self.begin.val == obj:
                return 0
        else:
            pos = 0
            curr = self.begin
            while True:
                prev = curr
                pos += 1
                if curr.next:
                    if prev.val == obj:
                        # do the reattachment
                        next = curr.next
                        return pos
                    curr = curr.next

        # if list has > 1 elements, traverse the list to find the element
        # remove the element from list chain, and do the reattachments

    def first(self):
        """Returns a *reference* to the first item, does not remove."""
        if self.begin is not None:
            return self.begin.val

    def last(self):
        """Returns a reference to the last item, does not remove."""
        if self.end is not None:
            return self.end.val

    def count(self):
        """Counts the number of elements in the list."""
        if self.begin is None:
            return 0
        elif self.begin == self.end:
            return 1
        else:
            count = 1
            curr = self.begin
            while curr.next:
                count += 1
                curr = curr.next
            print("Count", count)
            return count

    def get(self, index):
        """Get the value at index."""

    def dump(self, mark):
        """Debugging function that dumps the contents of the list."""
