package Zisterne;

public class Zisterne {
	int Volumen = 800;
	double D = 1.25;
	
	double h = 0.72;
	double d = 1.12;
	
	public void berechnen(){
		double D2 = Math.pow(D, 2);
		double d2 = Math.pow(d, 2);
	
		double V = 0;
		V = (h*Math.PI)/12;
		V =  V * (D2+d2+(d*D));
		V = V*1000;
		
			
		
		
		//System.out.println(V);
		
		
		/*while(V<800){
			D2 = Math.pow(D, 2);
			d2 = Math.pow(d, 2);
			
			
			V = 0;
			V = (h*Math.PI)/12;
			V =  V * (D2+d2+(d*D));
			V = V*1000;
			System.out.println(V);
			System.out.println(d);
			d = d+0.001;
			
		}
		*/
		
		
	}
	
	
	public double volumen_berechnen(double D1, double d1 , double h1){
		
		double D22 = Math.pow(D1, 2);
		double d22 = Math.pow(d1, 2);
		double V;
		V = 0;
		
		V = (h1*Math.PI)/12;
		V =  V * (D22+d22+(d1*D1));
		V = V*1000;
		System.out.println(V);
		
		//System.out.println(d22);
		return V;
		
	}
	
	public void hoehe_berechnen(double hg, double d1, double D1){
		double Vist = 0;
		double D111 = 0.1;
		double LDreicheck1,LDreicheck2, Dneu ;
		double Winkel1;
		double hf;
		double Dneu1;
		hf = 0.1;
		
		
		while(hf<hg){
			
		
		LDreicheck1 = (D1-d1)/2;
		
		Winkel1 = Math.toDegrees(Math.atan(hg/LDreicheck1));
		
		
		LDreicheck2 = (hf)/(Math.tan(Math.toRadians(Winkel1)));
		
		Dneu = LDreicheck1 - LDreicheck2;
		Dneu1 =d1+(2*Dneu);
		
		//System.out.println("Winkel grosses Dreieck " +Winkel1);
		//System.out.println(LDreicheck1);
		//System.out.println(LDreicheck2);
		//System.out.println("haktuell ist "+ hf + " Das neueberechnte D ist " +Dneu);
		
		System.out.println(hf);
		this.volumen_berechnen(Dneu1, d1, hf);
		
		hf = hf+0.01;
		
		}
		
		
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Zisterne berechnen = new Zisterne();
		
		//berechnen.hoehe_berechnen(1, fh, d1, V);
		berechnen.hoehe_berechnen(0.73 ,1.19, 1.25 );
	}

}
