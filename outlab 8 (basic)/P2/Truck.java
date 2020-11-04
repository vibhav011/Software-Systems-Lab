public class Truck extends Vehicle 
{
    public Truck(String r, String m, String o)
    {
        super(r, m, o);
    }

    public void checkPollutionStatus()
    {
        if(co2 <= 25 && co <= 0.8 && hc <= 1000)
            pollutionStatus = "PASS";
        else
            pollutionStatus = "FAIL";
    }
}