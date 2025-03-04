# Problem: Two City Scheduling - https://leetcode.com/problems/two-city-scheduling/

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        ans=[]
        difference=defaultdict(list)
        for i in range(len(costs)):
          
                difference[costs[i][1]-costs[i][0]].append(costs[i])
        keys=list(difference.keys())
        # for key in difference:
        #     keys.append(key)
        print(keys)
        keys.sort()
        print(keys)
        half=len(costs)//2
        count_a=0
        count_b=0

        for key in keys:
            for cost in difference[key]:
                if count_b<half:
                    ans.append(cost[-1])
                    count_b+=1
                else:
                    ans.append(cost[0])
                    count_a+=1
       
        return sum(ans)
        