package ProjectPackage;

import java.io.*;
import java.util.ArrayList;
import java.util.Scanner;

public class MainClass 
{
	
	public static void main(String[] args) 
	{
		Scanner in = new Scanner(System.in);
		int id, i = 0;
		System.out.println("WELCOME TO THE JOB PROFILE PLATFORM!!!!");
		while(i == 0)
		{
			System.out.println("\nSelect your identity: ");
			System.out.println("1) Job Applicant");
			System.out.println("2) Intern");
			System.out.println("3) Employer");
			System.out.println("4) Admin");
			System.out.println("5) Exit");
			id = in.nextInt();
			switch(id)
			{
				case 1:
					JobApplicant();
					break;
				
				case 2:
					Intern();
					break;
				
				case 3:
					Employer();
					break;
				
				case 4:
					Admin();
					break;
					
				case 5:
					return;
					
				default:
					System.out.println("The given input is wrong. Do you want to retry? (0 for YES/1 for NO");
					i = in.nextInt();
			}
		}			
	}
	
	public static void JobApplicant()
	{
		Scanner in = new Scanner(System.in);
		int sel, i = 0;
		while(i == 0)
		{
			System.out.println(" ");
			System.out.println("Select your intention: ");
			System.out.println("1) Make new profile");
			System.out.println("2) View your profile");
			System.out.println("3) Delete your profile");
			System.out.println("4) View all job applicant profiles");
			System.out.println("5) View all hired job applicants");
			System.out.println("6) Veiw available jobs");
			System.out.println("7) Veiw companies");
			System.out.println("8) Go back");
			sel = in.nextInt();
			File f = new File("JobApplicant.dat");
			JobApplicantClass j = new JobApplicantClass();
			int id;
			switch(sel)
			{
				case 1:
					makenewjobapplicant();
					break;
				
				case 2:
					int x = 0;
					System.out.println("Enter your id: ");
					id = in.nextInt();
					try
					{
						boolean cont = true;
						ObjectInputStream input = new ObjectInputStream(new FileInputStream(f));
						while(cont)
						{
							j = (JobApplicantClass)input.readObject();
							if(j != null)
							{
								if(j.id == id)
								{
									j.displayApplicant();
									x = 1;
								}
							}
							else
								cont = false;
						}
						input.close();
					}
					catch (Exception e)
					{
						
					}
					if(x == 0)
						System.out.println("This id does not exist");
					break;
				
				case 3:
					System.out.println("Enter your id: ");
					id = in.nextInt();
					deletejobapplicant(id);
					break;
					
				case 4:
					displayalljobapplicants();
					break;
					
				case 5:
					displayhiredjobapplicants();
					break;
					
				case 6:
					displayjobs();
					break;
				
				case 7:
					displaycompanies();
					break;
				
				case 8:
					return;
				
				default:
					System.out.println("The given input is wrong. Do you want to retry? (0 for YES/1 for NO");
					i = in.nextInt();
			}
		}	
		
	}
	
	public static void makenewjobapplicant()
	{
		ArrayList<Integer> ids = new ArrayList<Integer>();
		File f = new File("JobApplicant.dat");
		File file = new File("Temporary.dat");
		JobApplicantClass j = new JobApplicantClass();
		try
		{
			boolean cont = true;
			
			ObjectInputStream input = new ObjectInputStream(new FileInputStream(f));
			ObjectOutputStream out = new ObjectOutputStream(new FileOutputStream(file));
			while(cont)
			{
				j = (JobApplicantClass)input.readObject();
				ids.add(j.id);
				if(j != null)
					out.writeObject(j);
				else
					cont = false;
			}
			out.close();
			input.close();
		}
		catch(Exception e)
		{
			
		}
		try
		{
			boolean cont = true;
			ObjectOutputStream out = new ObjectOutputStream(new FileOutputStream(f));
			ObjectInputStream input = new ObjectInputStream(new FileInputStream(file));
				
			j.newApplicant();
			for(int i = 0; i < ids.size(); i++)
			{
				if(j.id == ids.get(i))
					j.id++;
			}
			System.out.println("Your id is " + j.id);
			out.writeObject(j);
			while(cont)
			{
				j = (JobApplicantClass)input.readObject();
				if(j != null)
					out.writeObject(j);
				else
					cont = false;
			}
			out.close();
			input.close();
		}

		catch(Exception e)
		{
			
		}
		
	}
	
