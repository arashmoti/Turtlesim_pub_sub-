#!/usr/bin/env python3
from first_pkg.srv import posecommand
from geometry_msgs.msg import Twist
import rospy 
rospy.init_node("publisher_node",anonymous=True)
pub=rospy.Publisher("/turtle1/cmd_vel",Twist,queue_size=1000)
list1=[0,0,0,0]
permision=False
def move():
    vel=Twist()
    vel.linear.x=list1[2]-list1[0]
    vel.linear.y=list1[3]-list1[1]
    pub.publish(vel)
ax=0
ay=0
def func(command):
    global ax,ay,permision
    ax=command.x
    ay=command.y
    list1[0]=list1[2]
    list1[1]=list1[3]
    list1[2]=ax
    list1[3]=ay
    permision=True
rospy.Service("command",posecommand,func)
r=rospy.Rate(2)
if __name__=="__main__":
    while True:
        if permision==True:
            move()
            permision=False
        print("x:{}\ny:{}\n".format(ax,ay))
        r.sleep()



