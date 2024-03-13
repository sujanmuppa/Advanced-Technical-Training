class Solution:
    def matrixDiagonally(self,mat):
        # code here
        n = len(mat)
        result = [mat[0][0]]
        change = 0
        i = 0
        j = 0
        while i != n and j != n:
            if change == 0:
                if j+1 < n:
                    j+=1
                    result += [mat[i][j]]
                    while i+1 < n and j-1 >= 0:
                        i += 1
                        j -= 1
                        result += [mat[i][j]]
                    change = 1
                    print(result)
                else:
                    change = -1
                
            elif change == 1:
                if i+1 < n:
                    i+=1
                    result += [mat[i][j]]
                    while i-1 >= 0 and j+1 < n:
                        i-=1
                        j+=1
                        result += [mat[i][j]]
                    change = 0
                    print(result)
                else:
                    change = -2
            elif change == -1:
                if i+1 < n:
                    i+=1
                    result += [mat[i][j]]
                    while i+1 < n and j-1 >= 0:
                        i += 1
                        j -= 1
                        result += [mat[i][j]]
                    change = -2
                    print(result)
            elif change == -2:
                if j+1 < n:
                    j+=1
                    result += [mat[i][j]]
                    while i-1 >= 0 and j+1 < n:
                        i-=1
                        j+=1
                        result += [mat[i][j]]
                    change = -1
                    print(result)
            if i == n-1 and j == n-1:
                break
        return result


# A Test Case:
mat = [[1,2,3],[4,5,6],[7,8,9]]
sol = Solution()
print(sol.matrixDiagonally(mat))