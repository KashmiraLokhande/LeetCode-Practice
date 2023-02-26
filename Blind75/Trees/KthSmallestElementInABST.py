from typing import Optional
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 0
        stack = []
        curr = root
        
        while curr or stack :
            while curr:
                print(curr.val)
                stack.append(curr)
                curr = curr.left
            # print(stack.pop().val)
            
            curr = stack.pop()
            n += 1
            if n == k:
                return curr.val
            curr = curr.right

# Driver Code
Q = deque()
 
# Helper function helps us in adding data
# to the tree in Level Order
def insertValue(data, root):
    newnode = TreeNode(data)
    if Q:
        temp = Q[0]
    if root == None:
        root = newnode
    elif temp.left == None:
        temp.left = newnode
    elif temp.right == None:
        temp.right = newnode
        atemp = Q.popleft()
    Q.append(newnode)
    return root
 
# Function which calls add which is responsible
# for adding elements one by one
def createTree(a, root):
    for i in range(len(a)):
        root = insertValue(a[i], root)
    return root
# Function for printing level order traversal
def levelOrder(root):
    Q = deque()
    Q.append(root)
    while Q:
        temp = Q.popleft()
        print(temp.val, end = ' ')
        if temp.left != None:
            Q.append(temp.left)
        if temp.right != None:
            Q.append(temp.right)
            
if __name__ == "__main__":
    a = [3,1,4,None,2]
    k = 1
    # a = [5,3,6,2,4,None,None,1]
    # k = 3
    root = None
    root = createTree(a, root)
    levelOrder(root)
    print(Solution().kthSmallest(root,k))
