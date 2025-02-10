# Problem: Flipping an Image - https://leetcode.com/problems/flipping-an-image/description/

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        output=[]
        for img in image:
            img.reverse()
        size=len(image)
        for i in range(size):
            for j in range(size):
                if image[i][j]==0:
                    image[i][j]=1
                else:
                    image[i][j]=0
            
        return image

