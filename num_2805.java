import java.util.Arrays;
import java.util.Collections;
import java.util.Scanner;

public class num_2805 {

    static int n;
    static long m;
    static int[] line;
    static int answer;
    static int c=0;
    static Scanner sc=new Scanner(System.in);

    public static void getInput(){
        n=sc.nextInt();
        m=sc.nextInt();
        line=new int[n];

        for (int i = 0; i < n; i++) {
            line[i]=sc.nextInt();
        }

    }

    public static void sol(){
        Arrays.sort(line);

        int fron=n-2;
        int back=n-1;
        long total=0;


        total+=line[back];
        while (true){
            total+=line[fron];

            long check=total-(back-fron+1)*line[fron];
            if (check < m && fron-1 >= 0){
                fron-=1;
            }else{
                int count=back-fron+1;
                total=total-count*line[fron];
                count-=1;

                while (total > m){
                    total=total-count*1;
                    c+=1;
                }
                break;
            }
        }

        if (total < m){
            answer=line[fron]+c-1;
        }else{
            answer=line[fron]+c;
        }

    }


    public static void main(String[] args) {
        getInput();
        sol();
        System.out.println(answer);
    }
}
