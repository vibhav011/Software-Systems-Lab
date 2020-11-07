import java.awt.event.*;
import javax.swing.*;
import javax.swing.table.*;
import java.io.File;
import java.util.Scanner;
import java.math.BigInteger; 
import java.security.MessageDigest;
import java.util.ArrayList;

public class GUI {

	public static File file = null;

	public static void main(String[] args) {  
		JFrame f = new JFrame();
		
		// Buttons
		JButton selectFile = new JButton("Select file");
		selectFile.setBounds(80,100,100, 40);
		JButton process = new JButton("Process");
		process.setBounds(220,100,100, 40);

		// Labels
		JLabel l1,l2;  
		l1 = new JLabel("Selected file: ");  
		l1.setBounds(50,50, 100,30);  
		l2 = new JLabel("None");  
		l2.setBounds(150,50, 100,30); 

		// Table model
		DefaultTableModel model = new DefaultTableModel();
		model.addColumn("Plain Text");
		model.addColumn("Result");

		// Table inside a scroll pane
		JTable jt = new JTable(model);	
		jt.setBounds(30,40,200,300);	 
		JScrollPane scrollPane = new JScrollPane();
		scrollPane.setBounds(100, 200, 200, 250); 
		scrollPane.setViewportView(jt);

		// When Select file is clicked
		selectFile.addActionListener(new ActionListener() {  
			public void actionPerformed(ActionEvent e){  
				file = null;
				JFileChooser chooser = new JFileChooser("."); 
				int returnVal = chooser.showOpenDialog(f);
				if(returnVal == JFileChooser.APPROVE_OPTION) {
					file = chooser.getSelectedFile();
					l2.setText(file.getName());
				}
			}  
		}); 

		// When process is clicked
		process.addActionListener(new ActionListener() {  
			public void actionPerformed(ActionEvent e){  
				if (file != null) {
					try {
						Scanner sc = new Scanner(file);
						MessageDigest md = MessageDigest.getInstance("MD5");
						model.setRowCount(0);		// Delete all rows

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

							if (actualhash.equals(hash)) model.addRow(new Object[]{text, "verified"});
							else model.addRow(new Object[]{text, "not verified"});
						}
					}
					catch (Exception e2) {
						System.out.println("Some Error Occurred!\n" + e2);
					}
				}
			}  
		}); 
  
		f.add(scrollPane);	  
		f.add(selectFile); f.add(process);
		f.add(l1); f.add(l2);
  
		f.setSize(400,500); 
		f.setLayout(null); 
		f.setVisible(true);
	}
}