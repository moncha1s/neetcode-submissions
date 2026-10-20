import heapq 

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        output = []
        dists = []

        for point in points:
            x, y = point[0], point[1]
            euclid = x**2 + y**2

            if len(dists) < k:
                heapq.heappush_max(dists, (euclid, point))
            elif dists[0][0] > euclid:
                heapq.heappop_max(dists)
                heapq.heappush_max(dists, (euclid, point))


        while dists:
            output.append(heapq.heappop_max(dists)[1])                
              

        return output