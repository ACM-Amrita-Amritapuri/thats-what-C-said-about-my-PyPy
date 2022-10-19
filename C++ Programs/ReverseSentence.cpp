#include <iostream>

using namespace std;

void rev_str(char *string) 

{

   if(*string == '\0')

       return;

    else 

    {

       rev_str(string+1);

       cout<<*string;

    }

}

int main() 

{

 char string[] = "Welcome to Coding";

    cout<<"Original String: "<<string<<endl;

    cout<<"Reversed String: ";

   rev_str(string);

    return 0;

}
