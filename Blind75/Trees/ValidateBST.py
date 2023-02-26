from typing import Optional
import math
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        
        def validate(node, low = -math.inf , high = math.inf):
            if not node:
                return True
            if node.val <= low or node.val >= high:
                return False
            
            return validate(node.left, low, node.val) and validate(node.right, node.val, high)
        return validate(root)

if __name__ == "__main__":
    elements = [5,1,4,None,None,3,6]
    root_node = TreeNode(val=elements[0])
    nodes = [root_node]
    for i, x in enumerate(elements[1:]):
        if x is None:
            continue
        parent_node = nodes[i // 2]
        is_left = (i % 2 == 0)
        node = TreeNode(val=x)
        if is_left:
            parent_node.left = node
        else:
            parent_node.right = node
        nodes.append(node)
    print(nodes[0].val)
    print(nodes[4].left)
    
