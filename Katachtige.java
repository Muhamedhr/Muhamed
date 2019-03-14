public class Katachtige extends Mammal
{
	private final String mammalType = "Katachtige";
	private final String kiesType = "Knipkiezen";
	private final boolean heeftPoten = true;
	private final boolean nachtdier = true;
	
	public void printInfo()
	{
		super.printInfo();
		System.out.println("Class Katachtige : function printInfo()");
		System.out.println("Dit is een : " + mammalType + " met het type kiezen: " + kiesType + ", en heeft poten :)");
	}
}