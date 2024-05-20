# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def largestValues(self, root):
        if root is None : return []

        heights = collections.defaultdict(list)

        def recursion(node, height):
            if node is None: return height - 1
            
            heights[height].append(node.val)
            
            return max(height, recursion(node.right, height + 1), recursion(node.left, height + 1))

        treeHeight = recursion(root, 0)

        res = []
        for i in range(treeHeight + 1):
            res.append(max(heights[i]))

        return res
