# Problem: Gas Station - https://leetcode.com/problems/gas-station/

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas)<sum(cost):
            return -1
        diff=0
        start_idx=0
        for i in range(len(gas)):
            diff+=gas[i]-cost[i]
            if diff<0:
                start_idx=i+1
                diff=0
        return start_idx