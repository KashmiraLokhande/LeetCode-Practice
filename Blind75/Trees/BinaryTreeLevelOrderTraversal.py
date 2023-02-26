from collections import deque
class TreeNode:
    def __init__(self, val = 0, left = None, right= None) -> None:
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root:TreeNode) -> list[list[int]]:
        res = []
        Q = deque()
        if root:
            Q.append(root)
        while Q:
            val = []
            for i in range(len(Q)):
                node = Q.popleft()
                val.append(node.val)
                if node.left:
                    Q.append(node.left)
                if node.right:
                    Q.append(node.right)
            res.append(val)
        return res

#driver code

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
if __name__ == "__main__":
    a = [3,9,20,None,None,15,7]
    root = None
    root = createTree(a, root)
    print(Solution().levelOrder(root))
