# Problem: Divide Players Into Teams of Equal Skill - https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
       
      skill.sort()  
      sum_skills=sum(skill)
      size=len(skill)
      if sum_skills % (size//2)!=0:
        return -1
      target=sum_skills//(size//2)
      
      chemistry=0
      left=0
      right=size-1
      while left<right:
        if skill[left]+skill[right]!=target:
            return -1
        
        chemistry+=skill[left]*skill[right]
        left+=1
        right-=1
        
        
      return chemistry