class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        current_wealth = 0
        for i in range(len(accounts)):
            for j in range(len(accounts[i])):
                current_wealth += accounts[i][j]
            if current_wealth > max_wealth:
                max_wealth = current_wealth
            current_wealth = 0

        return max_wealth 