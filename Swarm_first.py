#!/usr/bin/env python3

import math
import rospy
import turtlesim.msg 
from geometry_msgs.msg import Twist
rospy.init_node("pub6",anonymous=True)
def publisher():
    pub =rospy.Publisher("/turtle1/cmd_vel",Twist,queue_size=1000)
    pose=Twist()
    r=rospy.Rate(10)
    c=0
    while True:
        c+=1
        if c==100:
            break
        
        else:

            pose.linear.x=1
            pose.linear.y=0
            pose.angular.z=0.25*(math.pi)
            pub.publish(pose)
            print(x,y)
            r.sleep()




x=0
y=0

def position(data):
    global x
    global y
    x=data.x
    y=data.y

    





rospy.Subscriber("/turtle1/pose",turtlesim.msg.Pose,position)





c=0


r=rospy.Rate(1)
if __name__ == "__main__" :
    publisher()
    


    
    

        

    
        