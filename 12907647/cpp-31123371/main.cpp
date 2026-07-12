#include<iostream>
#include<cmath>
using namespace std;
int main(){
	cout << "Please input two numbers请输入两个数字，输入一个回车一下" << endl;
	int n1,n2;
	cin >> n1 >> n2;
	cout << "+:  " << n1 + n2 << endl;
	cout << "-:  " << n1 - n2 << endl;
	cout << "*:  " << n1 * n2 << endl;
	cout << "/:  " << n1 * 1.0 / n2 << endl;
	cout << "pow n1:  " << pow(n1,2) << endl;
	cout << "pow n2:  " << pow(n2,2) << endl;
	cout << "sqrt n1:  " << sqrt(n1) << endl;
	cout << "sqrt n2:  " << sqrt(n2) << endl;
	cout << "n3(求勾股定理第三遍的长度):  " << sqrt(pow(n1,2)+pow(n2,2)) << endl;
	cout << "(n1+n2)/2:  " << (n1+n2)*1.0/2 << endl << endl;
	cout << "thank for your using!886!谢谢使用，886！" << endl;
	return 0; 
}