package ProjectPackage;

public class EmployerClass extends UserClass
{
	static int idnum = 0;
	int id;
	String Company;
	
	public EmployerClass() 
	{
		super();
		this.Company = "Null";
	}
	
	public void newEmployer()
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
		System.out.println("Enter your company name: ");
		this.Company = in.next();
	}
	public void displayEmployer()
	{
		System.out.println("\nID: " + this.id);
		System.out.println("Name: " + this.getname());
		System.out.println("Age: " + this.getage());
		System.out.println("Email ID: " + this.getemail());
		System.out.println("Phone Number: " + this.getphnum());
		System.out.println("Company: " + this.Company);
	}
	
	public JobApplicantClass hirejobapp(JobApplicantClass obj)
	{
		obj.hire();
		return obj;
	}
	
	public InternClass hireintern(InternClass obj)
	{
		obj.hire();
		return obj;
	}
}
