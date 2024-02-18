#733
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if not image:
            return image
        
        row=len(image)
        col=len(image[0])

        oldColor=image[sr][sc]
        if oldColor==color:
            return image

        self.dfs(image,sr,sc,oldColor,color,row,col)

        return image

    def dfs(self,image,i,j,oldColor,color,row,col):

        if i<0 or j<0 or i>=row or j>=col or image[i][j]!=oldColor:
            return 

        image[i][j]=color

        self.dfs(image,i-1,j,oldColor,color,row,col)
        self.dfs(image,i+1,j,oldColor,color,row,col)
        self.dfs(image,i,j-1,oldColor,color,row,col)
        self.dfs(image,i,j+1,oldColor,color,row,col)

        