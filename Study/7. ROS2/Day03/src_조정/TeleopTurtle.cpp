#include <chrono>
//#include <algorithm>
#include <functional>
#include "TeleopTurtle.h"

using namespace std::chrono_literals;

void TeleopTurtle::initMsg()
{
    this->msg_.linear.x = 0.0;
    this->msg_.linear.y = 0.0;
    this->msg_.linear.z = 0.0;

    this->msg_.angular.x = 0.0;
    this->msg_.angular.y = 0.0;
    this->msg_.angular.z = 0.0;
}

void TeleopTurtle::foward()
{
    this->initMsg();
    this->msg_.linear.x = 2.0;

    RCLCPP_INFO(this->get_logger(), "twist msg publishing");
    this->publisher_->publish(this->msg_);
}

void TeleopTurtle::backward()
{
    // geometry_msgs::msg::Twist msg;

    // msg.linear.x = -2.0;
    // msg.linear.y = 0.0;
    // msg.linear.z = 0.0;

    // msg.angular.x = 0.0;
    // msg.angular.y = 0.0;
    // msg.angular.z = 0.0;

    this->initMsg();
    this->msg_.linear.x = -2.0; // 위어랑 동일

    RCLCPP_INFO(this->get_logger(), "twist msg publishing");
    this->publisher_->publish(this->msg_);
}

void TeleopTurtle::rotateLeft()
{
    // geometry_msgs::msg::Twist msg;

    // msg.linear.x = 0.0;
    // msg.linear.y = 0.0;
    // msg.linear.z = 0.0;

    // msg.angular.x = 0.0;
    // msg.angular.y = 0.0;
    // msg.angular.z = 2.0;
    this->initMsg();
    this->msg_.angular.z = 2.0; // 위어랑 동일


    RCLCPP_INFO(this->get_logger(), "twist msg publishing");
    this->publisher_->publish(this->msg_);
}

void TeleopTurtle::rotateRight()
{
    // geometry_msgs::msg::Twist msg;

    // msg.linear.x = 0.0;
    // msg.linear.y = 0.0;
    // msg.linear.z = 0.0;

    // msg.angular.x = 0.0;
    // msg.angular.y = 0.0;
    // msg.angular.z = -2.0;
    this->initMsg();
    this->msg_.angular.z = -2.0; // 위어랑 동일

    RCLCPP_INFO(this->get_logger(), "twist msg publishing");
    this->publisher_->publish(this->msg_);
}


TeleopTurtle::TeleopTurtle()
    : Node("teleop_pub")
{
    this->publisher_ = this->Node::create_publisher<geometry_msgs::msg::Twist>("/turtle1/cmd_vel", 10);
    this->timer_ = this->create_wall_timer
        (2000ms, std::bind(&TeleopTurtle::timer_callback, this));
    this->timer_->cancel();// 타이머 사용 하지 않을거라 cancel
}

void TeleopTurtle::timer_callback()
{    
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