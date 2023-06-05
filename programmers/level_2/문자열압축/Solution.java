// https://school.programmers.co.kr/learn/courses/30/lessons/60057?language=java

package level_2.문자열압축;

class Solution {
    public int solution(String s) {
        int answer = s.length(), reCount = 1;
        String compressingStr = "", compressedStr = "";
        for(int slicedLen = 1; slicedLen <= s.length() / 2; slicedLen++) {
            String str = "";
            for(int i = 0; i < s.length() ; i += slicedLen) {
                str = i+slicedLen <= s.length() ? s.substring(i, i+slicedLen) : s.substring(i);
                if(compressingStr.equals("")) compressingStr = str;
                else if(compressingStr.equals(str)) reCount++;
                else {
                    compressedStr += reCount == 1 ? compressingStr : reCount + compressingStr;
                    compressingStr = str;
                    reCount = 1;
                }
            }
            if(compressingStr.length() != 0) {
                compressedStr += reCount == 1 ? compressingStr : reCount + compressingStr;
                compressingStr = "";
                reCount = 1;
            }
            if(compressedStr.length() < answer) answer = compressedStr.length();
            compressedStr = "";
        }
        return answer;
    }
}

class Test {

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.solution("aabbaccc"));
    }
}