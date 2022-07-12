import java.awt.*;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class water {


    static int n;
    static int[][] map;
    static int mx;
    static Scanner sc = new Scanner(System.in);

    public static void getInput() {
        n = sc.nextInt();
        map = new int[n][n];
        mx = 0;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                int temp = sc.nextInt();
                if (temp > mx) {
                    mx = temp;
                }
                map[i][j] = temp;
            }
        }
    }

    public static void print(int[][] line){
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                System.out.print(Integer.toString(line[i][j]) + " ");
            }
            System.out.println();
        }
    }

    public static void main(String[] args){
        int T = sc.nextInt();

        int[] dx = {1, -1, 0, 0};
        int[] dy = {0, 0, 1, -1};

        for (int t = 0; t < T; t++) {
            int answer = 0;

            getInput();

            for (int num = 1; num < mx + 1; num++) {
                Queue<Integer> q = new LinkedList<Integer>();

                int [][] checked = new int[n][n];

                int count = 0;

                for (int i = 0; i < n; i++) {
                    for (int j = 0; j < n; j++) {
                        if (map[i][j] > num && checked[i][j] == 0) {
                            checked[i][j] = 1;
                            count += 1;

                            q.add(i);
                            q.add(j);

                            while (!q.isEmpty()) {
                                int x = q.remove();
                                int y = q.remove();
                                checked[x][y] = 1;

                                //System.out.println(Integer.toString(x) + " " + Integer.toString(y));
                                for (int k = 0; k < 4; k++) {
                                    int nx = x + dx[k];
                                    int ny = y + dy[k];
                                    if (0 <= nx && nx < n && 0 <= ny && ny < n && map[nx][ny] > num && checked[nx][ny] == 0) {
                                        q.add(nx);
                                        q.add(ny);
                                    }
                                }
                            }
                        }
                    }
                }
                print(checked);
                System.out.println(count);
                System.out.println("------------");
                if (answer < count){ answer = count; }
            }
            System.out.println("#"+Integer.toString(t+1)+" "+Integer.toString(answer));
        }
    }
}
