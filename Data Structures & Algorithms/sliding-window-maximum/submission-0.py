class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque

class Solution:
    def maxSlidingWindow(self, nums, k):
        q = deque()
        ans = []

        for i in range(len(nums)):
            # Remove elements outside window
            if q and q[0] <= i - k:
                q.popleft()

            # Maintain decreasing order
            while q and nums[q[-1]] <= nums[i]:
                q.pop()

            q.append(i)

            # Add maximum of current window
            if i >= k - 1:
                ans.append(nums[q[0]])

        return ans

        