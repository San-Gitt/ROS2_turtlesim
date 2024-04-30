#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import math

class TurtleSquare(Node):
    def __init__(self):
        super().__init__('turtle_star')
        self.publisher_ = self.create_publisher(Twist, 'turtle1/cmd_vel', 10)
        self.timer_period = 0.01  # seconds
        self.timer = self.create_timer(self.timer_period, self.timer_callback)
        print("hi")
        self.timer_count_linear = 0
        self.timer_count_angular = 0
        self.linear_speed = 1.0  # adjust as needed
        self.angular_speed = 0.3  # adjust as needed
        self.side_length = 2.0  # length of each side of the square in meters
        #self.total_sides = 2
        self.current_side = 1
        #self.var = 0
        self.twist = Twist()

    def timer_callback(self):
        #print("Hello")                #timer_period
        if (self.timer_count_linear-1)*self.timer_period <(self.side_length/self.linear_speed):
            # Start moving forward
            self.timer_count_angular = 0
            self.timer_count_linear += 1
            self.twist.linear.x = self.linear_speed
            self.twist.angular.z = 0.0
        
        else :
            self.twist.linear.x = 0.0
            if (self.timer_count_angular-1)*self.timer_period < ((math.pi*144)/(180*self.angular_speed)):#(90*math.pi) /(self.angular_speed*180) :
                self.timer_count_angular += 1
                self.twist.angular.z = -self.angular_speed
            else:
                self.timer_count_linear = 0
                self.current_side += 1
        
        self.publisher_.publish(self.twist)
        if self.current_side > 5:
            #self.timer.cancel()
            quit()


def main(args=None):
    rclpy.init(args=args)
    turtle_square = TurtleSquare()
    rclpy.spin(turtle_square)
    turtle_square.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()