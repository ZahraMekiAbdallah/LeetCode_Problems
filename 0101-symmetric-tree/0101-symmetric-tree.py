class Solution:

    # BFS     
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
      if not root:
        return True
      
      q = deque([root])
      
      while q:
        temp = []
        for i in range(len(q)):
          node = q.popleft()
          if node.left:
            temp.append(node.left.val)
            q.append(node.left)
          else:
            temp.append(None)
          if node.right:
            temp.append(node.right.val)
            q.append(node.right)
          else:
            temp.append(None)
            
        mid = len(temp) // 2
        if temp[:mid] != temp[mid:][::-1]: # compare first part with the reversed second part 
          return False
      return True
    
    # DFS
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
      def dfs(left, right):
        if not left and not right:
          return True
        
        if not left or not right:
          return False
        
        return(left.val == right.val and dfs(left.left, right.right) and dfs(left.right, right.left))
        
      return dfs(root.left, root.right)
          