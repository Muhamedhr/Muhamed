public class Mammal extends Animal
{
	private int monthsPregnant;
	private int amountOfWervels;
	private float lungCapicity;
	private final String animalType = "Mammal";
	private String manierVanSlapen = "zzzzzzzzzzzzzzz";
	
	public void setMonthsPregnant(int _monthspregnant)
	{
		monthsPregnant = _monthspregnant;
	}
	
	public int getMonthsPregnant()
	{
		return monthsPregnant;
	}
	
	public void setAmountOfWervels(int _amountOfWervels)
	{
		amountOfWervels = _amountOfWervels;
	}
	
	public int getAmountOfWervels()
	{
		return amountOfWervels;
	}
	
	public void setLungCapicity(float _lungCapicity)
	{
		lungCapicity = _lungCapicity;
	}
	
	public float getLungCapicity()
	{
		return lungCapicity;
	}
	
	public void setManierVanSlapen(String _manierVanSlapen)
	{
		manierVanSlapen = _manierVanSlapen;
	}
	
	public String getManierVanSlapen()
	{
		return manierVanSlapen;
	}
	
	public void baarKind(String message)
	{
		System.out.println("Class Mammal : Functie baarKind() : " + message);
	}
	
	public void slaap()
	{
		System.out.println("Class mammal : function slaap() : Dit dier slaapt -> "+ manierVanSlapen);
	}
	
	public void printInfo()
	{
		super.printInfo();
		System.out.println("Class Mammal : function printInfo()");
		System.out.println("Dit Zoogdier is gemiddeld: " + monthsPregnant + "maanden zwanger");
		System.out.println("Dit Zoogdier heeft: " + amountOfWervels + " wervels");
		System.out.println("Dit zoogdier heeft gemiddeld: " + lungCapicity + " liter lunginhoud");
		System.out.println("Dit Zoogdier slaapt zo -> : " + manierVanSlapen);
	}
		
}