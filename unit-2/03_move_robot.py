def add_waypoint(wp, route = None):
    if route is None:
        route = []
    route.append(wp)
    return route
r1 = add_waypoint((0, 0))
r2 = add_waypoint((5, 5))
print("r1 =", r1)
print("r2 =", r2)
print("same object?", r1 is r2)