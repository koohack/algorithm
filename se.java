import java.util.Scanner;

public class se {
    static int n;
    static int[][] map;
    static int mx;
    static Scanner sc = new Scanner(System.in);
    static int[] dx = {1, -1, 0, 0};
    static int[] dy = {0, 0, 1, -1};

    public static void getInput() {
        n = sc.nextInt();
        map = new int[n][n];
        mx = 0;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                int temp = sc.nextInt();
                if (temp > mx) { mx = temp; }
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

    public static void dfs(int[][] checked, int x, int y, int num){
        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            if (0 <= nx && nx < n && 0 <= ny && ny < n && map[nx][ny] > num && checked[nx][ny] == 0){
                checked[nx][ny] = 1;
                dfs(checked, nx, ny, num);
            }
        }
    }

    public static void main(String[] args) {
        int T = sc.nextInt();

        for (int t = 0; t < T; t++) {
            int answer = 0;

            getInput();

            for (int num = 1; num < mx; num++) {
                int[][] checked = new int[n][n];
                int count = 0;

                for (int i = 0; i < n; i++) {
                    for (int j = 0; j < n; j++) {
                        if (map[i][j] > num && checked[i][j] == 0){
                            count += 1;
                            checked[i][j] = 1;
                            dfs(checked, i, j, num);
                        }
                    }
                }
                if (answer < count) { answer = count; }
            }
            System.out.println("#"+Integer.toString(t+1)+" "+Integer.toString(answer));
        }
    }




}
