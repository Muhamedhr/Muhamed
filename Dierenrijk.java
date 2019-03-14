public class Dierenrijk
{
	public static void main(String[]args)
	{
		Animal a = new Animal();
		
		a.setWeight(999);
		a.setLength(300);
		a.setName("Kameel");
		a.setHeartBeatsPerMinute(60);
		
		
		Katachtige k = new Katachtige();
		
		k.setWeight(3);
		k.setLength(25);
		k.setHeartBeatsPerMinute(90);
		k.setName("Pinju");
		k.setMonthsPregnant(5);
		k.setAmountOfWervels(12);
		k.setLungCapicity(1);
		k.setManierVanSlapen("miaaauwwwww");
		
		System.out.println("==========================================================================");
		a.printInfo();
		System.out.println("==========================================================================");
		k.printInfo();
		System.out.println("==========================================================================");
		
	}
}