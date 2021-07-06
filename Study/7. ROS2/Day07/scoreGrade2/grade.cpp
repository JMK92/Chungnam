#include <vector>
#include <stdexcept>

#include "student_info.h"
//#include "median.h"
#include "grade.h"

using std::vector;
using std::domain_error;


double grade(double midterm, double finalterm, double homework)
{
	return 0.2*midterm + 0.4*finalterm + 0.4*homework;
}

double grade(double midterm, double finalterm, const vector<double>& homeworks)
{
	if (homeworks.size()==0)
	{
		// throw 0;
		throw domain_error("students didn't any homework");
	}

	//return grade(midterm, finalterm, median(homeworks));
	return grade(midterm, finalterm, average(homeworks));
}

/*
double grade(const Student_info& student)
{
	return grade(student.midterm, student.finalterm, student.homeworks);
}*/
