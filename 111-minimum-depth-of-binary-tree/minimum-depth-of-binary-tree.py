# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        # for BFS you have to use a deque 
        # trees are not cyclable, once you visit a node you cant go back to it
        if not root:
            return 0
        
        # starting bfs from the root
        queue = deque([root])
        levels = 0

        while queue > 0:
            levels += 1 # add another level since we are going down the tree
            for i in range(len(queue)):
                node = queue.popleft()

                if not node.left and not node.right:
                    return levels # return the level if there aren't any children left

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)
            



