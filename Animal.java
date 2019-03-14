public class Animal
{
	private float weight;
	private float length;
	private int heartBeatsPerMinute;
	private String name;
	
	public void setWeight(float _weight)
	{
		weight = _weight;
	}
	
	public float getWeight()
	{
		return weight;
	}
	
	public void setLength(float _length)
	{
		length = _length;
	}
	
	public float getLength()
	{
		return length;
	}
	
	public void setHeartBeatsPerMinute(int bpm)
	{
		heartBeatsPerMinute = bpm;
	}
	
	public int getHeartBeatsPerMinute()
	{
		return heartBeatsPerMinute;
	}
	
	public void setName(String _name)
	{
		name = _name;
	}
	
	public String getName()
	{
		return name;
	}
	
	public void printInfo()
	{
		System.out.println("Class Animal : function printInfo() : Dit Dier weegt: " + weight + " kilo");
		System.out.println("Dit Dier is: " + length + " centimeter lang");
		System.out.println("Dit Dier heeft: " + heartBeatsPerMinute + " hartslagen per minuut");
		System.out.println("Dit Dier heet: " + name);
	}
}