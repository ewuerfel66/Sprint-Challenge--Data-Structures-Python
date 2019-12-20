from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # Not at capacity
        if self.storage.length < self.capacity:
            self.storage.add_to_head(item)

        # At capacity
        else:
            # Remove oldest item
            self.storage.remove_from_tail()
            # Add new item
            self.storage.add_to_tail(item)
            self.storage.move_to_front(self.storage.tail)

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # Start at the tail
        cur = self.storage.tail
        list_buffer_contents.append(cur.value)

        while cur.prev is not None:
            cur = cur.prev
            list_buffer_contents.append(cur.value)

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
