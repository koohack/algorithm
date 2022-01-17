import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Stack;
import java.util.StringTokenizer;

public class num_3425 {
    static BufferedReader br;
    static StringTokenizer st;
    static String type;
    static ArrayList<String[]> list = new ArrayList<>();
    static Stack<long[]> stack = new Stack<>();
    static long N;
    static final long INF = 1000000000;

    static boolean func() {
        stack.push(new long[] {N});
        for (String[] arr : list) {
            if ("NUM".equals(arr[0])) {
                stack.push(new long[] {Long.parseLong(arr[1])});
            } else if ("POP".equals(arr[0])) {
                if (stack.isEmpty())
                    return false;
                stack.pop();
            } else if ("INV".equals(arr[0])) {
                if (stack.isEmpty())
                    return false;
                long a = stack.peek()[0];
                stack.pop();
                stack.push(new long[] {-a});
            } else if ("DUP".equals(arr[0])) {
                if (stack.isEmpty())
                    return false;
                stack.push(stack.peek());
            } else if ("SWP".equals(arr[0])) {
                if (stack.size() < 2)
                    return false;
                long num1 = stack.peek()[0];
                stack.pop();
                long num2 = stack.peek()[0];
                stack.pop();
                stack.push(new long[] {num1});
                stack.push(new long[] {num2});
            } else if ("ADD".equals(arr[0])) {
                if (stack.size() < 2)
                    return false;
                long num1 = stack.peek()[0];
                stack.pop();
                long num2 = stack.peek()[0];
                stack.pop();
                stack.push(new long[] {num1+num2});
            } else if ("SUB".equals(arr[0])) {
                if (stack.size() < 2)
                    return false;
                long num1 = stack.peek()[0];
                stack.pop();
                long num2 = stack.peek()[0];
                stack.pop();
                stack.push(new long[] {num2-num1});
            } else if ("MUL".equals(arr[0])) {
                if (stack.size() < 2)
                    return false;
                long num1 = stack.peek()[0];
                stack.pop();
                long num2 = stack.peek()[0];
                stack.pop();
                stack.push(new long[] {num1*num2});
            } else if ("DIV".equals(arr[0])) {
                if (stack.size() < 2)
                    return false;
                long num1 = stack.peek()[0];
                stack.pop();
                if (num1 == 0)
                    return false;
                long num2 = stack.peek()[0];
                stack.pop();
                stack.push(new long[] {num2/num1});
            } else if ("MOD".equals(arr[0])) {
                if (stack.size() < 2)
                    return false;
                long num1 = stack.peek()[0];
                stack.pop();
                if (num1 == 0)
                    return false;
                long num2 = stack.peek()[0];
                stack.pop();
                stack.push(new long[] {num2%num1});
            }
        }

        return true;
    }

    static void numinput() throws Exception {
        boolean chk = false;
        st = new StringTokenizer(br.readLine());

        int tc = Integer.parseInt(st.nextToken());
        while (tc-- > 0) {
            st = new StringTokenizer(br.readLine());

            N = Long.parseLong(st.nextToken());
            chk = func();
            if (!chk || stack.size() != 1) {
                System.out.println("ERROR");
            } else {
                if(Math.abs(stack.peek()[0])>INF)
                    System.out.println("ERROR");
                else
                    System.out.println(stack.peek()[0]);
            }

            while (!stack.isEmpty())
                stack.pop();
        }

        while(!list.isEmpty())
            list.remove(0);
    }

    static void typeinput() throws Exception {
        while (true) {
            st = new StringTokenizer(br.readLine());

            type = st.nextToken();
            if ("NUM".equals(type)) {
                String num = st.nextToken();
                list.add(new String[] { type, num });
            } else if ("END".equals(type) || "QUIT".equals(type)) {
                break;
            } else {
                list.add(new String[] { type });
            }
        }
    }

    public static void main(String[] args) throws Exception {
        br = new BufferedReader(new InputStreamReader(System.in));
        while (true) {
            typeinput();
            if ("QUIT".equals(type))
                break;
            numinput();
            st = new StringTokenizer(br.readLine());
            System.out.println();
        }
    }
}