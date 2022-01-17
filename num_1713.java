import java.io.FileInputStream;
import java.util.ArrayList;
import java.util.Scanner;

public class num_1713 {

    static int n;
    static int count;
    static int[] student=new int[101];
    static int[] check=new int[101];
    static ArrayList<ArrayList<Integer>> up=new ArrayList<ArrayList<Integer>>();
    static int[] cmd;
    static Scanner sc=new Scanner(System.in);
    static int minIndex=0;


    public static void getInput(){
        n=sc.nextInt();
        count=sc.nextInt();
        cmd=new int[count];

        for(int i=0; i<count; i++){
            cmd[i]=sc.nextInt();
        }
    }

    public static void sol(){
        int photo=1;

        for(int now : cmd){
            if(photo <= n){
                if (student[now]==0){
                    check[now]=photo;
                    student[now]+=1;
                    photo+=1;
                }else{
                    student[now]+=1;
                }
            }else{
                // 1. now 부분에 포토 유무 확인
                // 2. 포토에 있다면 그냥 ++

                // 4. 가장 적은과 같으면 바꾸는 작업 진행
                // 5. 바꿀때 뺀거의 student=0 해야 함
                if (check[now] > 0){
                    student[now]+=1;
                }else{
                    // 3. 포토에 없다면 가장 작은 것과 비교
                    student[now]+=1;
                    boolean c=checkMin(student[now]);
                    // 4. 가장 적은과 같으면 바꾸는 작업 진행
                    if(c){
                        check[minIndex]=0;
                        student[minIndex]=0;
                        check[now]=photo;
                        photo+=1;
                    }
                }
            }
        }

    }

    public static boolean checkMin(int temp){
        int min=999999999;
        int index=999999999;
        for (int i=0; i<101; i++){
            if (check[i] > 0){
                if(min > student[i]){
                    min=student[i];
                    index=check[i];
                    minIndex=i;
                }else if(min==student[i] && index > check[i]){
                    min=student[i];
                    index=check[i];
                    minIndex=i;
                }
            }
        }
        return true;
    }

    public static void answer(){
        for (int i = 0; i < 101; i++) {
            if (check[i] > 0){
                System.out.print(Integer.toString(i)+" ");
            }
        }
    }

    public static void main(String[] args) {
        getInput();
        sol();
        answer();
    }
}
