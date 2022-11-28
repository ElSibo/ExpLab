# EXPERIMENTAL ROBOTIC LABORATORI

## Brief Introduction:

In this REDME the work done for this assignment will be explained :                                                                     
the main goal of this assigment is to create a state machine that simulates the behavior of a robot inside an indoor environment consisting of various rooms, corridors and doors .
the ontology mapping we needed to build consists of an Urgency room, where the robot goes to charge, two central corridors, and 4 rooms (2 for each corridor).

In general the robot has to keep going from room to room giving precedence to the room it saw last, for an infinite cycle; however when it passes the tresHold then in this thing it has to go into urgent to recharge, Once it finishes recharging it repositions itself in one of the corridors and starts over again.

So the assignment consists of multiple evens, which are:
1) Build an ontology map that needs to be uploaded to Armor.
2) Build a finite state machine that communicates with Armor and simulates the scenario we described above.

