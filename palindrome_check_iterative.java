import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        
        Scanner sc=new Scanner(System.in);
        String A=sc.next();
        char chr;
        /* Enter your code here. Print output to STDOUT. */
        String rev="";
        for(int i=0;i<A.length();i++)
        {
            chr=A.charAt(i);
            rev=chr+rev;
        }

        if (A.equals(rev))
        {
            System.out.println("Yes");
        }
        else
        {
            System.out.println("No");
        }
    }
}



