import java.math.BigDecimal;
import java.util.*;
class Solution{

    public static void main(String []args){
        //Input
        Scanner sc= new Scanner(System.in);
        int n=sc.nextInt();
        String []s=new String[n+2];
        for(int i=0;i<n;i++){
            s[i]=sc.next();
        }
      	sc.close();

        //Write your code here
//         Arrays.sort(s, Collections.reverseOrder(new Comparator<String>() {
//         @Override
//         public int compare(String a1, String a2) {
//             //convert to big decimal inside comparator
//             //so permanent string values are never changed
//             //aka you only use the BigDecimal values to 
//             //compare the strings!
//             BigDecimal a = new BigDecimal(a1);
//             BigDecimal b = new BigDecimal(a2);
//             return a.compareTo(b);
//     }
// }));
// bubble sort
    for (int i = 0; i < s.length-2; i++) {
        for (int j = 1; j < (n-i); j++) {
            BigDecimal sj = new BigDecimal(s[j]);
            BigDecimal sj1 = new BigDecimal(s[j-1]);
            if(sj.compareTo(sj1) == 1){
                String temp = s[j];
                s[j] = s[j-1];
                s[j-1] = temp;
            }
        }       
    }

        //Output
        for(int i=0;i<n;i++)
        {
            System.out.println(s[i]);
        }
    }

}
