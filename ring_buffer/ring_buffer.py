from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # First Entry
        if self.storage.length == 0:
            self.storage.add_to_tail(item)
            # Mark as oldest
            self.current = self.storage.tail

        # Not at capacity
        elif self.storage.length < self.capacity:
            self.storage.add_to_tail(item)

        # At capacity
        else:
            # Overwrite value of oldest item
            self.current.value = item

            # Change oldest item
            if self.current.next is not None:
                self.current = self.current.next
            else: # tail
                self.current = self.storage.head


    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        if self.storage.head:
            # Start at the head
            cur = self.storage.head
            list_buffer_contents.append(cur.value)

            while cur.next is not None:
                cur = cur.next
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