	public static void deletejobapplicant(int id)
	{
		int x = 0;
		File f = new File("JobApplicant.dat");
		File file = new File("Temporary.dat");
		JobApplicantClass j = new JobApplicantClass();
		try
		{
			boolean cont = true;
			
			ObjectInputStream input = new ObjectInputStream(new FileInputStream(f));
			ObjectOutputStream out = new ObjectOutputStream(new FileOutputStream(file));
			while(cont)
			{
				j = (JobApplicantClass)input.readObject();
				if(j != null)
				{
					if(j.id != id)
						out.writeObject(j);
					else
						x = 1;
				}
				else
					cont = false;
			}
			out.close();
			input.close();
		}
		catch(Exception e)
		{
			
		}
		if(x == 0)
			System.out.println("This id does not exist");
		if(x == 1)
			System.out.println("Deleted");
		try
		{
			boolean cont = true;
			
			ObjectInputStream input = new ObjectInputStream(new FileInputStream(file));
			ObjectOutputStream out = new ObjectOutputStream(new FileOutputStream(f));
			while(cont)
			{
				j = (JobApplicantClass)input.readObject();
				if(j != null)
					out.writeObject(j);
				else
					cont = false;
			}
			out.close();
			input.close();
		}
		catch(Exception e)
		{
			
		}
	}
	
	public static void displayalljobapplicants()
	{
		File f = new File("JobApplicant.dat");
		JobApplicantClass j = new JobApplicantClass();
		try
		{
			boolean cont = true;
			ObjectInputStream input = new ObjectInputStream(new FileInputStream(f));
			while(cont)
			{
				j = (JobApplicantClass)input.readObject();
				if(j != null)
					j.displayApplicant();
				else
					cont = false;
			}
			input.close();
		}
		catch (Exception e)
		{
			
		}
	}
	
	public static void displayhiredjobapplicants()
	{
		File f = new File("HiredJobApplicants.dat");
		JobApplicantClass j = new JobApplicantClass();
		try
		{
			boolean cont = true;
			ObjectInputStream input = new ObjectInputStream(new FileInputStream(f));
			while(cont)
			{
				j = (JobApplicantClass)input.readObject();
				if(j != null)
					j.displayApplicant();
				else
					cont = false;
			}
			input.close();
		}
		catch (Exception e)
		{
			
		}
	}
	
	public static void displayjobs()
	{
		File f = new File("Job.dat");
		try
		{
			boolean cont = true;
			ObjectInputStream input = new ObjectInputStream(new FileInputStream(f));
			JobClass s = new JobClass();
			while(cont)
			{
				s = (JobClass)input.readObject(); // Object class object
				if(s != null)
				{
					s.diplayjob();
				}
				else
					cont = false;
			}
			input.close();
		}
		catch(Exception e)
		{
			
		}
	}
	
	public static void displaycompanies()
	{
		File f = new File("Company.dat");
		try
		{
			boolean cont = true;
			ObjectInputStream input = new ObjectInputStream(new FileInputStream(f));
			CompanyClass s = new CompanyClass();
			while(cont)
			{
				s = (CompanyClass)input.readObject(); // Object class object
				if(s != null)
				{
					s.displaycom();
				}
				else
					cont = false;
			}
			input.close();
		}
		catch(Exception e)
		{
			
		}
	}
	
