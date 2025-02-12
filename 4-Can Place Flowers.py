class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if flowerbed[0]==0:
            flowerbed[0]=1
            n-=1
        for i in range(len(flowerbed)-1):
            if flowerbed[i]!=1 and (flowerbed[i-1]==0 and flowerbed[i+1]==0):
                flowerbed[i]=1
                n-=1
        return n<1


