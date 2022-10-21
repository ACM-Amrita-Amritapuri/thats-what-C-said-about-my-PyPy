#include<stdio.h>
#include<stdlib.h>
int top=-1,n,*stack,choice,x;
void push()
{
	if(top>=n-1)
	{
		printf("Stack is overflow\n");
	}
	else
	{
		printf("Enter value to be pushed:\n");
		scanf("%d",&x);
		top++;
		*(stack+top)=x;
		printf("\n");
	}
}
void pop()
{
	if(top<=-1)
	{
		printf("Stack is underflow\n");
	}
	else
	{
		printf("The popped element is: %d\n",*(stack+top));
		top--;
	}
}
void peek()
{
	if(top>=0)
	{
		printf("Element on the top of stack is: %d\n",*(stack+top));
	}
	else
	{
		printf("Stack is empty");
	}
}
void isfull()
{
	if(top==n-1)
    {
		printf("TRUE");
	}
	else
	{
		printf("FALSE");
	}
}
void isempty()
{
	if(top==(-1))
    {
		printf("TRUE");
	}
	else
	{
		printf("FALSE");
	}
}
int main()
{
	printf("enter the size of stack:\n");
	scanf("%d",&n);
	stack = (int*)malloc(n*sizeof(int));
	printf("\n");
	printf("\n\t 1.PUSH\n\t 2.POP\n\t 3.PEEK\n\t 4.ISEMPTY\n\t 5.ISFULL\n\t 6.EXIT\n\t");
	do
	{
		printf("\nEnter the choice:\n");
		scanf("%d",&choice);
		switch(choice)
		{
			case 1:
			{
				push();
				break;
			}
			case 2:
			{
				pop();
				break;
			}
			case 3:
			{
				peek();
				break;
			}
			case 4:
            {
                isempty();
				break;
            }
			case 5:
            {
                isfull();
				break;
            }
            case 6:
            {
				printf("\n\t EXIT POINT ");
                break;
			}
            default:
            {
                printf ("\n\t Please Enter a Valid Choice(1/2/3/4/5/6)");
            }
		}
	}
		while(choice!=6);
		return 0;
}
