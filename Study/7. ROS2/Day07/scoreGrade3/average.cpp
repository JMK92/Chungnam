#include<vector>
#include"average.h"

using std::vector;

double average(const vector<double>& vec)
{
	
	double sum = 0.0;
	for (vector<double>::size_type i = 0; i != vec.size(); ++i)
		sum += vec[i];

	return sum / vec.size();
}
