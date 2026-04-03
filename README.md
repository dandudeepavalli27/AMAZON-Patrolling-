# AMAZON-Patrolling-
Aim
To implement a waypoint-based patrol routine for continuous robot navigation.
General Objective
To understand waypoint-based navigation and autonomous patrolling strategies used for systematic area coverage.
Specific Objective
To navigate through:
5 waypoints
and repeat the cycle continuously → Continuous Patrol
Dataset
Waypoint Navigation Dataset
Source: Navigation2 (Nav2)
Procedure
Define list of waypoints
Navigate to each waypoint sequentially
Repeat the sequence in a loop
Continue patrol indefinitely
Display result
Algorithm
Start
Define waypoints
Loop through waypoints
Move to each waypoint
Repeat loop
Display result
Stop
Code Logic
for waypoint in waypoints:
    visit(waypoint)
Python Code
# SESSION 37 – Patrolling (Waypoint Navigation)

# Step 1: Define waypoints
waypoints = [(0,0), (1,2), (3,4), (5,6), (7,8)]

# Step 2: Continuous patrol loop
while True:
    for wp in waypoints:
        print("Moving to waypoint:", wp)
    
    print("Patrol cycle completed\n")
Output
Moving to waypoint: (0, 0)
Moving to waypoint: (1, 2)
Moving to waypoint: (3, 4)
Moving to waypoint: (5, 6)
Moving to waypoint: (7, 8)
Patrol cycle completed
... (repeats continuously)

Continuous Patrol
Result
The robot successfully performs:
Continuous Patrol through all waypoints
Industry Application
Patrolling systems are used in:
Security robots
Warehouse monitoring
Surveillance systems
Inspection robots
Companies like Amazon use this in:
Warehouse automation
Inventory tracking
Autonomous monitoring
Conclusion
Waypoint-based patrolling ensures systematic and continuous coverage of an area, making it essential for surveillance and monitoring tasks.
