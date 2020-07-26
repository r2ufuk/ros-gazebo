# ros-gazebo

Series of incremental improvements over a demo for ROS with Gazebo

Listing complies with video numbers:

### coke.world
1- Throw a coke can with directional force and apply torque to achieve flipping

### cart.world
* Build a simple cart with wheel pairs of different sizes

* Attach revoluting joints for wheel rotation and steering

2- (Scripted) Apply toque to the rear wheel axle and move cart forward

* Write a tele-operation script to drive cart with keyboard input

* Following demo videos are all teleoperated

3- Accelerate and decelerate to stay in frame, then show steering arm movement

4- Move cart in reverse while rotating front wheels. Show encountered abrupt behavior during development: 
   1. Steering arm rotates 360 degrees. Cause:
      1. Self-collision was not enabled
      2. Limiting rotation degrees does not physically limit anything applied from ROS
   2. Joints split apart with excessive torque. Cause:
      1. Unknown. Nothing was explicitly manipulated to cause this issue.
      
5- Enable self-collision to front wheels and steering arm to produce a more realistic sim. This reveals design errors in the cart model:
   1. Front wheels should have been placed below the chasis
   2. (Failed attempt) Place static joint bumpers behind the steering arm to stop movement. Small joints immidiately break off.
   
## TODO

* Improve steering

* Add member: [excavator | loader | claw]