	public static void Intern()
	{
		Scanner in = new Scanner(System.in);
		int sel, i = 0;
		while(i == 0)
		{
			System.out.println(" ");
			System.out.println("Select your intention: ");
			System.out.println("1) Make new profile");
			System.out.println("2) View your profile");
			System.out.println("3) Delete your profile");
			System.out.println("4) View all intern profiles");
			System.out.println("5) View all hired interns profile");
			System.out.println("6) Veiw available internships");
			System.out.println("7) Veiw companies");
			System.out.println("8) Go back");
			sel = in.nextInt();
			File f = new File("Intern.dat");
			InternClass j = new InternClass();
			int id;
			switch(sel)
			{
				case 1:
					makenewintern();
					break;
				
				case 2:
					int x = 0;
					System.out.println("Enter your id: ");
					id = in.nextInt();
					try
					{
						boolean cont = true;
						ObjectInputStream input = new ObjectInputStream(new FileInputStream(f));
						while(cont)
						{
							j = (InternClass)input.readObject();
							if(j != null)
							{
								if(j.id == id)
								{
									j.displayIntern();
									x = 1;
								}
							}
							else
								cont = false;
						}
						input.close();
					}
					catch (Exception e)
					{
						
					}
					if(x == 0)
						System.out.println("This id does not exist");
					break;
					
				case 3:
					System.out.println("Enter your id: ");
					id = in.nextInt();
					deleteintern(id);
					break;
					
				case 4:
					displayallinterns();
					break;
					
				case 5:
					displayhiredinterns();
					break;
					
				case 6:
					displayinternships();
					break;
				
				case 7:
					displaycompanies();
					break;
				
				case 8:
					return;
				
				default:
					System.out.println("The given input is wrong. Do you want to retry? (0 for YES/1 for NO");
					i = in.nextInt();
			}
		}
	}
	
	public static void makenewintern()
	{
		ArrayList<Integer> ids = new ArrayList<Integer>();
		File f = new File("Intern.dat");
		File file = new File("Temporary.dat");
		InternClass j = new InternClass();
		try
		{
			boolean cont = true;
			
			ObjectInputStream input = new ObjectInputStream(new FileInputStream(f));
			ObjectOutputStream out = new ObjectOutputStream(new FileOutputStream(file));
			while(cont)
			{
				j = (InternClass)input.readObject();
				ids.add(j.id);
				if(j != null)
					out.writeObject(j);
				else
					cont = false;
			}
			out.close();
			input.close();
		}
		catch(Exception e)
		{
			
		}
		try
		{
			boolean cont = true;
			
			ObjectInputStream input = new ObjectInputStream(new FileInputStream(file));
			ObjectOutputStream out = new ObjectOutputStream(new FileOutputStream(f));
			j.newIntern();
			for(int i = 0; i < ids.size(); i++)
			{
				if(j.id == ids.get(i))
					j.id++;
			}
			System.out.println("Your id is " + j.id);
			out.writeObject(j);
			while(cont)
			{
				j = (InternClass)input.readObject();
				if(j != null)
					out.writeObject(j);
				else
					cont = false;
			}
			out.close();
			input.close();
		}
		catch(Exception e)
		{
			
		}
	}
	
	public static void deleteintern(int id)
	{
		int x = 0;
		File f = new File("Intern.dat");
		File file = new File("Temporary.dat");
		InternClass j = new InternClass();
		try
		{
			boolean cont = true;
			
			ObjectInputStream input = new ObjectInputStream(new FileInputStream(f));
			ObjectOutputStream out = new ObjectOutputStream(new FileOutputStream(file));
			while(cont)
			{
				j = (InternClass)input.readObject();
				if(j != null)
				{
					if(j.id != id)
						out.writeObject(j);
					else
						x = 1;
				}
				else
					cont = false;
			}
			out.close();
			input.close();
		}
		catch(Exception e)
		{
			
		}
		if(x == 0)
			System.out.println("This id does not exist");
		if(x == 1)
			System.out.println("Deleted");
		try
		{
			boolean cont = true;
			
			ObjectInputStream input = new ObjectInputStream(new FileInputStream(file));
			ObjectOutputStream out = new ObjectOutputStream(new FileOutputStream(f));
			while(cont)
			{
				j = (InternClass)input.readObject();
				if(j != null)
					out.writeObject(j);
				else
					cont = false;
			}
			out.close();
			input.close();
		}
		catch(Exception e)
		{
			
		}
	}
	
	public static void displayallinterns()
	{
		File f = new File("Intern.dat");
		InternClass j = new InternClass();
		try
		{
			boolean cont = true;
			ObjectInputStream input = new ObjectInputStream(new FileInputStream(f));
			while(cont)
			{
				j = (InternClass)input.readObject();
				if(j != null)
					j.displayIntern();
				else
					cont = false;
			}
			input.close();
		}
		catch (Exception e)
		{
			
		}
	}
	
