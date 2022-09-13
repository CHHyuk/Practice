#include <iostream>

void Myfunc(void)
{
	std::cout << "Myfunc(void) called" << std::endl;
}

void Myfunc(char c)
{
	std::cout << "Myfunc(char c) called" << std::endl;
}

void Myfunc(int a, int b)
{
	std::cout << "Myfunc(int a, int b) called" << std::endl;
}

int main(void)
{
	Myfunc();
	Myfunc('A');
	Myfunc(12, 13);
	return 0;
}
