#include <chrono>
//#include <algorithm>
#include <functional>
#include "TeleopPub.h"

using namespace std::chrono_literals;

void TeleopPub::initMsg()
{
    this->msg_.linear.x = 0.0;
    this->msg_.linear.y = 0.0;
    this->msg_.linear.z = 0.0;

    this->msg_.angular.x = 0.0;
    this->msg_.angular.y = 0.0;
    this->msg_.angular.z = 0.0;
}

void TeleopPub::foward()
{
    this->initMsg();
    this->msg_.linear.x = 0.2;

    RCLCPP_INFO(this->get_logger(), "foward");
    this->publisher_->publish(this->msg_);
}

void TeleopPub::backward()
{
    this->initMsg();
    this->msg_.linear.x = -0.2; // 위어랑 동일

    RCLCPP_INFO(this->get_logger(), "backward");
    this->publisher_->publish(this->msg_);
}

void TeleopPub::stop()
{
    this->initMsg();    

    RCLCPP_INFO(this->get_logger(), "stop");
    this->publisher_->publish(this->msg_);
}

void TeleopPub::rotateLeft()
{
    this->initMsg();
    this->msg_.angular.z = 2.0; // 위어랑 동일


    RCLCPP_INFO(this->get_logger(), "rotateLeft");
    this->publisher_->publish(this->msg_);
}

void TeleopPub::rotateRight()
{
    this->initMsg();
    this->msg_.angular.z = -2.0; // 위어랑 동일

    RCLCPP_INFO(this->get_logger(), "rotateRight");
    this->publisher_->publish(this->msg_);
}


TeleopPub::TeleopPub()
: Node("teleop_pub")
{
    this->publisher_ = this->Node::create_publisher<geometry_msgs::msg::Twist>("/cmd_vel", 10);
    // this->timer_ = this->create_wall_timer
    //     (2000ms, std::bind(&TeleopPub::timer_callback, this));
    // this->timer_->cancel();// 타이머 사용 하지 않을거라 cancel
}

// void TeleopPub::timer_callback()
// {    
//     geometry_msgs::msg::Twist msg;

//     msg.linear.x = 2.0;
//     msg.linear.y = 0.0;
//     msg.linear.z = 0.0;

//     msg.angular.x = 0.0;
//     msg.angular.y = 0.0;
//     msg.angular.z = 1.8;

//     RCLCPP_INFO(this->get_logger(), "twist msg publishing");
//     // 콘솔창에 출력

//     this->publisher_->publish(msg);
// }