	public static void displayhiredinterns()
	{
		File f = new File("HiredInterns.dat");
		InternClass j = new InternClass();
		try
		{
			boolean cont = true;
			ObjectInputStream input = new ObjectInputStream(new FileInputStream(f));
			while(cont)
			{
				j = (InternClass)input.readObject();
				if(j != null)
					j.displayIntern();
				else
					cont = false;
			}
			input.close();
		}
		catch (Exception e)
		{
			
		}
	}
	
	public static void displayinternships()
	{
		File f = new File("Internship.dat");
		try
		{
			boolean cont = true;
			ObjectInputStream input = new ObjectInputStream(new FileInputStream(f));
			InternshipClass s = new InternshipClass();
			while(cont)
			{
				s = (InternshipClass)input.readObject(); // Object class object
				if(s != null)
				{
					s.displayinternship();
				}
				else
					cont = false;
			}
			input.close();
		}
		catch(Exception e)
		{
			
		}
	}
	
	public static void Employer()
	{
		Scanner in = new Scanner(System.in);
		int sel, i = 0;
		while(i == 0)
		{
			System.out.println(" ");
			System.out.println("Select your intention: ");
			System.out.println("1) Make new profile");
			System.out.println("2) View your profile");
			System.out.println("3) Delete your profile");
			System.out.println("4) View all employer profiles");
			System.out.println("5) Veiw all job applicants");
			System.out.println("6) Veiw all internship applicants");
			System.out.println("7) Veiw available jobs");
			System.out.println("8) Veiw available internships");
			System.out.println("9) Veiw companies");
			System.out.println("10) Hire job  applicant");
			System.out.println("11) Hire interns");
			System.out.println("12) Add new job");
			System.out.println("13) Add new internship");
			System.out.println("14) Remove job");
			System.out.println("15) Remove internship");
			System.out.println("16) Go back");
			sel = in.nextInt();
			File f = new File("Employer.dat");
			EmployerClass j = new EmployerClass();
			int id;
			switch(sel)
			{
				case 1:
					makenewemployer();
					break;
				
				case 2:
					int x = 0;
					System.out.println("Enter your id: ");
					id = in.nextInt();
					try
					{
						boolean cont = true;
						ObjectInputStream input = new ObjectInputStream(new FileInputStream(f));
						while(cont)
						{
							j = (EmployerClass)input.readObject();
							if(j != null)
							{
								if(j.id == id)
								{
									j.displayEmployer();
									x = 1;
								}
							}
							else
								cont = false;
						}
						input.close();
					}
					catch (Exception e)
					{
						
					}
					if(x == 0)
						System.out.println("This id does not exist");
					break;
					
				case 3:
					System.out.println("Enter your id: ");
					id = in.nextInt();
					deleteemployer(id);
					break;
					
				case 4:
					displayallemployers();
					break;
					
				case 5:
					displayalljobapplicants();
					break;
					
				case 6:
					displayallinterns();
					break;
					
				case 7:
					displayjobs();
					break;
					
				case 8:
					displayinternships();
					break;
				
				case 9:
					displaycompanies();
					break;
				
				case 10:
					hirejobapplicant();
					break;
					
				case 11:
					hireintern();
					break;
					
				case 12:
					addjob();
					break;
					
				case 13:
					addinternship();
					break;
					
				case 14:
					displayjobs();
					System.out.println("Enter job id: ");
					id = in.nextInt();
					removejob(id);
					break;
					
				case 15:
					displayinternships();
					System.out.println("Enter internship id: ");
					id = in.nextInt();
					removeinternship(id);
					break;
					
				case 16:
					return;
				
				default:
					System.out.println("The given input is wrong. Do you want to retry? (0 for YES/1 for NO");
					i = in.nextInt();
			}
		}	
	}
	
