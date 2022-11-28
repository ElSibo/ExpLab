# EXPERIMENTAL ROBOTIC LABORATORI



  <p align="center">
 
  <img src="Diagrams_Pictures/expLAB.jpeg" width="650" title="hover text">
</p>

## 1) -Brief Introduction:

In this REDME the work done for this assignment will be explained :                                                                     
the main goal of this assigment is to create a state machine that simulates the behavior of a robot inside an indoor environment consisting of various rooms, corridors and doors .
the ontology mapping we needed to build consists of an Urgency room, where the robot goes to charge, two central corridors, and 4 rooms (2 for each corridor).

In general the robot has to keep going from room to room giving precedence to the room it saw last, for an infinite cycle; however when it passes the tresHold then in this thing it has to go into urgent to recharge, Once it finishes recharging it repositions itself in one of the corridors and starts over again.

So the assignment consists of multiple evens, which are:
1) Build an ontology map that needs to be uploaded to Armor.
2) Build a finite state machine that communicates with Armor and simulates the scenario we described above.

## 2) -Software Architecture, Temporal Diagrams and State Diagrams:

### Software Architecture:

 <p align="center">
 
  <img src="Diagrams_Pictures/Schermata 2022-11-27 alle 11.28.58.png" width="750" title="hover text">
</p>

The following diagram shows the software architecture of the assignment solution, as we can see the state machine communicates with Armor with 5 messages.

The state machine can be schematized into three states which are the Planer Action, the Rooms and the Urgent.

#### These three states keep communicating with Armor to perform their tasks:

1) The Planer Action state asks Armor if there are any rooms in with the UERGENT flag, in case of a positive answer it sends the robot to the Urgent state, in case of a negative answer it asks Armor the "visitedAt" value of all the rooms and takes the maximum among them (i.e. the room it has not visited for the longest time), based on this condition it sends the planer one of the rooms.

2) The Room state (we have described this general state reflecting all the states referred to the rooms) on the other hand asks Armor where the robot is through "isIn", then makes it move to one of the two corridors depending on which room the state is referred to (C1 if they are rooms R1 and R2, and C2 if they are rooms R3 and R4) by changing the value of "isIn", after which it moves the robot to the desired room and holds it for a while and eventually the robot returns to the corridor and the state returns to Planner Action.

3) The Urgent state is triggered by the planner when the values of "visitedAt " exceed the treshold, once the urgent state is triggered, it asks Armor where the robot is and places it in the room E through the "isIn" command, then it asks Armor for the value "visitedAt" and sets it the initial value (this procedure makes some time to simulate the recharging of the robot) after which the robot is spotted in a corridor again.

#### The messages that are sent and received by Armor are :

1) URGENT flag indicating how many rooms are in urgent.

2) "visitedAt" which indicates the value of the last time the room was visited(it is changed every time the robot is in the room).

3) "isIn" indicates which location the robot is in (it is changed to indicate the robot's movement)

#### The commands we used to communicate with with Armor:

1) QUERY: to query the information for "visitedAt", "isIn", "URGENCY".

2) REPLACE: to change the values for "visitedAt", "isIn", "URGENCY".

We then used then for convenience the armor_py library to call the resoner and buffer

### Temporal Diagrams:

<p align="center">
 
  <img src="Diagrams_Pictures/Schermata 2022-11-27 alle 18.36.33.png" width="750" title="hover text">
</p>

This diagram shows the time sequence of our project; bones the sequence in which the various states and Armor are called along over time.
It can be clearly understood that the proper operation of the node (which is composed of the various states of the state machine) occurs with synchronization with Armor.                                                                                               
In fact, there must be continuous communication with Armor, both for the Planner Action state, which must receive information from Armor to move to the correct state, and for the Room and Urgent states, which must receive information and modify the ontology in Armor.

### State Diagrams:



<p align="center">
 
  <img src="Diagrams_Pictures/Schermata 2022-11-28 alle 00.05.44.png" width="950" title="hover text">
</p>

This diagram shows the schematic of the finite state machine, the states it is composed of, and how the transition from one state to another takes place.

