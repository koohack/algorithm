import java.util.Scanner;

public class num_1806 {

    static int n;
    static int s;
    static int[] line;
    static int min=999999998;
    static Scanner sc=new Scanner(System.in);

    public static void getInput(){
        n=sc.nextInt();
        s=sc.nextInt();
        line=new int[n];

        for (int i = 0; i < n; i++) {
            line[i]=sc.nextInt();
        }
    }

    public static void sol(){
        int fron=-1;
        int back=-1;
        int pref=-1;
        int preb=-1;
        int total=0;

        while (!(fron >= n || back >= n)){
            //System.out.println("---------------------------------------------");
            //System.out.println(Integer.toString(back)+" "+Integer.toString(fron));
            if (total < s && fron+1 < n){
                fron+=1;
                total+=line[fron];
            }else if (total >= s && back+1 < n){
                back+=1;
                total-=line[back];

                int temp=fron-back+1;
                if(temp < min){
                    min=temp;
                }
            }

            if (pref==fron && preb==back){
                break;
            }
            //System.out.println(total);
            //System.out.println(Integer.toString(back)+" "+Integer.toString(fron));
            //System.out.println("---------------------------------------------");
            pref=fron;
            preb=back;
        }


    }

    public static void main(String[] args) {
        getInput();
        sol();
        if(min==999999998){
            System.out.println("0");
        }else {
            System.out.println(min);
        }
    }


}
