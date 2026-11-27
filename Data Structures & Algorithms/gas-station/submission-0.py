class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
        input: list of integers contain gas, list of integers
        containing cost 
        output: index that you should start at such that you can
        visit every gas station in gas (circular)
        constraints: 
        - can only start at a gas station if gas[i] > cost[i] 
        - can go from one gas station to another if current gas
        > cost[i] 
        - going from on station (i) to another (j): tank = current
        gas - cost[i] + cost[j]
        brute force:  start at every possible index and simulate 
        the entire run. O(n^2)
        """ 
        if sum(gas) < sum(cost):
            return -1 

        res = total = 0 

        for i in range(len(gas)): 
            total += (gas[i] - cost[i])

            if total < 0:
                total = 0
                res = i + 1 
        
        return res

        