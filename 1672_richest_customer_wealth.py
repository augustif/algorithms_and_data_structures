class Solution1:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        wealths = [sum(account) for account in accounts]
        return max(wealths)
    
class Solution0:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        max_wealth = 0
        for i in range(0,len(accounts)):
            i_wealth = 0
            for j in range(0,len(accounts[0])):
                i_wealth += accounts[i][j]
            if max_wealth < i_wealth:
                max_wealth = i_wealth
        return max_wealth