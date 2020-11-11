package readwrite;

import java.util.Scanner;
import java.io.File;

class ReaderWriter implements Runnable {
	private String FILENAME;
	private ProtectedTree ptree;
	private boolean iswriter;

	public ReaderWriter(String FILENAME, ProtectedTree ptree, boolean iswriter) {
		this.FILENAME = FILENAME;
		this.ptree = ptree;
		this.iswriter = iswriter;
	}

	public void run() {
		try {
			File file = new File(this.FILENAME);
			Scanner sc = new Scanner(file);

			while(sc.hasNextLine()) {
				int val = sc.nextInt();

				if (iswriter) this.ptree.write(val);
				else this.ptree.read(val);
			}
		}
		catch (Exception e) {}
	}
}