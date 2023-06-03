import java.util.Arrays;

class Solution {
    public int[] solution(long n) {
        String str = Long.toString(n);
        int[] answer = new int[str.length()];
        for (int i = str.length() - 1; i >= 0; i--) {
            answer[str.length() - i - 1] = str.charAt(i) - '0';
        }
        return answer;
    }
}

class Test {
    public static void main(String[] args) {
        Solution s = new Solution();
        s.solution(12345);
    }
}