	public static void makenewemployer()
	{
		ArrayList<Integer> ids = new ArrayList<Integer>();
		File f = new File("Employer.dat");
		File file = new File("Temporary.dat");
		EmployerClass j = new EmployerClass();
		try
		{
			boolean cont = true;
			
			ObjectInputStream input = new ObjectInputStream(new FileInputStream(f));
			ObjectOutputStream out = new ObjectOutputStream(new FileOutputStream(file));
			while(cont)
			{
				j = (EmployerClass)input.readObject();
				ids.add(j.id);
				if(j != null)
					out.writeObject(j);
				else
					cont = false;
			}
			out.close();
			input.close();
		}
		catch(Exception e)
		{
			
		}
		try
		{
			boolean cont = true;
			
			ObjectInputStream input = new ObjectInputStream(new FileInputStream(file));
			ObjectOutputStream out = new ObjectOutputStream(new FileOutputStream(f));
			j.newEmployer();
			for(int i = 0; i < ids.size(); i++)
			{
				if(j.id == ids.get(i))
					j.id++;
			}
			System.out.println("Your id is " + j.id);
			out.writeObject(j);
			while(cont)
			{
				j = (EmployerClass)input.readObject();
				if(j != null)
					out.writeObject(j);
				else
					cont = false;
			}
			out.close();
			input.close();
		}
		catch(Exception e)
		{
			
		}
	}
	
	public static void deleteemployer(int id)
	{
		int x = 0;
		File f = new File("Employer.dat");
		File file = new File("Temporary.dat");
		EmployerClass j = new EmployerClass();
		try
		{
			boolean cont = true;
			
			ObjectInputStream input = new ObjectInputStream(new FileInputStream(f));
			ObjectOutputStream out = new ObjectOutputStream(new FileOutputStream(file));
			while(cont)
			{
				j = (EmployerClass)input.readObject();
				if(j != null)
				{
					if(j.id != id)
						out.writeObject(j);
					else
						x = 1;
				}
				else
					cont = false;
			}
			out.close();
			input.close();
		}
		catch(Exception e)
		{
			
		}
		if(x == 0)
			System.out.println("This id does not exist");
		if(x == 1)
			System.out.println("Deleted");
		try
		{
			boolean cont = true;
			
			ObjectInputStream input = new ObjectInputStream(new FileInputStream(file));
			ObjectOutputStream out = new ObjectOutputStream(new FileOutputStream(f));
			while(cont)
			{
				j = (EmployerClass)input.readObject();
				if(j != null)
					out.writeObject(j);
				else
					cont = false;
			}
			out.close();
			input.close();
		}
		catch(Exception e)
		{
			
		}
	}
	
	public static void displayallemployers()
	{
		File f = new File("Employer.dat");
		EmployerClass j = new EmployerClass();
		try
		{
			boolean cont = true;
			ObjectInputStream input = new ObjectInputStream(new FileInputStream(f));
			while(cont)
			{
				j = (EmployerClass)input.readObject();
				if(j != null)
					j.displayEmployer();
				else
					cont = false;
			}
			input.close();
		}
		catch (Exception e)
		{
			
		}
	}
	
	public static void hirejobapplicant()
	{
		displayalljobapplicants();
		Scanner in = new Scanner(System.in);
		int id, x = 0;
		System.out.println("Enter the id of the job applicant you want to hire: ");
		id = in.nextInt();
		File f = new File("JobApplicant.dat");
		JobApplicantClass j = new JobApplicantClass();
		JobApplicantClass nj = new JobApplicantClass();
		try
		{
			boolean cont = true;
			ObjectInputStream input = new ObjectInputStream(new FileInputStream(f));
			while(cont)
			{
				j = (JobApplicantClass)input.readObject();
				if(j != null)
				{
					if(j.id == id)
					{
						nj.copy(j);
						nj.hire = true;
					}
					else
						x = 1;
				}
				else
					cont = false;
			}
			input.close();
		}
		catch (Exception e)
		{
			
		}
		if(x == 0)
			System.out.println("This id does not exist");
		if(x == 1)
			System.out.println("Hired");
		File file = new File("HiredJobApplicants.dat");
		try
		{
			ObjectOutputStream out = new ObjectOutputStream(new FileOutputStream(file));
			out.writeObject(nj);
			out.close();
		}
		catch (Exception e)
		{
			
		}
		deletejobapplicant(id);
	}
	
