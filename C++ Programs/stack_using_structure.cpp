#include<iostream>
using namespace std;

struct stack
{
	int a[5];
	int top;
	
};

void push(struct stack*);
void pop(struct stack*);
void display(struct stack*);
void peak(struct stack*);

int main()
{ 
	struct stack obj;int s;
	obj.top=-1;
	do{
		cout<<"\nEnter your choice:";
		cout<<"\n1.push\n2.pop\n3.display\n4.peak\n";
		cin>>s;
			switch(s)
			{

				case 1:push(&obj);
				break;
				case 2:pop(&obj);
				break;
				case 3:display(&obj);
				break;
				case 4:peak(&obj);
				break;
			}
		}while(s!=0);
}

 void push(struct stack* obj)
{   
	cout<<"Enter the array to be inserted:";
	obj->top++;
	cin>>obj->a[obj->top];
}

void pop(struct stack* obj)
{ 
	 if(obj->top==-1)
	 {
		 cout<<"STACK is empty";
	 }
	 else
	 {
	   cout<<"The element has been poped: "<<obj->a[obj->top]<<endl;
	   obj->top--; 
	 }	
}

void display(struct stack* obj)
{  	
	 int i;
	 if(obj->top==-1)
	 {
		 cout<<"STACK is empty";
	 }
	 else
	 {
		cout<<"The  array is:";
		for(i=obj->top;i>=0;i--)
		{
			cout<<obj->a[i]<<" ";
		}
     }   
}

void peak(struct stack *obj)
{
	cout<<"Peak is:"<<obj->a[obj->top];
}
