from typing import Optional
from collections import deque

# Definition for a binary tree node. 
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+ 1 : ], inorder[mid +1 :])
        
        return root

# Driver Code

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
    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]
    levelOrder(Solution().buildTree(preorder, inorder))
    res = Solution().buildTree(preorder, inorder)
    # print(res.left)
