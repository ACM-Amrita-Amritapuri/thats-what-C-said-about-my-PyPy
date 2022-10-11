package ProjectPackage;

import java.io.Serializable;
import java.util.ArrayList;
import java.util.Scanner;

public class InternshipClass implements Serializable
{
	static Scanner in = new Scanner(System.in);
	static int idnum = 0;
	int id;
	String Company;
	String Type;
	Double Stipend;
	ArrayList<String> Skills = new ArrayList<String>();
	Double Duration;
	
	public InternshipClass()
	{
		this.Company = "Null";
		this.Type = "Null";
		this.Stipend = 0.0;
		this.Duration = 0.0;
		this.Skills.add("Empty");
	}
	
	void getskil()
	{
		for(int i = 0; i < this.Skills.size(); i++)
		{
			System.out.println(this.Skills.get(i));
		}
	}
	
	void setskil(ArrayList<String> a)
	{
		for(int i = 0; i < a.size(); i++)
		{
			if(i == 0)
			{
				this.Skills.set(0,a.get(i));
			}
			else
				this.Skills.add(a.get(i));
		}
	}
	
	public void newinternship()
	{
		idnum++;
		this.id = idnum;
		System.out.println("\nEnter company name: ");
		this.Company = in.next();
		System.out.println("Enter the type of internship: ");
		this.Type = in.next();
		System.out.println("Enter the stipend: ");
		this.Stipend = in.nextDouble();
		System.out.println("Enter the duration of the internship: ");
		this.Duration = in.nextDouble();
		System.out.println("Enter the required skills: ");
		int i = 0, j = 0;
		while (i == 0)
		{
			if(j == 0)
			{
				this.Skills.set(0,in.next());
				j = 1;
			}
			else
				this.Skills.add(in.next());
			System.out.println("Do you want to add more skills? (0 for YES/1 for NO)");
			i = in.nextInt();
			if (i == 1)
				break;
		}
	}
	
	public void displayinternship()
	{
		System.out.println("\nID: " + this.id);
		System.out.println("Company: " + this.Company);
		System.out.println("Internship Type: " + this.Type);
		System.out.println("Stipend: " + this.Stipend);
		System.out.println("Duration: " + this.Duration);
		System.out.println("Required Skills: ");
		this.getskil();
	}
}
