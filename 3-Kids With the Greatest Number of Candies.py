class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        out = []
        maximum = max(candies)
        for i in range(len(candies)):
            out.append(candies[i]+extraCandies>=maximum)
        return out

