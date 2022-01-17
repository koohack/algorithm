import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class num_3055 {

    static int r=0;
    static int c=0;
    static Scanner sc=new Scanner(System.in);
    static char[][] map;
    static int[][] dp;
    static Queue<point> queue = new LinkedList<>();
    static int endx;
    static int endy;

    public static void getInput(){

        for(int i=0; i<r; i++){
            String temp=sc.next();
            for(int j=0; j<c; j++){
                char m=temp.charAt(j);
                if (m=='S'){
                    point water=new point(i, j, 'S');
                    queue.add(water);
                    dp[i][j]=1;
                }else if(m=='X'){
                    dp[i][j]=-2;
                }else if (m=='D'){
                    endx=i;
                    endy=j;
                }
                else{
                    dp[i][j]=0;
                }
                map[i][j]=m;

            }
        }
        for (int i=0; i<r; i++){
            for (int j = 0; j < c; j++) {
                if (map[i][j]=='*'){
                    point start=new point(i, j, '*');
                    queue.add(start);
                    dp[i][j]=-1;
                }
            }
        }
    }

    // * water, X stone, D hole, S object
    // x->r y->c
    // process from start point
    public static void sol(){
        while(!queue.isEmpty()){
            point temp=queue.poll();
            int x=temp.x;
            int y=temp.y;
            int type=temp.type;

            // 1. 움직일 수 있는 곳인지 확인
            // 2. 움직일 수 있는 곳 바로 부근에 물이 있는지 확인
            // 3.
            if (type=='S'){
                // 1. 움직일 수 있는 곳인지 확인
                // 1.1. dp 값이 0보다 클 때 움직일 수 있는 곳임
                // 1.2. dp 값이 -1 물, -2 돌
                if (x+1 < r && dp[x+1][y] >= 0){
                    if(map[x+1][y]=='D'){
                        if(dp[x+1][y]==0 || dp[x+1][y] > dp[x][y]+1){
                            dp[x+1][y]=dp[x][y]+1;
                        }
                    }
                    int check=0;
                    // 갈 곳 부근에 물이 없어야 함, 3곳 모두 없어야 함
                    if (x+2 < r && dp[x+2][y]==-1){
                        check=1;
                    }
                    if (y+1 < c && dp[x+1][y+1]==-1){
                        check=1;
                    }
                    if(y-1 >= 0 && dp[x+1][y-1]==-1){
                        check=1;
                    }

                    if (check==0){
                        if (dp[x+1][y]==0 || dp[x+1][y] > dp[x][y]+1){
                            dp[x+1][y]=dp[x][y]+1;
                        }
                        point start=new point(x+1, y, 'S');
                        queue.add(start);
                    }
                }
                if (x-1 >= 0 && dp[x-1][y] >= 0){
                    if(map[x-1][y]=='D'){
                        if(dp[x-1][y]==0 || dp[x-1][y] > dp[x][y]+1){
                            dp[x-1][y]=dp[x][y]+1;
                        }
                    }
                    int check=0;
                    if (x-2 >= 0 && dp[x-2][y]==-1){
                        check=1;
                    }
                    if (y+1 < c && dp[x-1][y+1]==-1){
                        check=1;
                    }
                    if (y-1 >= 0 && dp[x-1][y-1]==-1){
                        check=1;
                    }
                    if (check==0){
                        if (dp[x-1][y]==0 || dp[x-1][y] > dp[x][y]+1){
                            dp[x-1][y]=dp[x][y]+1;
                        }
                        point start=new point(x-1, y, 'S');
                        queue.add(start);
                    }
                }
                if (y+1 < c && dp[x][y+1] >= 0){
                    if(map[x][y+1]=='D'){
                        if(dp[x][y+1]==0 || dp[x][y+1] > dp[x][y]+1){
                            dp[x][y+1]=dp[x][y]+1;
                        }
                    }
                    int check=0;
                    if (x+1 < r && dp[x+1][y+1]==-1){
                        check=1;
                    }
                    if (x-1 >= 0 && dp[x-1][y+1]==-1){
                        check=1;
                    }
                    if (y+2 < c && dp[x][y+2]==-1){
                        check=1;
                    }
                    if (check==0){
                        if (dp[x][y+1]==0 || dp[x][y+1] > dp[x][y]+1){
                            dp[x][y+1]=dp[x][y]+1;
                        }
                        point start=new point(x, y+1, 'S');
                        queue.add(start);
                    }
                }
                if (y-1 >= 0 && dp[x][y-1] >= 0){
                    if(map[x][y-1]=='D'){
                        if(dp[x][y-1]==0 || dp[x][y-1] > dp[x][y]+1){
                            dp[x][y-1]=dp[x][y]+1;
                        }
                    }
                    int check=0;
                    if (x+1 < r && dp[x+1][y-1]==-1){
                        check=1;
                    }
                    if (x-1 >= 0 && dp[x-1][y-1]==-1){
                        check=1;
                    }
                    if (y-2 >= 0 && dp[x][y-2]==-1){
                        check=1;
                    }
                    if (check==0){
                        if (dp[x][y-1]==0 || dp[x][y-1] > dp[x][y]+1){
                            dp[x][y-1]=dp[x][y]+1;
                        }
                        point start=new point(x, y-1, 'S');
                        queue.add(start);
                    }
                }

            }else if (type=='*'){
                if (x+1 < r && dp[x+1][y] > -1 && map[x+1][y]!='D'){
                    dp[x+1][y]=-1;
                    point water=new point(x+1, y, '*');
                    queue.add(water);
                }
                if (x-1 >= 0 && dp[x-1][y] > -1 && map[x-1][y]!='D'){
                    dp[x-1][y]=-1;
                    point water=new point(x-1, y, '*');
                    queue.add(water);
                }
                if (y+1 < c && dp[x][y+1] > -1 && map[x][y+1]!='D'){
                    dp[x][y+1]=-1;
                    point water=new point(x, y+1, '*');
                    queue.add(water);
                }
                if (y-1 >= 0 && dp[x][y-1] > -1  && map[x][y-1]!='D'){
                    dp[x][y-1]=-1;
                    point water=new point(x, y-1, '*');
                    queue.add(water);
                }
            }

            /*
            for (int i = 0; i < r; i++) {
                for (int j = 0; j < c; j++) {
                    System.out.print(dp[i][j]);
                }
                System.out.println();
            }
            System.out.println("-----------------");
             */

        }

    }

    public static void main(String[] args) {
        r=sc.nextInt();
        c=sc.nextInt();
        map=new char[r][c];
        dp=new int[r][c];
        getInput();
        sol();
        if(dp[endx][endy]==0){
            System.out.println("KAKTUS");
        }else{
            System.out.println(dp[endx][endy]-1);
        }


    }
}

class point{
    int x;
    int y;
    char type;

    public point(int x, int y, char type){
        this.x=x;
        this.y=y;
        this.type=type;
    }

}