	public static void hireintern()
	{
		displayallinterns();
		Scanner in = new Scanner(System.in);
		int id, x = 0;
		System.out.println("Enter the id of the job applicant you want to hire: ");
		id = in.nextInt();
		File f = new File("Intern.dat");
		InternClass j = new InternClass();
		InternClass nj = new InternClass();
		try
		{
			boolean cont = true;
			ObjectInputStream input = new ObjectInputStream(new FileInputStream(f));
			while(cont)
			{
				j = (InternClass)input.readObject();
				if(j != null)
				{
					if(j.id == id)
					{
						nj.copy(j);
						nj.hire = true;
					}
					else
						x = 1;
				}
				else
					cont = false;
			}
			input.close();
		}
		catch (Exception e)
		{
			
		}
		if(x == 0)
			System.out.println("This id does not exist");
		if(x == 1)
			System.out.println("Hired");
		File file = new File("HiredInterns.dat");
		try
		{
			ObjectOutputStream out = new ObjectOutputStream(new FileOutputStream(file));
			out.writeObject(nj);
			out.close();
		}
		catch (Exception e)
		{
			
		}
		deleteintern(id);
	}
	
	public static void addjob()
	{
		File f = new File("Job.dat");
		File file = new File("Temporary.dat");
		JobClass j = new JobClass();
		try
		{
			boolean cont = true;
			
			ObjectInputStream input = new ObjectInputStream(new FileInputStream(f));
			ObjectOutputStream out = new ObjectOutputStream(new FileOutputStream(file));
			while(cont)
			{
				j = (JobClass)input.readObject();
				if(j != null)
					out.writeObject(j);
				else
					cont = false;
			}
			out.close();
			input.close();
		}
		catch(Exception e)
		{
			
		}
		try
		{
			boolean cont = true;
			
			ObjectInputStream input = new ObjectInputStream(new FileInputStream(file));
			ObjectOutputStream out = new ObjectOutputStream(new FileOutputStream(f));
			j.newjob();
			out.writeObject(j);
			while(cont)
			{
				j = (JobClass)input.readObject();
				if(j != null)
					out.writeObject(j);
				else
					cont = false;
			}
			out.close();
			input.close();
		}
		catch(Exception e)
		{
			
		}
	}
	
	public static void addinternship()
	{
		File f = new File("Internship.dat");
		File file = new File("Temporary.dat");
		InternshipClass j = new InternshipClass();
		try
		{
			boolean cont = true;
			
			ObjectInputStream input = new ObjectInputStream(new FileInputStream(f));
			ObjectOutputStream out = new ObjectOutputStream(new FileOutputStream(file));
			while(cont)
			{
				j = (InternshipClass)input.readObject();
				if(j != null)
					out.writeObject(j);
				else
					cont = false;
			}
			out.close();
			input.close();
		}
		catch(Exception e)
		{
			
		}
		try
		{
			boolean cont = true;
			
			ObjectInputStream input = new ObjectInputStream(new FileInputStream(file));
			ObjectOutputStream out = new ObjectOutputStream(new FileOutputStream(f));
			j.newinternship();
			out.writeObject(j);
			while(cont)
			{
				j = (InternshipClass)input.readObject();
				if(j != null)
					out.writeObject(j);
				else
					cont = false;
			}
			out.close();
			input.close();
		}
		catch(Exception e)
		{
			
		}
	}
	
	public static void removejob(int id)
	{
		File f = new File("Job.dat");
		File file = new File("Temporary.dat");
		JobClass j = new JobClass();
		try
		{
			boolean cont = true;
			
			ObjectInputStream input = new ObjectInputStream(new FileInputStream(f));
			ObjectOutputStream out = new ObjectOutputStream(new FileOutputStream(file));
			while(cont)
			{
				j = (JobClass)input.readObject();
				if(j != null)
				{
					if(j.id != id)
						out.writeObject(j);
				}
				else
					cont = false;
			}
			out.close();
			input.close();
		}
		catch(Exception e)
		{
			
		}
		try
		{
			boolean cont = true;
			
			ObjectInputStream input = new ObjectInputStream(new FileInputStream(file));
			ObjectOutputStream out = new ObjectOutputStream(new FileOutputStream(f));
			while(cont)
			{
				j = (JobClass)input.readObject();
				if(j != null)
					out.writeObject(j);
				else
					cont = false;
			}
			out.close();
			input.close();
		}
		catch(Exception e)
		{
			
		}
	}
	
