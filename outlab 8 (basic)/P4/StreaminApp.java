/*
DO NOT MODIFY THE CODE STUB
NO NEED TO DEFINE main()
*/

import java.util.*;

class StreamingApp
{
	public static Map<String, ArrayList<String> > getFavouriteGenres(Map<String, ArrayList<String> > userMovies, Map<String, ArrayList<String> > movieGenres)
	{
		Map<String, ArrayList<String> > ans = new HashMap<String, ArrayList<String> >();
		Map<String, String> movTogen = new HashMap<String, String>();
		for(Map.Entry <String, ArrayList<String> > entry : movieGenres.entrySet())
		{
			String y = entry.getKey();
			for(String x : entry.getValue())
				movTogen.put(x, y);
        }
		for(Map.Entry <String, ArrayList<String> > entry : userMovies.entrySet())
		{
			String y = entry.getKey();
			Map<String, Integer> fin = new HashMap<String, Integer>();
			for(String x : entry.getValue())
			{
                String z = movTogen.get(x);
				if(fin.containsKey(z))
					fin.put(z, fin.get(z)+1);
				else
					fin.put(z, 1);
			}
			int high = 0;
			for(Map.Entry <String, Integer> ent : fin.entrySet())
                high = Math.max(high, ent.getValue());
			ArrayList<String> a = new ArrayList<String>();
			for(Map.Entry <String, Integer> ent : fin.entrySet())
			{
				if(ent.getValue() == high)
					a.add(ent.getKey());
			}
			ans.put(y, a);
		}
		return ans;
	}
}