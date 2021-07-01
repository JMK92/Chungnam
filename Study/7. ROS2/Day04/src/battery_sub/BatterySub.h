#ifndef BATTERYSUB_H
#define BATTERYSUB_H

#include <memory>               // shared_pointer 쓸 때 필요함
#include <rclcpp/rclcpp.hpp>
#include <sensor_msgs/msg/battery_state.hpp>


class BatterySub : public rclcpp::Node {
public:
    BatterySub();

private:
    void msg_callback(const sensor_msgs::msg::BatteryState::SharedPtr msg) const;

    rclcpp::Subscription<sensor_msgs::msg::BatteryState>::SharedPtr subscriptor_;

};

#endif