# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = [root]
        visited = []
        return_list = []
        while len(stack):
            node = stack.pop()
            if not node:
                continue
            if node not in visited:
                visited.append(node)
                if node.left != None:
                    stack.append(node)
                    stack.append(node.left)
                else:
                    return_list.append(node.val)
                    if node.right != None:
                        stack.append(node.right)
            else:
                return_list.append(node.val)
                if node.right != None:
                    stack.append(node.right)
        return return_list