package ProjectPackage;

import java.util.ArrayList;

public class InternClass extends UserClass
{
	static int idnum = 0;
	int id;
	String Field_of_study;
	ArrayList <String> skills = new ArrayList<String>();
	boolean hire;
	
	public InternClass()
	{
		super();
		this.Field_of_study = "Null";
		this.hire = false;
		this.skills.add("Empty");
	}
	
	void hire()
	{
		this.hire = true;
	}
	
	void getskil()
	{
		for(int i = 0; i < this.skills.size(); i++)
		{
			System.out.println(this.skills.get(i));
		}
	}
	void setskil(ArrayList<String> a)
	{
		for(int i = 0; i < a.size(); i++)
		{
			if(i == 0)
			{
				skills.set(0,a.get(i));
			}
			else
				skills.add(a.get(i));
		}
	}
	
	public void newIntern()
	{
		idnum++;
		this.id = idnum;
		System.out.println("\nEnter your name: ");
		this.setname(in.next());
		System.out.println("Enter your age: ");
		this.setage(in.nextInt());
		System.out.println("Enter your email id :");
		this.setemail(in.next());
		System.out.println("Enter your phone number: ");
		this.setphnum(in.next());
		System.out.println("Enter your skills: ");
		int i = 0, j = 0;
		while (i == 0)
		{
			if(j == 0)
			{
				this.skills.set(0,in.next());
				j = 1;
			}
			else
				this.skills.add(in.next());
			System.out.println("Do you want to add more skills? (0 for YES/1 for NO)");
			i = in.nextInt();
			if (i == 1)
				break;
		}
	}
	
	public void displayIntern()
	{
		System.out.println("\nID: " + this.id);
		System.out.println("Name: " + this.getname());
		System.out.println("Age: " + this.getage());
		System.out.println("Email ID: " + this.getemail());
		System.out.println("Phone Number: " + this.getphnum());
		System.out.println("Skills: ");
		getskil();
		System.out.println("Hire Status: " + this.hire);
	}
	
	public void copy(InternClass intern)
	{
		this.id = intern.id;
		this.setname(intern.getname());
		this.setage(intern.getage());
		this.setemail(intern.getemail());
		this.setphnum(intern.getphnum());
		this.setskil(intern.skills);
		this.Field_of_study = intern.Field_of_study;
		this.hire = intern.hire;
	}
}
