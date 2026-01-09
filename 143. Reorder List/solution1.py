def func(head):
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    sec_pt = slow.next
    slow.next = tail = None
    while sec_pt:
        tmp = sec_pt.next
        sec_pt.next = tail
        tail = sec_pt
        sec_pt = tmp
    
    head_sec = tail
    while head and head_sec:
        tmp, tmp2 = head.next, head_sec.next
        head.next = head_sec
        head_sec.next = tmp
        head, head_sec = tmp, tmp2