The finite state machine consists of a Planner Action state (which decides what state to go to), you exit the state with 'go_R1'(to go to room R1), 'go_R2'(to go to room R2), 'go_R3'(to go to room R3), 'go_R4'(to go to room R4)and with 'Urgent'(to go to Urgency), you enter the state with 'go_plan'; in the Robot_Move_to_Rx state you exit with 'go_plan' and enter with 'go_Rx'(Rx represents the individual rooms R1,R2,R3,R4); nthe URGENCY state you exit with 'go_plan and enter with 'Urgent'.

## 3) -Installation and Running procedure:

The first think to do is dowload (with: gitclone + link of github) this repository in you workspace and make a catkin_make.

For this installation procedure we have taken into account that you already have ROS installed with your work space (in case you have not done so we attach a link so you can do so) and that you also have armor already installed in your work space (in case you have not done so we attach a link so you can do so).

#### (official Raccomanded) ROS Link: https://wiki.ros.org/ROS/Installation
#### (unofficial) ROS Link: https://www.macheronte.com/installiamo-ed-eseguiamo-ros/
#### ARMOR link: https://github.com/EmaroLab/armor

Plus you must have smach and smach viwer installed to have a graphical representation of the finite state machine, they are installed with the following commands:

```console
# INSTALLATION
# - eventually install smach with 
#          $ sudo apt-get install ros-noetic-executive-smach*
# - create ROS package in your workspace:
#          $ catkin_create_pkg smach_tutorial std_msgs rospy
# - move this file to the 'smach_tutorial/scr' folder and give running permissions to it with
#          $ chmod +x state_machine.py
# - run the 'roscore' and then you can run the state machine with
#          $ rosrun smach_tutorial state_machine.py
# - eventually install the visualiser using
#          $ sudo apt-get install ros-kinetic-smach-viewer
# - run the visualiser with
#          $ rosrun smach_viewer smach_viewer.py
```

Now the first think to do is to run roscore and armor, in 2 different teriminal: 

```bsh
  # - run roscore:
          $ roscore
  # -in different terminal run armor:
          $ rosrun armor execute it.emarolab.armor.ARMORMainService
```
After that, we must build the ontological map taht we need for execute the assignmnet; and we do it with this command:
```bsh
          $ rosrun expLab Build_map.py 
```
After that, we run the State Machine, with this command:

```bsh
          $ rosrun expLab SM_assignment.py
```
If we wont to see the graphical rapresentation of the State Machine and how it work, we can use the smach_viwer for the graph, with this commnad :

```bsh
          $ rosrun smach_viewer smach_viewer.py 
```
## 4) -Video about assigment:
this video show how the state machine work and  at the left side we can see the armo and the node of the state machine comunicate with each other.

#### link: https://youtu.be/R5EBC7u4ep8

## 5) -Working hypothesis and environment:

### System’s features:

The main goal of the system is to simulate motion in a specific context (in our case it was an indoor consisting of multiple rooms and hallways) to do this we organized the work in a finite state machine that identified the most important stages of this simulation.
Generally the design is organized with a reasoner (armor) communicating with the node (SM_assigment.py) at different stages of the state machine.
The first communication is when it happens with the planner that receives information from armor; this information is decisive for the next state, which can be the movement to the rooms or the movement to the ungency (for the simulation we modify the data of the ontology map that uses the reasoner armor) and then return to the planner that will decide the new movement. 

### System’s limitations:

The limitations of this system are mainly that it is a fairly rough simulation, because it does not take into account a dimensioned area of the map, so that the robot moves not only in rooms but also by giving it a path.
Another limitation is that the robot's movement is decided by a state of the state machine and not by the resone, where we do not use its computational skills, must instead are used only to figure out whether the robot should go URGENT.

### Possible technical Improvements:

To improve our system we have to start from the limitations it has and for that I would propose to create a dimensional map of the environment (with x,y coordinates), also giving a time in the motion that will give us as a consequence the speed of the robot.
The most important improvement in my opinion is to use the potential of the reasoner by having armor decide the next state; this would be possible if we also implement rules that decision.
 
## 6) -Authors and Contacts:

#### Authors: Bouazza El Moutaouakil 
#### github: https://github.com/ElSibo
#### contacts: siboasa@gmail.com
