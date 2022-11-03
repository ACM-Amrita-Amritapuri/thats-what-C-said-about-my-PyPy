#include <fstream>
#include <iostream>
#include <cstring>
using namespace std;
class Person{
    char name[20];
    long phone;
public:
    Person(){}
    Person(char n[20],long ph){
        strcpy(name,n);phone=ph;
    }
    void setName(char n[20]){strcpy(name,n);}
    void setPhone(long num){phone=num;}
    const char* getName(){return name;}
    long getPhone(){return phone;}
    void display(){cout<<name<<"  "<<phone;}

};
int main () {
   char name[20];
   long number;
   Person p1,p2,p3;
   int res;
   // open a file in write mode.
   ofstream outfile;
   outfile.open("D:\\cpp\\s.txt");
   while(1){

   cout << "Enter your name";
   cin>>name;
   cout<<"enter number";
   cin>>number;
   //cin.getline(name,20);
   //cin.ignore();
   //cin.getline(number,10);
   p1.setName(name);
   p1.setPhone(number);

   // write inputted data into the file.
  //  statement to write a person object to a file
   outfile.write((char*)&p1,sizeof(Person));

    p1.display();
   cout<<"continue(0\1)";
   cin>>res;
   if(res==0)break;
   }
    outfile.close();


   //cin.ignore();

   // open a file in read mode.
   ifstream infile;
   infile.open("D:\\cpp\\s.txt");
   cout<<"enter name to be searched";
   cin>>name;
    while(1){
        infile.read((char*)&p3,sizeof(Person));
        if(infile.eof())break;
        if((strcmp(p3.getName(),name))==0)  //compare name and display number
            p3.display();

    }

   // close the opened file.
   infile.close();

   return 0;
}
