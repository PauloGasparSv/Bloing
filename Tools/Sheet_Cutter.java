import java.awt.image.BufferedImage;
import javax.imageio.ImageIO;
import java.io.IOException;
import java.io.File;

public class Sheet_Cutter{
		public static void main(String args[]){

			BufferedImage sheet = null;
			BufferedImage frames[][] = null;
			int lines = -1;
			int columns = -1;
			try{
				sheet = ImageIO.read(new File(args[0]));
				
				lines = Integer.parseInt(args[1]);
				columns = Integer.parseInt(args[2]);

				int width = (int)(sheet.getWidth()/columns);
				int height = (int)(sheet.getHeight()/lines);

				frames = new BufferedImage[lines][columns];

				for(int line = 0; line < lines; line++)
					for(int column = 0; column < columns; column++)
						frames[line][column] = sheet.getSubimage(column*width,line*height,width,height);


			}catch(IOException e){
				System.out.println("ERROR. Could be caused by wrong file path.");
				System.exit(0);
			}

			if(frames != null){
				try{
					File outputFolder = new File(args[3]);
					outputFolder.mkdir();
					int current_frame = 0;
					for(int line = 0; line < lines; line++){
						for(int column = 0; column < columns; column++){
							File output = new File(args[3]+"/"+current_frame+".png");
							ImageIO.write(frames[line][column],"png",output);
							current_frame++;
						}
					}
				}catch(IOException e){
					System.out.println("ERROR. Could be caused by wrong saving path.");
					System.exit(0);
				}

			}

		}


}