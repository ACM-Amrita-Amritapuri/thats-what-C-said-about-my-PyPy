#include<iostream>
using namespace std;

class stack
{
	public:
	int a[5];
	int top;
	stack()
	{
		top=-1;
	}
	void push();
	void pop();
	void display();
	void peek();
	
};

void stack::push()
{ 
	cout<<"Enter the array to be inserted:";
	top++;
	cin>>a[top];
}

void stack::pop()
{
	 if(top==-1)
	 {
		 cout<<"STACK is empty";
	 }
	 else
	 {
	   cout<<"The element has been poped: "<<a[top]<<endl;
	   top--; 
	 }	
}

void stack::display()
{	
	 int i;
	 if(top==-1)
	 {
		 cout<<"STACK is empty";
	 }
	 else
	 {
		cout<<"The  array is:";
		for(i=top;i>=0;i--)
		{
			cout<<a[i]<<" ";
		 } 
	 } 
}

void stack::peek()
{
	cout<<"Peak is:"<<a[top];
}

int main()
{ 
    stack obj;int s;
	do{
		cout<<"\nEnter your choice:";
		cout<<"\n1.push\n2.pop\n3.display\n4.peak\n";
		cin>>s;
			switch(s)
			{

				case 1:obj.push();
				break;
				case 2:obj.pop();
				break;
				case 3:obj.display();
				break;
				case 4:obj.peek();
				break;
			}
		}while(s!=0);
}
