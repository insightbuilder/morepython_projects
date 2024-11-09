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
            # a -> b -> c ->d
            prev = None
            while True:
                # print("while in pop")
                if curr.next:
                    # print(f"Printing curr: {curr}")
                    # print(f"Printing prev: {prev}")
                    prev = curr
                    curr = curr.next
                else:
                    remove = curr
                    # print("Remove is:", remove)
                    # print("prev is:", prev)
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
                self.begin = self.end = None
                return 0
        # if self.begin is equal to obj then return 0
        # and assign self.begin to its next

        elif self.begin.val == obj:
            self.begin = self.begin.next
            return 0
        # else
        # remove the element from list chain, match element
        # do the reattachment between the prev and next
        # how to remember the prev node
        else:
            pos = 0
            curr = self.begin
            prev = None
            while True:
                # check if value == tgt
                if curr.val == obj:
                    # no need to check if prev is none
                    prev.next = curr.next
                    # return pos
                    return pos
                # if not move to the next element
                if curr.next:
                    prev = curr
                    curr = curr.next
                    # increment only when moving to
                    # next elment
                    pos += 1
                print(f"Printing prev in while: {prev}")

        # if list has > 1 elements, traverse the list to find the element

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
            # print("Count", count)
            return count

    def get(self, index):
        """Get the value at index."""
        # print("Count in get: ", self.count())
        if self.count() < index or self.count() == 0:
            return None
        else:
            pos = 0
            curr = self.begin
            while pos != index and curr.next:
                curr = curr.next
                pos += 1
            if pos == index:
                return curr.val
            else:
                None

    def dump(self):
        """Debugging function that dumps the contents of the list."""
        if self.begin is None:
            return "Empty List"
        elif self.begin == self.end:
            return self.begin.val
        else:
            out_string = self.begin.val
            curr = self.begin
            while True:
                if curr.next:
                    out_string += f" | {curr.next.val}"
                    curr = curr.next
                else:
                    return out_string
