import java.io.File;
import java.util.Scanner;
import java.math.BigInteger; 
import java.security.MessageDigest;

public class MD5 {
	public static void main(String[] args) {
		File file = new File("MD5sums");

		try {
			Scanner sc = new Scanner(file);
			MessageDigest md = MessageDigest.getInstance("MD5");

			while(sc.hasNextLine()) {
				String line = sc.nextLine();
				int ind = line.lastIndexOf('-');
				String text = line.substring(0, ind-1);
				String hash = line.substring(ind+2, ind+34);
				
				byte[] thedigest = md.digest(text.getBytes("UTF-8"));
				BigInteger no = new BigInteger(1, thedigest);
				String actualhash = no.toString(16); 
				while (actualhash.length() < 32) 
					actualhash = "0" + actualhash;

				if (actualhash.equals(hash)) System.out.println("verified");
				else System.out.println("not verified");
			}
		}
		catch (Exception e) {
			System.out.println("Some Error Occurred!\n" + e);
		}
	}
}