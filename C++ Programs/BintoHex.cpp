#include <iostream>
using namespace std;

int main()

{

	char bno[1000], hex[1000];

	int temp;

	long int i = 0, j = 0;

	cout << "Enter Binary Number : ";

	cin >> bno;

	while (bno[i])

	{

		bno[i] = bno[i] - 48;

		++i;
	}

	--i;

	while (i - 2 >= 0)

	{

		temp = bno[i - 3] *8 + bno[i - 2] *4 + bno[i - 1] *2 + bno[i];

		if (temp > 9)

			hex[j++] = temp + 55;

		else

			hex[j++] = temp + 48;

		i = i - 4;
	}

	if (i == 1)

		hex[j] = bno[i - 1] *2 + bno[i] + 48;

	else if (i == 0)

		hex[j] = bno[i] + 48;

	else

		--j;

	cout << "\nHexadecimal Number equivalent to Binary Number : ";

	while (j >= 0)

	{

		cout << hex[j--];
	}

	return 0;

}
