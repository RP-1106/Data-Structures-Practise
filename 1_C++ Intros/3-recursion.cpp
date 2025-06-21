#include <iostream>

int factorial(int);

int main()
{
	int num=4;
	int result = factorial(num);
	std::cout << "Factorial of " << num << "is : " << result;
	return 0;
}

int factorial(int n)
{
	if (n>1){
		return n * factorial(n-1);
	} else {
		return 1;
	}
}
