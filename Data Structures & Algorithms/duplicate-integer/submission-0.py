class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}
        size = len(nums)


        for i in range(size):
            curr = nums[i]
            check = hashmap.get(curr, 0)

            if check == 0:
                hashmap.setdefault(curr, 1)
            else:
                return True


        return False
        
        

        