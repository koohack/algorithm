import javax.xml.parsers.SAXParser;
import java.util.ArrayList;
import java.util.Scanner;

public class num_1927 {

    static int n;
    static int[] sto;
    static ArrayList<Integer> line=new ArrayList<Integer>();
    static Scanner sc=new Scanner(System.in);

    public static void getInput(){
        n=sc.nextInt();

        sto=new int[n];
    }

    public static void sol(){
        for (int i = 0; i < n; i++) {
            int cmd=sc.nextInt();

            if (cmd==0){
                if (line.size() == 0){
                    System.out.println(0);
                }else{
                    System.out.println(line.remove(0));
                }
            }else{
                int size=line.size();
                for (int j = 0; j < size; j++) {
                    if (line.get(j) > cmd){
                        line.add(j, cmd);
                    }
                }
                if (line.size()==0){
                    line.add(cmd);
                }
            }
            //System.out.println(line);
        }
    }

    public static void sol1(){
        




    }


    public static void main(String[] args) {
        getInput();
        sol1();
    }

    public static class minHeap{
        int heap[];
        int size;

        public minHeap(int size){
            heap=new int[size];
        }

        public void insert(int x){
            heap[++size]=x;

            for (int i=size; i >= 0; i/=2){
                if (heap[i/2] > heap[i]){
                    swap(i/2, i);
                }
            }



        }

        public void swap(int a, int b){
            int temp=heap[a];
            heap[a]=heap[b];
            heap[b]=temp;
        }

    }


}
