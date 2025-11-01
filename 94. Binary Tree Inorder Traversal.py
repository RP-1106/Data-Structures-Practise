# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


'''
1. If root does not exist, return empty list
2. If root exists and has left child, go to left child
3. If root exists and has no left child, print root and go to right child
'''
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        #INORDER = LEFT, ROOT, RIGHT

        '''
        #METHOD 1: USING RECURSION
        if not root:
            return []
        
        result=[]
        def dfs(root):
            if root.left:
                dfs(root.left)
            result.append(root.val)
            if not root.right:
                return 
            else:
                dfs(root.right)
                
        dfs(root)
        return result
        '''

        #METHOD 2: USING STACK
        if not root:
            return []

        result = []
        stack = []
        curr = root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            result.append(curr.val)
            curr = curr.right

        return result




            
        
