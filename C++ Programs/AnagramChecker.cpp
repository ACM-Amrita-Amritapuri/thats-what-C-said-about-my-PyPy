#include <iostream>
#include<string>
using namespace std;

int isanagram(string str1,string str2)
{
	int count1[26] = {0}, count2[26] = {0}, ascii, i = 0;
	while (str1[i] != '\0')         //counting all alphabets in string 1
	{
		ascii=str1[i]-97;	//taking each character's ascii value and feeding it into the count array
		count1[ascii]+=1;	//taking into assumption that the string is made of lower case chars only.
		i++;
	}
	i = 0;
	while (str2[i] != '\0')              //counting all alphabets in string 2
	{
		ascii=str2[i]-97;
		count2[ascii]+=1;
		i++;
	}
	for (i = 0; i < 26; i++) //comparing the count of chars in both strings
	{
		if (count1[i] != count2[i])
			return 0;
	}
	return 1;
}

int main()
{

	string str1,str2;
    cout<<"Enter string 1\n";
    getline(cin,str1);
	cout<<"Enter String 2:\n";
	getline(cin,str2);
	
	if (isanagram(str1, str2)) //calling the anagram checking method
		printf("The strings are anagrams\n");
	else
		printf("The strings are not anagrams\n");
	return 0;
}
