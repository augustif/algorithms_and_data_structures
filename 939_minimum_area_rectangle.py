from  math import inf
class Solution:
    def minAreaRect(self, points: list[list[int]]) -> int:
        
        def calc_area(x2, x1, y2, y1):
            return abs(x2 -x1) * abs(y2 - y1)

        points_dict = dict()
        for point in points:
            if point[0] in points_dict.keys():
                points_dict[point[0]].add(point[1])
            else:
                points_dict[point[0]] = {point[1]}
        
        area = inf

        for point_i in points:
            # take any other point as diagonal element
            for point_j in points:
                if point_i[0] != point_j[0] and point_i[1] != point_j[1]:
                    # look for third vertex: same x as point_j
                    if point_i[1] in points_dict[point_j[0]] and point_j[1] in points_dict[point_i[0]]:
                        this_area = calc_area(point_j[0], point_i[0], point_j[1], point_i[1])
                        area =this_area if  this_area < area else area
                            
        return area if area != inf+1 else 0

# time complexity: O(n^3)
# space complexity: O(n)  

