# SwarmRobotics-Simulation
Purpose statement:
Swarm robotics is a new approach to the coordination of multiple robots as a system which consists of a large number of 
simple physical robots. It is supposed that a desired collective behavior emerge from the interaction between the robots
 and the interface of the robots with the environment.
 
Master Goal:
Attempting to build a simulation for Swarm robotics using Turtle library in Python

Sub goals:
1.	Follow the master (all bots follow one) 
2.	Find an object (all bots search for an object in a specific area)
3.	obstacle avoidance (all bots navigate an obstacle course)
4.  line follow (all bots follow the line)


Setup:
1.	Create the environment 
2.	Create bots
3.	Create movement logic for the bots
4.	Create proximity and orientation algorithms 

Situational Awareness:
1. Create a class that allows for situational awareness
    a. create a method for distance sensor at every 45 degrees around an object (8 distance measurements)
    b. create a method for a buffer distance that works best (about 20 on all 8 axises)
    c. incorporate the ability to sense when the set buff is reduced

Notes:
    - link: https://stackoverflow.com/questions/43440399/make-one-python-turtle-chase-another-turtle
        * how to make a turtle follow another

    - follow the master:
        * When the main bot hits the enemy, the enemy hides and reappears behind the main bot and follows its direction