import java.util.Scanner;

public class num_2748 {


    static int n;
    static long store[]=new long[91];
    static long answer;
    static Scanner sc=new Scanner(System.in);


    public static void getInput(){
        n=sc.nextInt();
    }


    public static void sol(){
        store[1]=1;
        store[2]=1;
        re(3, n);
    }

    public static void re(int now, int limit){
        if (now > limit){
            answer=store[limit];
        }else{
            store[now]=store[now-1]+store[now-2];
            re(now+1, limit);
        }

    }

    public static void main(String[] args) {
        getInput();
        sol();
        System.out.println(answer);
    }

}
