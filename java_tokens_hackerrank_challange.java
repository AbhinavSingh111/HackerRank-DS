import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String s = scan.nextLine();
        if (s.matches("[ ]+"))
        {
            System.out.println("0");
        }
        else{
            // Write your code here.
        String q = s.replaceAll("^[\\s]+", "");
        String [] str = q.split("[[ ]+,?.@'!_]+");
        int num= str.length;
        System.out.println(num);
        for(int i = 0 ; i<num ; i++)
        {
            System.out.println(str[i]);
        }
        }

        
        
        scan.close();
    }
}

