# Problem: Find Duplicate File in System - https://leetcode.com/problems/find-duplicate-file-in-system/

from collections import defaultdict
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
   
        content_map=defaultdict(list)
        for path in paths:
            part=path.split() 
            directory=part[0]
            for file in part[1:]:  
                file_name,content=file.split("(")
                content=content[:-1] 
                
                content_map[content].append(f"{directory}/{file_name}")
        ans=[]    
        for group in content_map.values():
            if len(group)>1:
                ans.append(group)
            
        return ans

      


        