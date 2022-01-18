import java.util.Scanner;

public class num_2003 {

    static int n;
    static int m;
    static int[] line;
    static int count=0;
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

        int fron=0;
        int back=0;
        int pref=-1;
        int preb=-1;
        int total=0;

        while(true){
            if (total < m && fron < n){
                total+=line[fron];
                fron+=1;
            }else if(total > m && back < n){
                while (true){
                    total-=line[back];
                    back+=1;
                    if (total <= m){
                        break;
                    }
                }
            }
            if (total==m && back < n){
                count+=1;
                total-=line[back];
                back+=1;
            }

            if (pref==fron && preb==back){
                break;
            }

            pref=fron;
            preb=back;
        }


    }


    public static void main(String[] args) {
        getInput();
        sol();
        System.out.println(count);
    }
}
