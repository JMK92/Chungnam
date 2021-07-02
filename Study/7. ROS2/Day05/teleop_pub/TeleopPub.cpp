#include <chrono>
//#include <functional>
#include "TeleopPub.h"
#include<algorithm>

using std::min;
using std::max;


// 1.
// 전역변수 앞에 Teleop_pub 2번과 같이 사용
// const int DIRECTION_FORWARD  = 1;
// const int DIRECTION_BACKWARD = 2;
// const int ROTATE_LEFT        = 3;
// const int ROTATE_RIGHT       = 4;
// const int DIRECTION_STOP     = 5;

// 2.
// private에 넣었기 때문에
const int TeleopPub::DIRECTION_FORWARD  = 1;
const int TeleopPub::DIRECTION_BACKWARD = 2;
const int TeleopPub::ROTATE_LEFT        = 3;
const int TeleopPub::ROTATE_RIGHT       = 4;
const int TeleopPub::DIRECTION_STOP     = 5;

const double TeleopPub::MAX_SPEED = 0.22;
const double TeleopPub::MAX_RADIAN = 2.84;

const double TeleopPub::STEP_SPEED = 0.02;
const double TeleopPub::STEP_RADIAN = 0.1;

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

void TeleopPub::move(int operation)
{
    //this->initMsg();
    switch(operation){
    case DIRECTION_FORWARD:
        // this->msg_.linear.x += 0.02;
        // if(this->msg_.linear.x > TeleopPub::MAX_SPEED)
        //     this->msg_.linear.x = TeleopPub::MAX_SPEED;
        this->msg_.linear.x = min(TeleopPub::MAX_SPEED, this->msg_.linear.x + STEP_SPEED);
        RCLCPP_INFO(this->get_logger(), "Forward");
        break;
    case DIRECTION_BACKWARD:
        // this->msg_.linear.x += -0.02;
        // if(this->msg_.linear.x < -TeleopPub::MAX_SPEED)
        //     this->msg_.linear.x = -TeleopPub::MAX_SPEED;
        this->msg_.linear.x = max(-TeleopPub::MAX_SPEED, this->msg_.linear.x - STEP_SPEED);
        RCLCPP_INFO(this->get_logger(), "Backward");
        break;
    case ROTATE_LEFT:
        // this->msg_.angular.z += 0.2;
        // if(this->msg_.angular.z > TeleopPub::MAX_RADIAN)
        //     this->msg_.angular.z = TeleopPub::MAX_RADIAN;
        this->msg_.angular.z = min(TeleopPub::MAX_RADIAN, this->msg_.angular.x + STEP_RADIAN);
        RCLCPP_INFO(this->get_logger(), "Rotate_Left");
        break;
    case ROTATE_RIGHT:
        // this->msg_.angular.z += -0.2;
        // if(this->msg_.angular.z < -TeleopPub::MAX_RADIAN)
        //     this->msg_.angular.z = -TeleopPub::MAX_RADIAN;
        this->msg_.angular.z = max(-TeleopPub::MAX_RADIAN, this->msg_.angular.x - STEP_RADIAN);
        RCLCPP_INFO(this->get_logger(), "Rotate_Right");
        break;
    
    case DIRECTION_STOP: 
        this->initMsg();       
        break;
    }   
    
    this->publisher_->publish(this->msg_);
}

// void TeleopPub::stop()
// {
//     this->initMsg();    

//     RCLCPP_INFO(this->get_logger(), "stop");
//     this->publisher_->publish(this->msg_);
// }

// void TeleopPub::backward()
// {
//     this->initMsg();
//     this->msg_.linear.x = -0.2; // 위어랑 동일

//     RCLCPP_INFO(this->get_logger(), "backward");
//     this->publisher_->publish(this->msg_);
// }



// void TeleopPub::rotateLeft()
// {
//     this->initMsg();
//     this->msg_.angular.z = 2.0; // 위어랑 동일


//     RCLCPP_INFO(this->get_logger(), "rotateLeft");
//     this->publisher_->publish(this->msg_);
// }

// void TeleopPub::rotateRight()
// {
//     this->initMsg();
//     this->msg_.angular.z = -2.0; // 위어랑 동일

//     RCLCPP_INFO(this->get_logger(), "rotateRight");
//     this->publisher_->publish(this->msg_);
// }


TeleopPub::TeleopPub()
: Node("teleop_pub")
{
    this->publisher_ = this->Node::create_publisher<geometry_msgs::msg::Twist>("/cmd_vel", 10);
    // this->timer_ = this->create_wall_timer
    //     (2000ms, std::bind(&TeleopPub::timer_callback, this));
    // this->timer_->cancel();// 타이머 사용 하지 않을거라 cancel
    this->initMsg();
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