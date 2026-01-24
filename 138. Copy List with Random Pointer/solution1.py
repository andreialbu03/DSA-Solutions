def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        node_map = {}
        dummy = head

        while dummy:
            node_map[dummy] = Node(dummy.val)
            dummy = dummy.next

        for key, val in node_map.items():
            next_val = key.next
            if next_val:
                val.next = node_map[key.next]
            else:
                val.next = next_val

            random_val = key.random
            if random_val:
                val.random = node_map[key.random]
            else:
                val.random = random_val

        return next(iter(node_map.values())) if node_map else None