#include<iostream>
#include<vector>

#include "student_info.h"

using std::istream;
using std::vector;



istream& read_hw(istream& in, vector<double>& homeworks)
{
	if(in){
		homeworks.clear();

		double hw;
		while(in >> hw ){
			homeworks.push_back(hw);
		}

		in.clear();   
	}
	return in;
}



istream& read(istream& in, Student_info& student)
{
	in >> student.name >> student.midterm >> student.finalterm;
	
	read_hw(in, student.homeworks);	

	return in;
}

bool compare(const Student_info& s1, const Student_info& s2)
{
	return s1.name < s2.name;

}

