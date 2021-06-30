#include <chrono>
//#include <algorithm>
#include <functional>
#include "TeleopTurtle.h"

using namespace std::chrono_literals;


TeleopTurtle::TeleopTurtle()
    : Node("teleop_pub")
{
    this->publisher_ = this->Node::create_publisher<geometry_msgs::msg::Twist>("/turtle1/cmd_vel", 10);
    this->timer_ = this->create_wall_timer
        (2000ms, std::bind(&TeleopTurtle::timer_callback, this));
}

void TeleopTurtle::timer_callback()
{
    //geometry_msgs::msg::Twist msg = {{2.0, 0.0, 0.0}, {0.0, 0.0, 1.8}};

    geometry_msgs::msg::Twist msg;

    msg.linear.x = 2.0;
    msg.linear.y = 0.0;
    msg.linear.z = 0.0;

    msg.angular.x = 0.0;
    msg.angular.y = 0.0;
    msg.angular.z = 1.8;

    RCLCPP_INFO(this->get_logger(), "twist msg publishing");
    // 콘솔창에 출력

    this->publisher_->publish(msg);
}