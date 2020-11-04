abstract public class Vehicle 
{
    protected String regNo, manufacturer, owner, pollutionStatus;
    protected double co2, co, hc;

    public Vehicle(String r, String m, String o)
    {
        regNo = r;
        manufacturer = m;
        owner = o;
        pollutionStatus = "PENDING";
    }

    public void setPollutionValues(double a, double b, double c)
    {
        co2 = a;
        co = b;
        hc = c;
        checkPollutionStatus();
    }

    public String getStatus()
    {
        return pollutionStatus;
    }

    abstract public void checkPollutionStatus();
    public String toString()
    {
        String a = "Reg No: " + regNo + "\nManufacturer: " + manufacturer + "\nOwner: " + owner + "\nPollution Status: " + pollutionStatus;
        return a;
    }
}
