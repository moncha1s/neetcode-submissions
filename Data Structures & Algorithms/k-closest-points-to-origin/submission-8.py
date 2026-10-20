import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # calculate squared dist from the points to the input
        dists = []
        output = []

        # creats the heap of the distances, but not the actual ordering of points
        for i, point in enumerate(points):
            x = point[0]
            y = point[1]
            euclid = math.sqrt( (x - 0)**2 + (y - 0)**2)
            # add the distance and index in points
            dist = (euclid, point)
            dists.append(dist)

        heapq.heapify(dists)
        print(dists)
        for i in range(k):
            # grab the index of top point
           output.append(heapq.heappop(dists)[1])


        return output