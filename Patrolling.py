# SESSION 37 – Patrolling (Waypoint Navigation)

# Step 1: Define waypoints
waypoints = [(0,0), (1,2), (3,4), (5,6), (7,8)]

# Step 2: Continuous patrol loop
while True:
    for wp in waypoints:
        print("Moving to waypoint:", wp)
    
    print("Patrol cycle completed\n")
