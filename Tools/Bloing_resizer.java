import java.awt.image.BufferedImage;
import javax.imageio.ImageIO;
import java.io.IOException;
import java.io.File;

public class Bloing_resizer{
	public static void main(String args[]){
		BufferedImage image[] = null;
		String folder[] = {"Atacando","Correndo","Morrendo","Parado","Pulando"};
		for(int a = 0; a < 5; a++){
			try{					
				image = new BufferedImage[a == 0?16:20];
				for(int i = 0; i < (a==0?16:20); i++)
					image[i] = ImageIO.read(new File("../Assets/Grace/"+folder[a]+"/"+i+".png")).getSubimage(11,9,102,84);		
				
			}catch(IOException e){
				System.out.println("ERROR. Could be caused by wrong file path.");
				System.exit(0);
			}
			if(image != null){
				try{
					File outputFolder = new File("../Assets/Grace/"+folder[a]+"/");
					outputFolder.mkdir();
					for(int i = 0; i < image.length; i++){
						File output = new File("../Assets/Grace/"+folder[a]+"/"+i+".png");
						ImageIO.write(image[i],"png",output);
					}
				}
				catch(IOException e){
					System.out.println("ERROR. Could be caused by wrong saving path.");
					System.exit(0);
				}
			}
		}
	}
}