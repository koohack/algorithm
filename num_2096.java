import java.util.Scanner;

public class num_2096 {

    static int[] maxdp;
    static int[] mindp;
    static int[] store;
    static int n;
    static int max=0;
    static int min=999999999;
    static Scanner sc=new Scanner(System.in);

    public static void getInput(){
        n=sc.nextInt();

        maxdp=new int[3];
        mindp=new int[3];
        store=new int[3];
    }

    public static int getMin(int x, int y, int z){
        if (x < y){
            if (x < z){
                return x;
            }
        }
        if (y < z){
            if (y < x){
                return y;
            }
        }
        if (z < x){
            if (z < y){
                return z;
            }
        }
        return 0;
    }

    public static int getMax(int x, int y, int z){
        if (x > y){
            if (x > z){
                return x;
            }
        }
        if (y > x){
            if (y > z){
                return y;
            }
        }
        if (z > x){
            if (z > y){
                return z;
            }
        }
        return 0;
    }

    public static void sol(){
        for (int i = 0; i < n; i++) {
            if (i==0){
                for (int j = 0; j < 3; j++) {
                    int t=sc.nextInt();
                    maxdp[j]=t;
                    mindp[j]=t;
                }
                continue;
            }
            for (int j = 0; j < 3; j++) {
                store[j]=sc.nextInt();
            }

            for (int j = 0; j < n; j++) {
                int max1=0;
                int max2=0;
                int max3;
                int min1=999999999;
                int min2=999999999;
                int min3;

                if (j+1 < n){
                    max1=store[j+1]+maxdp[j];
                    min1=store[j+1]+mindp[j];
                }
                if (j-1 >= 0){
                    max2=store[j-1]+maxdp[j];
                    min2=store[j-1]+mindp[j];
                }
                max3=store[j]+maxdp[j];
                min3=store[j]+mindp[j];

                maxdp[j]=getMax(max1, max2, max3);
                mindp[j]=getMin(min1, min2, min3);
            }
        }
    }

    public static void answer(){
        for (int i = 0; i < 3; i++) {
            if (maxdp[i] > max){
                max=maxdp[i];
            }
            if (mindp[i] < min){
                min=mindp[i];
            }
        }
    }


    public static void main(String[] args) {
        getInput();
        sol();
        answer();
        System.out.println(Integer.toString(max)+" "+Integer.toString(min));
    }
}
