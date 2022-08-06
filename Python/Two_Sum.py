#Using Hashmap
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hMap = {}
        for i,n in enumerate(nums):
            diff = target-n
            if diff in hMap:
                return [hMap[diff], i]
            hMap[n]=i
        return
      
#for loop
n = [2,7,11,15]
t = 9
for i in range(len(n)):
    for j in range(i+1,len(n)):
        if n[i]+n[j]==t:
            print([i,j])
        
        
#2-pointer
l = 0
r = len(n)-1
while l<=r:
    if n[l]+n[r]==t:
        print([l,r])
    r-=1
    if l==r:
        l+=1
        r =len(n)-1
