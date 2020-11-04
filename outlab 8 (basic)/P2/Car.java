public class Car extends Vehicle 
{
    public Car(String r, String m, String o)
    {
        super(r, m, o);
    }

    public void checkPollutionStatus()
    {
        if(co2 <= 15 && co <= 0.5 && hc <= 750)
            pollutionStatus = "PASS";
        else
            pollutionStatus = "FAIL";
    }
}