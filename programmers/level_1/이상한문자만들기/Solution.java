// https://school.programmers.co.kr/learn/courses/30/lessons/12930

package level_1.이상한문자만들기;

import java.util.Arrays;

class Solution {
    public String solution(String s) {
        String answer = "";
        int j = 0;
        for (int i = 0; i < s.length(); i++) {
            if(s.charAt(i) == ' ') {
                answer += " ";
                j = 0;
            }
            else {
                answer += j % 2 == 0 ? Character.toUpperCase(s.charAt(i)) : Character.toLowerCase(s.charAt(i));
                j++;
            }
        }
        answer += " ";
        return answer.substring(0, answer.length() - 1);
    }
}

// class Solution {
//   public String solution(String s) {

//         String answer = "";
//         int cnt = 0;
//         String[] array = s.split("");
//         for(String ss : array) {
//             cnt = ss.contains(" ") ? 0 : cnt + 1;
//             answer += cnt%2 == 0 ? ss.toLowerCase() : ss.toUpperCase(); 
//         }
//       return answer;
//   }
// }

class Test {
    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.solution(" s sss   "));
    }
}