import ListNode

def mergeTwoLists(self, list1, list2):
    if list1 and list2:
        if list1.val > list2.val:
            list1, list2 = list2, list1
        list1.next = self.mergeTwoLists(list1.next, list2) #selfの動きがわからない
    return list1 or list2

list1 = ListNode()
#ListNode型のlist1,list2を用意できなくてテストを実行できない

