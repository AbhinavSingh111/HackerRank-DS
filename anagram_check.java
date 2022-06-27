import java.util.Scanner;

public class Solution {

    static boolean isAnagram(String a, String b) {
        // Complete the function

        if(a.length()==b.length())
        {
            a=a.toLowerCase();
            b=b.toLowerCase();

            for(int i=0;i<a.length();i++)
            {
                for(int j=0;j<b.length();j++)
                {
                    if(a.charAt(i)==b.charAt(j))
                    {
                        b = b.substring(0,j)+""+b.substring(j+1);
                        break;
                    }
                }
            }

            if(b.length()==0)
            {
                return true;
            }
            else
            {
                return false;
            }
        }
        else
            {
                return false;
            }

    }

  public static void main(String[] args) {
    
        Scanner scan = new Scanner(System.in);
        String a = scan.next();
        String b = scan.next();
        scan.close();
        boolean ret = isAnagram(a, b);
        System.out.println( (ret) ? "Anagrams" : "Not Anagrams" );
    }
}
