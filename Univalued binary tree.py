//https://leetcode.com/submissions/detail/600786275/


def findDuplicate(root, start):
    flag = True
    if root:
        if root.val != start:
            return False

        if root.left:
            flag = findDuplicate(root.left, start)

        if flag == False:
            return False

        if root.right and flag == True:
            return findDuplicate(root.right, start)
    return True


return (findDuplicate(root, root.val))