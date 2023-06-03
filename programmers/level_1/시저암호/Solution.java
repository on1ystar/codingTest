// https://school.programmers.co.kr/learn/courses/30/lessons/12926
package level_1.시저암호;

class Solution {
    public String solution(String s, int n) {
        StringBuilder answer = new StringBuilder(s.length());
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if(c == ' ') answer.append(c);
            else if('A' <= c && c <= 'Z') {
                if(c + n <= 'Z') answer.append((char) (c + n));
                else answer.append((char) (c + n - 26));
            }
            else {
                if(c + n <= 'z') answer.append((char) (c + n));
                else answer.append((char) (c + n - 26));
            }
        }
        return answer.toString();
    }
}

class Test {
    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.solution("ABwxyz", 1));
    }
}