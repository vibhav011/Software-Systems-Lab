import java.util.Map;
import java.util.HashMap;
import java.util.Scanner;
import java.io.File;

public class PollutionCheck 
{
    public static void main(String[] args) 
    {
        Map<String, Vehicle> vehicles = new HashMap<String, Vehicle>();
        File file1 = new File(args[0]);
        File file2 = new File(args[1]);
        File file3 = new File(args[2]);

        Scanner sc=null;
        try 
        {
            sc=new Scanner(file1);
            while(sc.hasNextLine())
            {
                String data = sc.nextLine();
                String arr[] = data.split(", ", 5);
                if(!vehicles.containsKey(arr[0]))
                {
                    if(arr[3] == "Truck")
                    {
                        Truck obj = new Truck(arr[0], arr[1], arr[2]);
                        vehicles.put(arr[0], obj);
                    }
                    else
                    {
                        Car obj = new Car(arr[0], arr[1], arr[2]);
                        vehicles.put(arr[0], obj);
                    }
                }
            }
            sc = new Scanner(file2);
            while(sc.hasNextLine())
            {
                String data = sc.nextLine();
                String arr[] = data.split(", ", 4);
                vehicles.get(arr[0]).setPollutionValues(Float.parseFloat(arr[1]), Float.parseFloat(arr[2]), Float.parseFloat(arr[3]));
            }
            sc = new Scanner(file3);
            while(sc.hasNextLine())
            {
                String data = sc.nextLine();
                if(!vehicles.containsKey(data))
                    System.out.println("NOT REGISTERED");
                else
                    System.out.println(vehicles.get(data).getStatus());
            }
        } 
        catch (Exception e) 
        {
            System.out.println("File Not Found!" + e);
        }
    }
}