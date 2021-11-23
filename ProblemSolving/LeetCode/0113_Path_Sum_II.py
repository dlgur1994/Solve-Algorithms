import sys
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Tree:
    def __init__(self):
        self.root = None
    
    def addNode(self, center, left, right): 
        if self.root == None:
            self.root = center
            center.val = int(center.val)
        
        if left.val != 'null':
            center.left = left
            left.val = int(left.val)
        if right.val != 'null':
            center.right = right
            right.val = int(right.val)

    def printNode(self, node):
        print(node.val)
        if node.left:
            self.printNode(node.left)
        if node.right:
            self.printNode(node.right)

class Solution:
    def dfs(self, node, arr, sum, targetsum):
        if node.left:
            arr += node
            self.dfs(node.left, arr, sum, targetsum)
        if node.right:
            arr += node
            self.dfs(node.right, arr, sum, targetsum)
            

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        ans = self.dfs(root, [], 0, targetSum)
        return ans

nodes = list(map(TreeNode,sys.stdin.readline().rstrip().split(',')))
targetsum = int(sys.stdin.readline())

tree = Tree()
for i in range(len(nodes)//2):
    tree.addNode(nodes[i], nodes[2*i+1], nodes[2*i+2])
# tree.printNode(tree.root)

mod = Solution()
print(mod.pathSum(tree.root, targetsum))