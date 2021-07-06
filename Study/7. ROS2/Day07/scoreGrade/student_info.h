#ifndef STUDENT_INFO_H
#define STUDENT_INFO_H

#include <string>
#include<string>
#include <vector>

struct Student_info{
	std::string name;
	double midterm;
	double finalterm;
	std::vector<double> homeworks;

	
};

std::istream& read(std::istream& in, Student_info& student);
std::istream& read_hw(std::istream& in, std::vector<double>& homeworks);

bool compare(const Student_info& s1, const Student_info& s2);

#endif
