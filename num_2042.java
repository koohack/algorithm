import java.util.Scanner;

public class num_2042 {


    static int n;
    static int m;
    static int k;
    static int[] line;
    static Scanner cs=new Scanner(System.in);
    static int[] store;

    public static void getInput(){
        n=cs.nextInt();
        m=cs.nextInt();
        k=cs.nextInt();

        line=new int[n];
        store=new int[n];
        for (int i = 0; i < n; i++) {
            int temp=cs.nextInt();
            if(i==0){
                line[i]=temp;
            }else{
                line[i]=line[i-1]+temp;
            }
            store[i]=temp;
        }
    }


    public static void main(String[] args) {
        getInput();

        for (int i = 0; i < m+k; i++) {
            int cmd=cs.nextInt();
            int front=cs.nextInt();
            int back=cs.nextInt();

            if (cmd==1){
                // change
                int temp=back-store[front-1];
                for (int j = front-1; j < n; j++) {
                    line[j]=line[j]+temp;
                }
                store[front-1]=back;
            }else{
                if (front-2 >= 0){
                    System.out.println(line[back-1]-line[front-2]);
                }else{
                    System.out.println(line[back-1]);
                }
            }
        }
    }
}
