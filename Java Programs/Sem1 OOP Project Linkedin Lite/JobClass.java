package ProjectPackage;

import java.io.Serializable;
import java.util.ArrayList;
import java.util.Scanner;

public class JobClass implements Serializable
{
	static Scanner in = new Scanner(System.in);
	static int idnum = 0;
	int id;
	String Company;
	String Post;
	String JobLocation;
	ArrayList<String> Qualifications = new ArrayList<String>();
	int Experience;
	int TrainingPeriod;
	
	public JobClass()
	{
		this.Company = "Null";
		this.Post = "Null";
		this.JobLocation = "Null";
		this.Experience = 0;
		this.TrainingPeriod = 0;
		this.Qualifications.add("Empty");
	}
	
	void getquali()
	{
		for(int i = 0; i < this.Qualifications.size(); i++)
		{
			System.out.println(this.Qualifications.get(i));
		}
	}
	
	void setquali(ArrayList<String> a)
	{
		for(int i = 0; i < a.size(); i++)
		{
			if(i == 0)
			{
				Qualifications.set(0,a.get(i));
			}
			else
				Qualifications.add(a.get(i));
		}
	}
	
	public void diplayjob() 
	{
		System.out.println("\nID: " + this.id);
		System.out.println("Company: " + this.Company);
		System.out.println("Post: " + this.Post);
		System.out.println("Location: " + this.JobLocation);
		System.out.println("Required Qualification: ");
		this.getquali();
		System.out.println("Required Experience: " + this.Experience + " years");
		System.out.println("Training Period: " + this.TrainingPeriod + " months");
	}
	
	public void newjob()
	{
		idnum++;
		this.id = idnum;
		System.out.println("\nEnter company name: ");
		this.Company = in.next();
		System.out.println("Enter post: ");
		this.Post = in.next();
		System.out.println("Enter job location: ");
		this.JobLocation = in.next();
		System.out.println("Enter the number of years of experience required: ");
		this.Experience = in.nextInt();
		System.out.println("Enter the duration of training period (in months): ");
		this.TrainingPeriod = in.nextInt();
		System.out.println("Enter required qualifications: ");
		int i = 0, j = 0;
		while (i == 0)
		{
			if(j == 0)
			{
				this.Qualifications.set(0,in.next());
				j = 1;
			}
			else
				this.Qualifications.add(in.next());
			System.out.println("Do you want to add more qualifications? (0 for YES/1 for NO)");
			i = in.nextInt();
			if (i == 1)
				break;
		}
	}
}