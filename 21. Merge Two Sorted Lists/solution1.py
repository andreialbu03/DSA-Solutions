def func(list1, list2):
    dummy = ListNode(0, None)
    prev = dummy

    while list1 and list2:
        if list1.val < list2.val:
            prev.next = list1
            list1 = list1.next
        else:
            prev.next = list2
            list2 = list2.next
        prev = prev.next
        
    if list1:
        prev.next = list1
    if list2:
        prev.next = list2

    return dummy.next