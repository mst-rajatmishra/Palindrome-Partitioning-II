class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        
        # Step 1: Create the isPalindrome table
        isPalindrome = [[False] * n for _ in range(n)]
        
        for right in range(n):
            for left in range(right + 1):
                if s[left] == s[right] and (right - left <= 2 or isPalindrome[left + 1][right - 1]):
                    isPalindrome[left][right] = True
        
        # Step 2: Create the dp array
        dp = [0] * n
        
        for i in range(n):
            if isPalindrome[0][i]:
                dp[i] = 0
            else:
                min_cuts = float('inf')
                for j in range(i):
                    if isPalindrome[j + 1][i]:  # Check if s[j+1:i+1] is a palindrome
                        min_cuts = min(min_cuts, dp[j] + 1)
                dp[i] = min_cuts
        
        return dp[-1]  # The minimum cuts for the whole string

# Example usage:
sol = Solution()
print(sol.minCut("aab"))  # Output: 1
print(sol.minCut("a"))     # Output: 0
print(sol.minCut("ab"))    # Output: 1
