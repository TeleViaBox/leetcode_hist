
# STATUS: TLE
# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         ans = float("-inf")
#         for i in range(len(nums)):
#             s = nums[i]
#             if s > ans:
#                 ans = s
#             # print(ans, "ans", s, "s")
#             for j in range(i+1, len(nums)):
#                 # print("max", nums(len(nums))) FAIL!
#                 s = s + nums[j]
#                 if s > ans:
#                     ans = s
#             #     print(ans, "ans2", s, "s2")
#             # print(ans, "ANS", s, "S")
#         return ans                    
            
        
#         m = float("-inf")
        
#         ans = nums[0]
#         for idx in range(0, len(nums)-1):
#             temp = nums[idx]
#             if ans < temp:
#                 ans = temp
#             for i in range(0, ):
#                 if ans < (ans + nums[idx+]):
#                     ans = ans + nums[idx+1]
                
            

            

#         # for idx in range(0, len(nums)-1):
#         #     ans = nums[idx] + nums[idx+1]
#         for idx in range(0, len(nums)-1):
#             ans = nums[idx]
#             for plus in range(0, len(nums)-1):
#                 ans = nums[idx+1]
#         for idx in range(0, len(nums)-1):
#             ans = nums[idx]
#             for plus in range(0, len(nums)-1):
#                 for 
#                 ans = nums[idx+1] + nums[idx+2]
            
#             for inner in range(0, ?):
         
        
#         1
#         2
#         3
#         x
#          x
#           x
#         xx
#          xx
#         xxx
        
    """    
    def maxSubArray(self, nums: List[int]) -> int:
        for idx in range(0, len(nums)-1):
            if num[idx]>0:
                new[i] = num[idx]
                i += 1
        if i == 0:
            return min(nums)
        for idx
    """
#     FALSE: should be contiguous!

            
            # step1:
            
#         nums {a,b,c,d,e}
# o,x,x
# o,o,x
# 
# 

# if (-): not to add
# if all are (-), return the minist one.

