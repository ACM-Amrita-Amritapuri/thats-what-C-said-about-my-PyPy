#include<stdio.h>
#include<stdlib.h>
#include<stdbool.h>
int front=-1,rear=-1,*queue,capacity;
void enqueue()
{
	int temp;
	if(rear==capacity-1)
	{
		printf("Queue is overflow\n");
	}
	else
	{
		if(front==-1)
		front=0;	
		printf("Insert element into queue:\n");
		scanf("%d",&temp);
		rear=rear+1;
		*(queue+rear)=temp;
	}
}
void dequeue()
{
	if(front==-1||front>rear)
	{
		printf("Queue is underflow\n");
	}
	else
	{
		printf("Element dequeued from queue is: %d\n",*(queue+front));
		front=front+1;
	}
}
bool isfull()
{
	if(rear==capacity-1)
	{
		return true;
	}
	else
	{
		return false;
	}
}
bool isempty()
{
	if((front==rear)&&(rear==-1))
	{
		return true;
	}
	else
	{
		return false;
	}
}
int main()
{
	int choice;
	printf("Enter the capicity:\n");
	scanf("%d",&capacity);
	queue=(int*)malloc(capacity*sizeof(int));
	printf("1.enqueue\n");
	printf("2.dequeue\n");
	printf("3.front\n");
	printf("4.rear\n");
	printf("5.isempty\n");
	printf("6.isfull\n");
	printf("7.quit\n");
	printf("Enter your choice:\n");	 
	while(1)
	{
		scanf("%d",&choice);
		switch(choice)
		{
			case 1:
			enqueue();
			break;
			case 2:
			dequeue();
			break;
			case 3:
			printf("Front element is: %d\n",*(queue+front));
			break;
			case 4:
			printf("Rear element is: %d\n",*(queue+rear));
			break;
			case 5:
			if(isempty())
			{
				printf("Queue is empty\n");
			}
			else
			{
				printf("Queue is not empty\n");
			}
			break;
			case 6:
			if(isfull())
			{
				printf("Queue is full\n");
			}
			else
			{
				printf("Queue is not full\n");
			}
			break;
			case 7:
			exit(0);
			default:
			printf("Choose the correct option:\n");
			
		}
	}
}
