class Solution(object):
    def hasValidPath(self, grid):
        m=len(grid);
        n=len(grid[0]);
        self.res=False;
        def func(r,c,s):
            if(r>=m or c>=n):
                return;
            if((r,c) in s):
                return;
            s.add((r,c))
            if(r==m-1 and c==n-1):
                self.res=True;
                return;
            if(grid[r][c]==1):
                if( c+1<n and (grid[r][c+1]==3 or grid[r][c+1]==5 or grid[r][c+1]==1)):
                    func(r,c+1,s);
                if(c-1>=0 and (grid[r][c-1]==1 or grid[r][c-1]==4 or grid[r][c-1]==6)):
                    func(r,c-1,s);
            if(grid[r][c]==2 ):
                if( r+1<m and (grid[r+1][c]==5 or grid[r+1][c]==6 or grid[r+1][c]==2)):
                    func(r+1,c,s);
                if(r-1>=0 and (grid[r-1][c]==2 or grid[r-1][c]==3 or grid[r-1][c]==4)):
                    func(r-1,c,s);
            if(grid[r][c]==3 ):
                if( r+1<m and (grid[r+1][c]==2 or grid[r+1][c]==5 or grid[r+1][c]==6)):
                    func(r+1,c,s);
                if(c-1>=0 and (grid[r][c-1]==1 or grid[r][c-1]==4 or grid[r][c-1]==6)):
                    func(r,c-1,s)
            if(grid[r][c]==4  ):
                if(r+1<m and (grid[r+1][c]==2 or grid[r+1][c]==5 or grid[r+1][c]==6)):
                    func(r+1,c,s);
                if(c+1<n and (grid[r][c+1]==1 or grid[r][c+1]==3 or grid[r][c+1]==5)):
                    func(r,c+1,s);
            if(grid[r][c]==5  ):
                if(r-1>=0 and (grid[r-1][c]==2 or grid[r-1][c]==3 or grid[r-1][c]==4)):
                    func(r-1,c,s);
                if(c-1>=0 and (grid[r][c-1]==1 or grid[r][c-1]==4 or grid[r][c-1]==6)):
                    func(r,c-1,s);
            if(grid[r][c]==6  ):
                if(c+1<n and (grid[r][c+1]==1 or grid[r][c+1]==3 or grid[r][c+1]==5)):
                    func(r,c+1,s)
                if(r-1>=0 and (grid[r-1][c]==2 or grid[r-1][c]==3 or grid[r-1][c]==4)):
                    func(r-1,c,s)
        func(0,0,set());
        return self.res

        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        