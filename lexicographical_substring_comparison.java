package others;

import java.util.Scanner;
public class substring_comparison {

    public static String getSmallestAndLargest(String s, int k) {
        String smallest = "";
        String largest = "";
        
        // Complete the function
        // 'smallest' must be the lexicographically smallest substring of length 'k'
        // 'largest' must be the lexicographically largest substring of length 'k'
//       here value of k is taken as 3

    for (int i = 0; i <= s.length() - 3; i++) 
    {
        String substr = s.substring(i, i + 3);
        if (substr.matches("[a-zA-Z]+")) 
        { 
            if (smallest=="" && largest =="")
            {
                smallest=substr;
                largest=substr;
            }
            if (substr.compareTo(smallest)<0)
            {
                smallest=substr;
            }
            if (substr.compareTo(largest)>0)
            {
                largest=substr;
            }
        }
    }
    
        return smallest + "\n" + largest;
    }


    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String s = scan.next();
        int k = scan.nextInt();
        scan.close();
      
        System.out.println(getSmallestAndLargest(s, k));
    }
}
