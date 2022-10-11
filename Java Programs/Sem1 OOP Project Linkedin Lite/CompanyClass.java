package ProjectPackage;

import java.io.Serializable;
import java.util.Scanner;

public class CompanyClass implements Serializable
{
	static Scanner in = new Scanner(System.in);
	static int idnum = 0;
	int id;
	String Name;
	String HeadQuarters;
	String Email;
	String Sector;
	
	public CompanyClass()
	{
		this.Name = "Null";
		this.HeadQuarters = "Null";
		this.Email = "Null";
		this.Sector = "Null";
	}
	
	void newcom()
	{
		idnum++;
		this.id = idnum;
		System.out.println("\nEnter the company name: ");
		this.Name = in.nextLine();
		System.out.println("Enter the headquaters location: ");
		this.HeadQuarters = in.nextLine();
		System.out.println("Enter the Email ID: ");
		this.Email = in.nextLine();
		System.out.println("Enter the industry sector: ");
		this.Sector = in.nextLine();
	}
	
	void displaycom()
	{
		System.out.println("\nID: " + this.id);
		System.out.println("Company name: " + this.Name);
		System.out.println("Headquaters locations: " + this.HeadQuarters);
		System.out.println("Email ID: " + this.Email);
		System.out.println("Industry sector: " + this.Sector);
	}
}