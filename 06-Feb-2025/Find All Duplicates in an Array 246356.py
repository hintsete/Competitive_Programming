# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

 res=[]
        count=Counter(nums)
        for key in count.keys():
            if count[key]==2:
                res.append(key)
            
        return res
