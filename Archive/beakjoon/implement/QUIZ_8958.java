import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class QUIZ_8958 {
    public static void main(String[] args) throws IOException {

        BufferedReader _input = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer tokenizer = new StringTokenizer(_input.readLine());
        int N = Integer.parseInt(tokenizer.nextToken());
        String[] answers = new String[N];
        for(int i = 0; i < N; i++){
            tokenizer = new StringTokenizer(_input.readLine());
            answers[i] = tokenizer.nextToken();
        }

        for(String answer: answers){
            int sum = 0;
            char[] target = answer.toCharArray();
            int counter = 0;
            for(int i = 0; i < target.length; i++){
                if(target[i] == 'O'){
                    counter += 1;
                    sum += counter;
                }else{
                    counter = 0;
                }
            }
            System.out.println(sum);
        }

        _input.close();
    }
}
