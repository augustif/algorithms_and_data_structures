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

        if not root:
            return traversal
        
        # depth first traversal
        def dft (root, is_root):
            
            if root is None:
                return None
            
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

# time complexity: O(n) where n is the number of tree nodes (each is processed once)
# space complexity: O(n) 

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
