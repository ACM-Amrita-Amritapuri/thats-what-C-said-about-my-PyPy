#include<iostream>
using namespace std;

class queue
{
	public:
	int a[5];
	int rear,front;
	queue()
	{
		rear=-1;
		front=-1;
	}
	void enqueue();
	void dequeue();
	void display();
};

void queue::enqueue()
{ 
	cout<<"Enter the element to be inserted:";
	rear++;
	cin>>a[rear];
}

void queue::dequeue()
{
	 if(rear==-1)
	 {
		 cout<<"QUEUE is empty\n";
	 }
	 else
	 {
		 front++;
	   cout<<"The element has been removed: "<<a[front]<<endl;
	   rear--; 
	 }	
}

void queue::display()
{	
	 int i;
	 if(rear==-1)
	 {
		 cout<<"QUEUE is empty\n";
	 }
	 else
	 {
		cout<<"The  Queue is:";
		for(i=front+1;i<=rear;i++)
		{
			cout<<a[i]<<" ";
		 } 
		 cout<<"\n";
	 } 
}

int main()
{ 
    queue obj;int s;
	do{
		cout<<"1.enqueue\n2.dequeue\n3.display\n";
		cout<<"Enter your choice:";
		cin>>s;
			switch(s)
			{

				case 1:obj.enqueue();
				break;
				case 2:obj.dequeue();
				break;
				case 3:obj.display();
				break;
			}
		}while(s!=0);
}
