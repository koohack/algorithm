import java.util.ArrayList;
import java.util.Scanner;

public class num_2143 {

    static int t;
    static int n;
    static int m;
    static int[] line1;
    static int[] line2;
    static ArrayList<Integer> temp1=new ArrayList<Integer>();
    static ArrayList<Integer> temp2=new ArrayList<Integer>();
    static Scanner sc=new Scanner(System.in);

    public static void getInput(){
        t=sc.nextInt();
        n=sc.nextInt();
        line1=new int[n];
        for (int i = 0; i < n; i++) {
            line1[i]=sc.nextInt();
        }
        m=sc.nextInt();
        line2=new int[n];
        for (int i = 0; i < n; i++) {
            line2[i]=sc.nextInt();
        }
    }

    public static void sol(){
        for (int i = 0; i < n; i++) {
            int temp=line1[i];
            temp1.add(temp);
            for (int j = i+1; j < n; j++) {
                temp+=line1[j];
                temp1.add(temp);
            }
        }

        for (int i = 0; i < m; i++) {
            int temp=line2[i];
            temp2.add(temp);
            for (int j = i+1; j < m; j++) {
                temp+=line2[j];
                temp2.add(temp);
            }
        }



    }

    public static void main(String[] args) {

    }
}
