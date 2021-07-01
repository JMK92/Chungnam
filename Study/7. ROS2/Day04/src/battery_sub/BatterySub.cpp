#include "BatterySub.h"
//#include <algorithm>
#include <functional>
//#include <string>

using std::placeholders::_1;

//using namespace std::chrono_literals;
    
BatterySub::BatterySub() 
    : Node("battery_sub")
{
    this->subscriptor_ = 
        this->Node::create_subscription<sensor_msgs::msg::BatteryState>
        ("/battery_state", 10, std::bind(&BatterySub::msg_callback, this, _1));
        // 10 - qos(quality of service 신뢰성)
}


void BatterySub::msg_callback(const sensor_msgs::msg::BatteryState::SharedPtr msg) const
{
    double voltage = msg->voltage;
    double percentage = msg->percentage;
    RCLCPP_INFO(this->get_logger(), 
        "current percentage : %.2f \t current volt : %.2f", voltage, percentage);
}

