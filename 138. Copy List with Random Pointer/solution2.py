def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        node_map = {}
        dummy = head

        while dummy:
            node_map[dummy] = Node(dummy.val)
            dummy = dummy.next

        for key, val in node_map.items():
            val.next = node_map.get(key.next)
            val.random = node_map.get(key.random)

        return node_map.get(head)