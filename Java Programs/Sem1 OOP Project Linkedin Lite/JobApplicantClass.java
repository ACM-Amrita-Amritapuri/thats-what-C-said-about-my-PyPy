package ProjectPackage;

import java.util.ArrayList;

public class JobApplicantClass extends UserClass
{
	static int idnum = 0;
	int id;
	ArrayList<String> qualifications = new ArrayList<String>(1);
	int experiance;
	ArrayList<String> skills = new ArrayList<String>(1);
	boolean hire;
	
	public JobApplicantClass()
	{
		super();
		this.experiance = 0;
		this.hire = false;
		this.qualifications.add("Empty");
		this.skills.add("Empty");
	}
	
	void hire()
	{
		this.hire = true;
	}	
	
	void getquali()
	{
		for(int i = 0; i < this.qualifications.size(); i++)
		{
			System.out.println(this.qualifications.get(i));
		}
	}
	
	void getskil()
	{
		for(int i = 0; i < this.skills.size(); i++)
		{
			System.out.println(this.skills.get(i));
		}
	}
	
	void setquali(ArrayList<String> a)
	{
		for(int i = 0; i < a.size(); i++)
		{
			if(i == 0)
			{
				qualifications.set(0,a.get(i));
			}
			else
				qualifications.add(a.get(i));
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
	
	public void newApplicant()
	{
		idnum++;
		this.id = idnum;
		System.out.println("\nEnter your name: ");
		this.setname(in.next());
		System.out.println("Enter your age: ");
		this.setage(in.nextInt());
		System.out.println("Enter your email id: ");
		this.setemail(in.next());
		System.out.println("Enter your phone number: ");
		this.setphnum(in.next());
		System.out.println("Enter your years of experiance in industry: ");
		this.experiance = in.nextInt();
		System.out.println("Enter your qualifications: ");
		int i = 0, j = 0;
		while (i == 0)
		{
			if(j == 0)
			{
				this.qualifications.set(0,in.next());
				j = 1;
			}
			else
			{
				this.qualifications.add(in.next());
			}
			System.out.println("Do you want to add more qualifications? (0 for YES/1 for NO)");
			i = in.nextInt();
			if (i == 1)
				break;
		}
		System.out.println("Enter your skills: ");
		i = 0;
		j = 0;
		while (i == 0)
		{
			if(j == 0)
			{
				this.skills.set(0,in.next());
				j = 1;
			}
			else
			{
				this.skills.add(in.next());
			}
			System.out.println("Do you want to add more skills? (0 for YES/1 for NO)");
			i = in.nextInt();
			if (i == 1)
				break;
		}
	}
	
	public void displayApplicant()
	{
		System.out.println("\nID: " + this.id);
		System.out.println("Name: " + this.getname());
		System.out.println("Age: " + this.getage());
		System.out.println("Email ID: " + this.getemail());
		System.out.println("Phone Number: " + this.getphnum());
		System.out.println("Experiance: " + this.experiance + " years");
		System.out.println("Qualifications: ");
		getquali();
		System.out.println("Skills: ");
		getskil();
		System.out.println("Hire Status: " + this.hire);
	}
	
	public void copy(JobApplicantClass jobapp)
	{
		this.id = jobapp.id;
		this.setname(jobapp.getname());
		this.setage(jobapp.getage());
		this.setemail(jobapp.getemail());
		this.setphnum(jobapp.getphnum());
		this.experiance = jobapp.experiance;
		this.setquali(jobapp.qualifications);
		this.setskil(jobapp.skills);
		this.hire = jobapp.hire;
	}
}