	public static void removeinternship(int id)
	{
		File f = new File("Internship.dat");
		File file = new File("Temporary.dat");
		InternshipClass j = new InternshipClass();
		try
		{
			boolean cont = true;
			
			ObjectInputStream input = new ObjectInputStream(new FileInputStream(f));
			ObjectOutputStream out = new ObjectOutputStream(new FileOutputStream(file));
			while(cont)
			{
				j = (InternshipClass)input.readObject();
				if(j != null)
				{
					if(j.id != id)
						out.writeObject(j);
				}
				else
					cont = false;
			}
			out.close();
			input.close();
		}
		catch(Exception e)
		{
			
		}
		try
		{
			boolean cont = true;
			
			ObjectInputStream input = new ObjectInputStream(new FileInputStream(file));
			ObjectOutputStream out = new ObjectOutputStream(new FileOutputStream(f));
			while(cont)
			{
				j = (InternshipClass)input.readObject();
				if(j != null)
					out.writeObject(j);
				else
					cont = false;
			}
			out.close();
			input.close();
		}
		catch(Exception e)
		{
			
		}
	}
	
	public static void Admin()
	{
		Scanner in = new Scanner(System.in);
		int sel, i = 0;
		while(i == 0)
		{
			System.out.println(" ");
			System.out.println("Select your intention: ");
			System.out.println("1) Add company");
			System.out.println("2) Delete company");
			System.out.println("3) Go back");
			sel = in.nextInt();
			int id;
			switch(sel)
			{
				case 1:
					addcompany();
					break;
					
				case 2:
					System.out.println("Enter company id: ");
					id = in.nextInt();
					deletecompany(id);
					break;
					
				case 3:
					return;
					
				default:
					System.out.println("The given input is wrong. Do you want to retry? (0 for YES/1 for NO");
					i = in.nextInt();
			}
		}
	}
	
	public static void addcompany()
	{
		ArrayList<Integer> ids = new ArrayList<Integer>();
		File f = new File("Company.dat");
		File file = new File("Temporary.dat");
		CompanyClass j = new CompanyClass();
		try
		{
			boolean cont = true;
			
			ObjectInputStream input = new ObjectInputStream(new FileInputStream(f));
			ObjectOutputStream out = new ObjectOutputStream(new FileOutputStream(file));
			while(cont)
			{
				j = (CompanyClass)input.readObject();
				ids.add(j.id);
				if(j != null)
					out.writeObject(j);
				else
					cont = false;
			}
			out.close();
			input.close();
		}
		catch(Exception e)
		{
			
		}
		try
		{
			boolean cont = true;
			
			ObjectInputStream input = new ObjectInputStream(new FileInputStream(file));
			ObjectOutputStream out = new ObjectOutputStream(new FileOutputStream(f));
			j.newcom();
			for(int i = 0; i < ids.size(); i++)
			{
				if(j.id == ids.get(i))
					j.id++;
			}
			out.writeObject(j);
			while(cont)
			{
				j = (CompanyClass)input.readObject();
				if(j != null)
					out.writeObject(j);
				else
					cont = false;
			}
			out.close();
			input.close();
		}
		catch(Exception e)
		{
			
		}
	}
	
	public static void deletecompany(int id)
	{
		int x = 0;
		File f = new File("Company.dat");
		File file = new File("Temporary.dat");
		CompanyClass j = new CompanyClass();
		try
		{
			boolean cont = true;
			
			ObjectInputStream input = new ObjectInputStream(new FileInputStream(f));
			ObjectOutputStream out = new ObjectOutputStream(new FileOutputStream(file));
			while(cont)
			{
				j = (CompanyClass)input.readObject();
				if(j != null)
				{
					if(j.id != id)
						out.writeObject(j);
					else
						x = 1;
				}
				else
					cont = false;
			}
			out.close();
			input.close();
		}
		catch(Exception e)
		{
			
		}
		if(x == 0)
			System.out.println("This id does not exist");
		if(x == 1)
			System.out.println("Deleted");
		try
		{
			boolean cont = true;
			
			ObjectInputStream input = new ObjectInputStream(new FileInputStream(file));
			ObjectOutputStream out = new ObjectOutputStream(new FileOutputStream(f));
			while(cont)
			{
				j = (CompanyClass)input.readObject();
				if(j != null)
					out.writeObject(j);
				else
					cont = false;
			}
			out.close();
			input.close();
		}
		catch(Exception e)
		{
			
		}
	}
	
}