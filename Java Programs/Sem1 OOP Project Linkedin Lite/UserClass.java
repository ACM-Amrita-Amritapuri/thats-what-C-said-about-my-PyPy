package ProjectPackage;

import java.io.Serializable;
import java.util.Scanner;

public class UserClass implements Serializable
{
	static Scanner in = new Scanner(System.in);
	private String Name;
	private int Age;
	private String Email;
	private String PhNum;
	
	public UserClass()
	{
		this.Name = "Null";
		this.Age = 0;
		this.Email = "Null";
		this.PhNum = "Null";
	}
	
	public UserClass(String name, int age, String email, String phnum)
	{
		this.Name = name;
		this.Age = age;
		this.Email = email;
		this.PhNum = phnum;
	}

	public void adduser()
	{
		System.out.println("\nEnter your name: ");
		this.Name = in.nextLine();
		System.out.println("Enter your age:");
		this.Age = in.nextInt();
		System.out.println("Enter your E-mail ID: ");
		this.Email = in.nextLine();
		System.out.println("Enter your phone number: ");
		this.PhNum = in.nextLine();
	}
	
	void setname(String name)
	{
		this.Name = name;
	}
	void setemail(String email)
	{
		this.Email = email;
	}
	void setphnum(String phnum)
	{
		this.PhNum = phnum;
	}
	void setage(int age)
	{
		this.Age = age;
	}
	
	int getage()
	{
		return this.Age;
	}
	String getname()
	{
		return this.Name;
	}
	String getemail()
	{
		return this.Email;
	}
	String getphnum()
	{
		return this.PhNum;
	}
}