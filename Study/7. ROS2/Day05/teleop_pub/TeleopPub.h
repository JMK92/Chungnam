#ifndef TELEOP_PUB_H
#define TELEOP_PUB_H

#include <memory>
#include <rclcpp/rclcpp.hpp>
#include <geometry_msgs/msg/twist.hpp>

//< 진행 순서 >

// 1.  -> 단독 사용
// 이렇게 사용해도 되고 cpp 파일에 const int 로 붙여서 전역변수로 만들어줘도 됨.
// #define DIRECTION_FORWARD   1  // define은 C언어 스타일 
// #define DIRECTION_BACKWARD  2
// #define ROTATE_LEFT         3
// #define ROTATE_RIGHT        4
// #define DIRECTION_STOP      5

// 2.  -> Teleop_pub.cpp 1번과 같이 사용
// // cpp파일에서 사용할려면 extern 선언해주어야 사용가능함, 
// extern const int DIRECTION_FORWARD; 
// extern const int DIRECTION_BACKWARD; 
// extern const int ROTATE_LEFT;      
// extern const int ROTATE_RIGHT;      
// extern const int DIRECTION_STOP;    

class TeleopPub : public rclcpp::Node {
public:
    TeleopPub();

    void move(int operation);

    //void foward();
    //void backward();
    //void stop();
    //void rotateLeft();
    //void rotateRight();

    // 3.   -> Teleop_pub.cpp 2번과 같이 사용
    // 전역변수인데 특정 클래스랑 연관 잇으면 static으로 만들어줌
    static const int DIRECTION_FORWARD; 
    static const int DIRECTION_BACKWARD; 
    static const int ROTATE_LEFT;      
    static const int ROTATE_RIGHT;      
    static const int DIRECTION_STOP; 

private:    
    static const double MAX_SPEED;
    static const double MAX_RADIAN;

    static const double STEP_SPEED;
    static const double STEP_RADIAN;

    rclcpp::Publisher<geometry_msgs::msg::Twist>::SharedPtr publisher_;
    //rclcpp::TimerBase::SharedPtr timer_;

    geometry_msgs::msg::Twist msg_;  // 멤버변수로 사용

    void initMsg();       

    //void timer_callback();
};

#endif