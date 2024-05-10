def Solution(num: list):
    ans=0
    for i in num:
        ans^=i
    return ans

#Example 1:
print("Example 1:")
nums1=[2,2,1]
print(Solution(nums1))

#Example 2:
print("Example 2:")
nums2=[4,1,2,1,2]
print(Solution(nums2))

#Example 3:
print("Example 3:")
nums3=[1]
print(Solution(nums3))
