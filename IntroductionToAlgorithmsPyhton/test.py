import ListNode

nums1 = [1,2,4]
nums2 = [1,3,4]

for i in range(len(nums1)):
    if (i == len(nums1) - 1):
        nodes1 = ListNode.ListNode(nums1[i])
    else:
        nodes1 = ListNode.ListNode(nums1[i], nums1[i+1])

while nodes1.val != 4:
    print(nodes1.val)