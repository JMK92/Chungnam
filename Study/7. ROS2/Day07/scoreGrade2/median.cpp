#include<vector>
#include<stdexcept>
#include<algorithm>

#include"median.h"

using std::vector;
using std::sort;
using std::domain_error;

double median(vector<double> vec)
{
	if(vec.size() == 0) {
		throw domain_error("vector is empty");
	}
		
	sort(vec.begin(), vec.end());

	vector<double>::size_type mid = vec.size() / 2;
	
	double median 
		= ( vec.size() % 2) ? vec[mid] : (vec[mid] + vec[mid-1]) / 2;

	return median;	
}
