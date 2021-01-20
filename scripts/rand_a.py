#!/usr/bin/env python3
#license:BSD-3-Clause-License
#Copyright (c) 2020, Shinnosuke Tamai & Ryuichi Ueda.
#All rights reserved.                                                                                                                                                          
import rospy
import random
import string
from std_msgs.msg import Int32

rospy.init_node("prac")
pub = rospy.Publisher('prac_up', Int32, queue_size=1)
dat = string.ascii_lowercase#+string.ascii_uppercase

T1 = 0
T2 = 0
NOT = 0
while NOT < 10:
    NOT += 1
    dat1=''.join([random.choice(dat) for i in range(6)])
    print(dat1)
    ans = input("GO!:")


    if dat1 == ans :
        print("True")
        T1 += 1
    else :
        print("False")
        T2 += 1


print("finsh! true:", T1," number of times:", NOT)
