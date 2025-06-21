#include <iostream>

int fibonacci (int);

int main()
{
	int num=7;
	int result = fibonacci(num);
	std::cout << "Fibonacci of " << num << "is : " << result;
	return 0;
}

int fibonacci(int n)
{	if (n==0){ return 0; }
	else if (n==1) {return 1;}
	else{ return fibonacci(n-1) + fibonacci(n-2); }
}
