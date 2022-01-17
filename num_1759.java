import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class num_1759 {


    static ArrayList<Character> line=new ArrayList<Character>();
    static int count=0;
    static int clen=0;
    static Scanner sc=new Scanner(System.in);

    public static int[] newcheck(int[] ch){
        int[] out=new int[clen];
        for(int i=0; i<clen; i++) {
            out[i] = ch[i];
        }
        return out;
    }

    public static void sol(int[] check, String string, char pre, int now, int limit, int index){
        if(now==limit){
            int len=string.length();
            int count=0;
            int count1=0;
            for(int i=0; i<len; i++){
                if(string.charAt(i)=='a'){
                    count++;
                }else if(string.charAt(i)=='e'){
                    count++;
                }else if(string.charAt(i)=='i'){
                    count++;
                }else if(string.charAt(i)=='o'){
                    count++;
                }else if(string.charAt(i)=='u'){
                    count++;
                }else{
                    count1++;
                }
            }
            if(count==0 || count1 < 2){
                return;
            }
            System.out.println(string);
        }else{
            for (int i=index+1; i<clen; i++){
                if (check[i]==0 && (int)pre < (int)line.get(i)){
                    int[] tcheck=newcheck(check);
                    tcheck[i]=1;
                    String temp=new String(string);
                    temp+=line.get(i);
                    sol(tcheck, temp, line.get(i), now+1, limit, i);
                }
            }
        }
    }

    public static void main(String[] args) {
        count=sc.nextInt();
        clen=sc.nextInt();

        for(int i=0; i<clen; i++){
            line.add(sc.next().charAt(0));
        }

        Collections.sort(line);

        for(int i=0; i<clen; i++){
            int[] check=new int[clen];
            String temp="";
            temp+=line.get(i);
            sol(check, temp, line.get(i), 1, count, i);
        }


    }


}
