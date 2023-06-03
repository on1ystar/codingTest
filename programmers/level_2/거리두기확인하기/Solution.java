// https://school.programmers.co.kr/learn/courses/30/lessons/81302?language=java

package level_2.거리두기확인하기;

// import java.time.Year;
import java.util.Arrays;

class Test {

    public static void main(String[] args) {
        Solution s = new Solution();
        String[][] places = {{"PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"}, {"POOPO", "OOOOO", "OOOXP", "OPOPX", "OOOOO"}, {"POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"}, {"OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"}, {"PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"}};
        System.out.println(Arrays.toString(s.solution(places)));
    }
}

/*
 * P는 응시자가 앉아있는 자리를 의미합니다.
 * O는 빈 테이블을 의미합니다.
 * X는 파티션을 의미합니다.
 */
class Solution {
    public int[] solution(String[][] places) {
        int[] answer = new int[5];

        int i = 0;
        for(String[] place : places) {
            int safe = 1;
            for(int y = 0; y < 5; y++) {
                for(int x = 0; x < 5; x++) {
                    if(place[y].charAt(x) == 'P') {
                        if(y < 4) safe *= checkDown(place, x, y);
                        if(x < 4) safe *= checkRight(place, x, y);
                        if(x > 0) safe *= checkLeft(place, x, y);
                        if(safe == 0) break;
                    }
                }
                if(safe == 0) break;
            }
            answer[i++] = safe;
        }
        return answer;
    }

    private int checkDown(String[] place, int x, int y) {
        if(place[y + 1].charAt(x) == 'O') return check(place, x, y + 2) * check(place, x + 1, y + 1) * check(place, x - 1, y + 1);
        else return check(place, x, y + 1);
    }
    private int checkRight(String[] place, int x, int y) {
        if(place[y].charAt(x + 1) == 'O') return check(place, x + 2, y) * check(place, x + 1, y + 1);
        else return check(place, x + 1, y);
    }
    private int checkLeft(String[] place, int x, int y) {
        if(place[y].charAt(x - 1) == 'O') return check(place, x - 2, y) * check(place, x - 1, y + 1);
        else return check(place, x - 1, y);
    }
    private int check(String[] place, int x, int y) {
        if(0 > x || x > 4 || y > 4) return 1;
        if(place[y].charAt(x) == 'X') return 1;
        else if(place[y].charAt(x) == 'O') return 1;
        else return 0;  // (place[y].charAt(x) == 'P')
    }
}