import java.awt.*;
import javax.swing.*;
public class java {

	JFrame Frame;
	JLabel Messwert;
	JTextField Wert;
	JButton OK;
	JSlider Slider;
	
	public void Fenster(){
		Frame = new JFrame ("mein Fenster");
		Frame.getContentPane().setLayout(new FlowLayout());
				
		Messwert = new JLabel("Messwert");
		// Objeckt Messwert vom Typ JLabel erzeugen
		Frame.getContentPane().add(Messwert);
		// Dem Frame das Objeckt Messwert hinzufügen
		
		Wert = new JTextField(10);
		Frame.getContentPane().add(Wert);
		
		OK = new JButton("OK");
		Frame.getContentPane().add(OK);
		
		Slider = new JSlider();
		Frame.getContentPane().add(Slider);
		
		Frame.pack();
		//pack() bewirkt, dass das Frame die minimale Grösse
		//bei optimaler Anordnung der in ihm enthaltenen Komponenten bekommt.
		Frame.setVisible(true);
		
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		java Fenster = new java();
		 Fenster.Fenster();
	}
}
