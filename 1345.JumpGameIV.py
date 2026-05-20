from collections import defaultdict, deque

class Solution:
    def minJumps(self, arr):
        n = len(arr)

        vis = [False] * n
        mp = defaultdict(list)

        for i in range(n):
            mp[arr[i]].append(i)

        q = deque([0])
        vis[0] = True
        cnt = 0

        while q:
            sz = len(q)

            for _ in range(sz):
                idx = q.popleft()

                if idx == n - 1:
                    return cnt

                if idx - 1 >= 0 and not vis[idx - 1]:
                    q.append(idx - 1)
                    vis[idx - 1] = True

                if idx + 1 < n and not vis[idx + 1]:
                    q.append(idx + 1)
                    vis[idx + 1] = True

                for x in mp[arr[idx]]:
                    if not vis[x]:
                        q.append(x)
                        vis[x] = True

                mp[arr[idx]] = []

            cnt += 1

        return -1