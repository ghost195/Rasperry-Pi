package Muster;

public class Singleton {

	private static Singleton instance;
	
	private Singleton(){
		System.out.println("Test");
	}
	
	public static Singleton getInstance() {
		if(Singleton.instance == null){
			Singleton.instance = new Singleton();
		}
		return Singleton.instance;
	}
	
}
