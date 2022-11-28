#! /usr/bin/env python 

## @file Build_onto_map.py
# @brief In this file we are build the ontological map 
# - that we will use in the state machine of assigment
#
# @section author: 
# - CREATED by Bouazza EL Moutaouakil on 24/11/22
# @section version: 
# - version(1.0)

##  LIBRARI
# we are declared the librari tha we are need
# to do assignment
 
from armor_api.armor_client import ArmorClient
import rospy
import time 
from os.path import dirname, realpath

## CLIENT SET-UP
# we are seting the path where we wiil save  the ontologi,
# and we are creating the armor client 
# @param client define the client that talk with armor

path = dirname(realpath(__file__))
path = path + "/topological_map/"

client = ArmorClient("My_client", "My_reference")
client.utils.load_ref_from_file(path + "topological_map.owl", "http://bnc/exp-rob-lab/2022-23",True,"PELLET", False )  # initializing with buffered manipulation and reasoning

## we are informing the user
print("ADD DOOR TO THE ONTOLOGY")

## add individuals to the class DOOR (D1, ..., D7) .

client.manipulation.add_ind_to_class("D1","DOOR")
client.utils.sync_buffered_reasoner()
client.manipulation.add_ind_to_class("D2","DOOR")
client.utils.sync_buffered_reasoner()
client.manipulation.add_ind_to_class("D3","DOOR")
client.utils.sync_buffered_reasoner()
client.manipulation.add_ind_to_class("D4","DOOR")
client.utils.sync_buffered_reasoner()
client.manipulation.add_ind_to_class("D5","DOOR")
client.utils.sync_buffered_reasoner()
client.manipulation.add_ind_to_class("D6","DOOR")
client.utils.sync_buffered_reasoner()
client.manipulation.add_ind_to_class("D7","DOOR")
client.utils.sync_buffered_reasoner()

## we are informing the user
print("ADD ROOM TO THE ONTOLOGY")

##ADD INDIVIDUALS IN ROOM  R1,R2,R3,R4
client.manipulation.add_ind_to_class("R1","ROOM")
client.utils.sync_buffered_reasoner()
client.manipulation.add_ind_to_class("R2","ROOM")
client.utils.sync_buffered_reasoner()
client.manipulation.add_ind_to_class("R3","ROOM")
client.utils.sync_buffered_reasoner()
client.manipulation.add_ind_to_class("R4","ROOM")
client.utils.sync_buffered_reasoner()

## we are informing the user
print("ADD URGENT TO THE ONTOLOGY")

##ADD INDIVIDUALS IN URGENT  E
client.manipulation.add_ind_to_class("E","URGENT")
client.utils.sync_buffered_reasoner()

## we are informing the user
print("ADD CORRIDOR TO THE ONTOLOGY")

##ADD INDIVIDUAS IN CORRIDOR C1,C2
client.manipulation.add_ind_to_class("C1","CORRIDOR")
client.utils.sync_buffered_reasoner()
client.manipulation.add_ind_to_class("C2","CORRIDOR")
client.utils.sync_buffered_reasoner()

## i must dijoint the  clasees because door, location  are diferent think

client.call('DISJOINT','IND','',["D1","D2","D3","D4","D5","D6","D7"])
client.call('DISJOINT','IND','',["R1","R2","R3","R4","C2","C1","E"])

client.utils.sync_buffered_reasoner()


## Robot is in urgency room at the begining

client.call('ADD','OBJECTPROP','IND',['isIn', 'Robot1', 'C1'])
client.utils.sync_buffered_reasoner()

## we are informing the user
print("ADD Object properti to LOCATION  TO THE ONTOLOGY")

## we add a object hasDoor to the ROOM and URGENT
client.manipulation.add_objectprop_to_ind("hasDoor","E","D6")
client.utils.sync_buffered_reasoner()
client.manipulation.add_objectprop_to_ind("hasDoor","E","D7")
client.utils.sync_buffered_reasoner()
client.manipulation.add_objectprop_to_ind("hasDoor","R1","D1")
client.utils.sync_buffered_reasoner()
client.manipulation.add_objectprop_to_ind("hasDoor","R2","D2")
client.utils.sync_buffered_reasoner()
client.manipulation.add_objectprop_to_ind("hasDoor","R3","D3")
client.utils.sync_buffered_reasoner()
client.manipulation.add_objectprop_to_ind("hasDoor","R4","D4")
client.utils.sync_buffered_reasoner()

## we add a object hasDoor to the CORRIDOR C1
client.manipulation.add_objectprop_to_ind("hasDoor","C1","D1")
client.utils.sync_buffered_reasoner()
client.manipulation.add_objectprop_to_ind("hasDoor","C1","D2")
client.utils.sync_buffered_reasoner()
client.manipulation.add_objectprop_to_ind("hasDoor","C1","D5")
client.utils.sync_buffered_reasoner()
client.manipulation.add_objectprop_to_ind("hasDoor","C1","D7")
client.utils.sync_buffered_reasoner()

## we add a object hasDoor to the CORRIDOR C2
client.manipulation.add_objectprop_to_ind("hasDoor","C2","D6")
client.utils.sync_buffered_reasoner()
client.manipulation.add_objectprop_to_ind("hasDoor","C2","D3")
client.utils.sync_buffered_reasoner()
client.manipulation.add_objectprop_to_ind("hasDoor","C2","D4")
client.utils.sync_buffered_reasoner()
client.manipulation.add_objectprop_to_ind("hasDoor","C2","D5")
client.utils.sync_buffered_reasoner()

## we are informing the user
print("ADD DATAPROPERTY TO THE ONTOLOGY")

## ask to armor hoe is the value now of Robot1 and extract the info 
A = client.query.dataprop_b2_ind('now', "Robot1")
client.utils.sync_buffered_reasoner()
A =  (A[0].split('"'))[1]

## add data properti visitedAt to the ROOM equal to now of Robot1
client.call('ADD','DATAPROP','IND',['visitedAt', 'R1','Long',A])
client.utils.sync_buffered_reasoner()
client.call('ADD','DATAPROP','IND',['visitedAt', 'R2','Long',A])
client.utils.sync_buffered_reasoner()
client.call('ADD','DATAPROP','IND',['visitedAt', 'R3','Long',A])
client.utils.sync_buffered_reasoner()
client.call('ADD','DATAPROP','IND',['visitedAt', 'R4','Long',A])
client.utils.sync_buffered_reasoner()



##apply change and query

client.utils.apply_buffered_changes()
client.utils.sync_buffered_reasoner()

## we are informing the user
print("SAVE IT TO FILE .owl in: ",path)

## save in file Assignment.owl in the initil path
client.utils.save_ref_with_inferences(path + "Assignment.owl")



