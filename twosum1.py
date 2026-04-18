def twoSum(self, nums, target):
        hashmap = {}
        n = len(nums)
        for i in range(n):
            current_number = nums[i]
            number = target - current_number
            if((number) in hashmap):
                return hashmap[number],i
            hashmap[current_number] = i
