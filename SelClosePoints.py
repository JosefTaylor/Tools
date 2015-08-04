import rhinoscriptsyntax as r
import copy

def SelClosePoints():
    points = r.GetObjects("Points to search")
    tolerance = r.GetReal("Tolerance", 0.5, 0)
    sel_points = copy.copy(points)
    check = []
    search_points = copy.copy(points)
    for point in points:
        search_points.remove(point)
        if len(search_points) > 0:
            n_close = r.PointArrayClosestPoint(search_points, point)
            d = r.Distance(point, search_points[n_close])
            if d < tolerance:
                sel_points.remove(point)
                check.append(search_points[n_close])
                
    r.SelectObjects(sel_points)
    print(len(sel_points))

SelClosePoints()