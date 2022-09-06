class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        length = len(image)
        for i in range(length):
            l, r= 0, length - 1
            while l<r:
                image[i][l], image[i][r] = image[i][r],image[i][l]
                l+=1
                r-=1
        for i in range(length):
            for j in range(length):
                image[i][j] = 1 if not image[i][j] else 0
        return image
                
                
                