from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class SolutionDFT:
    def delNodes(self, root: [TreeNode], to_delete: list[int]) -> list[int]:
        traversal = []

        # depth first traversal
        def dft (root, is_root):
            
            if root.val in to_delete:
                if root.left is not None:
                    dft(root.left, True)
                if root.right is not None:
                    dft(root.right, True)
                root.left = None
                root.right = None
                return None
            
            if is_root:
                traversal.append(root)
            
            if root.left is not None:
                root.left = dft(root.left, False)

            if root.right is not None:
                root.right = dft(root.right, False)

            return root
        
        dft(root, True)
        return traversal

class SolutionBFT:
    def delNodes(self, root: [TreeNode], to_delete: list[int]) -> list[int]:

        roots = set()
        queue = deque()
        queue.append((root, True))
        to_delete = set(to_delete)

        while queue:
            
            node, is_root = queue.popleft()
            
            if is_root and node.val not in to_delete:
                roots.add(node)
                
            if node.val in to_delete:
                if node.left is not None:
                    queue.append((node.left, True))
                node.left = None
                if node.right is not None:
                    queue.append((node.right, True))
                node.right = None

            else:
                if node.left is not None:
                    queue.append((node.left, False))
                    if node.left.val in to_delete:
                        node.left = None
                if node.right is not None:
                    queue.append((node.right, False))
                    if node.right.val in to_delete:
                        node.right = None

        return roots

# queue []
# root [ 1 6 7]

# curr : 7



if __name__ == '__main__':
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)
    node7 = TreeNode(7)

    node1.left  = node2
    node1.right = node3
    node2.left  = node4
    node2.right = node5
    node3.left  = node6
    node3.right = node7

    # test case 
    # nodes = [TreeNode(1,2,3), TreeNode(2,4,5), TreeNode(4), TreeNode(6), TreeNode(7)]
    # nodes = [TreeNode(1,2), TreeNode(2,4), TreeNode(4), TreeNode(6), TreeNode(7)]
    # roots = [1, 6, 7]

    # root = [1,2,3,4,5,6,7]
    to_delete = [3,5]
    # out = [[1,2,null,4],[6],[7]]
    
    solution = SolutionBFT()
    sol = solution.delNodes(node1, to_delete)
    print([root.val for root in sol])

# Copied dft solution on LeetCode https://leetcode.com/problems/delete-nodes-and-return-forest/solutions/328854/Python-Recursion-with-explanation-Question-seen-in-a-2016-interview/ 
class Solution(object):
    def delNodes(self, root, to_delete):
        to_delete = set(to_delete)
        res = []
        def walk(root, parent_exist):
            if root is None:
                return None
            if root.val in to_delete:
                root.left = walk(root.left, parent_exist=False)
                root.right = walk(root.right, parent_exist=False)
                return None
            else:
                if not parent_exist:
                    res.append(root)
                root.left = walk(root.left, parent_exist=True)
                root.right = walk(root.right, parent_exist=True)
                return root
        walk(root, parent_exist=False) 
        return res

