class Solution:    
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
      ''' Optimal solving with O(n+m) instead of O(n*m) using monotonic stack'''
      dic = {}
      for i in range(len(nums1)):
        dic[nums1[i]] = i
        
      res = [-1] * len(nums1)
      stack = []
      
      for i in range(len(nums2)):
        while stack and nums2[i] > stack[-1]:
          last_el = stack.pop() 
          res[dic[last_el]] = nums2[i]
        if nums2[i] in dic.keys():
          stack.append(nums2[i])  
      return res
        

#  Reversed array 
#     dic = {}
#     for i in range(len(nums1)):
#       dic[nums1[i]] = i

#     res = [-1] * len(nums1)
#     stack = []

#     for i in range(len(nums2)-1, -1, -1):
#       if nums2[i] in dic.keys():
#         while stack:
#           last_el = stack.pop()
#           if last_el > nums2[i]: 
#             res[dic[nums2[i]]] = last_el
#             stack.append(last_el)
#             break
#       stack.append(nums2[i])

#     return res

    
    
    
    