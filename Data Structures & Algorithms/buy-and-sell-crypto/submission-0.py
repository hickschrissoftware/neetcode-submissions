class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0 # Buy pointer (represents the lowest price seen so far)
        right = 1 # Sell pointer (exploring current prices)
        max_profit = 0

        while right < len(prices):
            # Check if we found a profitable transaction
            if prices[left] < prices[right]:
                current_profit = prices[right] - prices[left]
                max_profit = max(max_profit, current_profit)
            else:
                # If prices[right] is lower than prices[left],
                # we found a new cheaper buy day! Shift left pointer there.
                left = right

            # Always move the right pointer forward to check the next day
            right += 1

        return max_profit