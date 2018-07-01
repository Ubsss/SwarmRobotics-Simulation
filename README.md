# SwarmRobotics-Simulation

Master Goal:
Attempting to build a simulation for Swarm robotics using Turtle library in Python

Sub goals:
1.	Individual robots follow each other 
2.	All the bots search for an object and converge on it when found
3.	Bots form a shape
4. Bots chase a player

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