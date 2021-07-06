#include<iostream>
#include<vector>
#include"median.h"
#include "student_info.h"
#include "grade.h"
using std::istream;
using std::vector;

istream& read_hw(istream& in, vector<double>& homeworks)
{
	if (in) {
		homeworks.clear();				// 벡터 비움
	
		double hw;
		while (in >> hw) {
			homeworks.push_back(hw);
		}

		in.clear();			
	// 숙제를 몇개 받을지 모르고, (여러명의 학생을 받을 때) 두번째줄에 이름을 받는데, 그때 더블형이 되어있어서
	// cin내부적으로 오류가 생김 (이름은 스트링인데, 더블로 되어있어서),, 그래서 클리어 해줌,,,

	}
	return in;
}

istream& read(istream& in, Student_info& student)
{
	double midterm;
	double finalterm;
	vector<double> homeworks;
	

	in >> student.name >>midterm >> finalterm;
	read_hw(in, homeworks);	
	
	if(in)
		student.finalScore = grade(midterm, finalterm, homeworks);
	return in;
}

bool compare(const Student_info& s1, const Student_info& s2)
{
	return s1.name < s2.name;

}

