// https://school.programmers.co.kr/learn/courses/30/lessons/68645

package programmers.level_2.삼각달팽이;

class Test {

    public static void main(String[] args) {
        Solution s = new Solution();
        int[] answer = s.solution(5);
        for (int a : answer) {
            System.out.print(a + ", ");           
        }
        System.out.println();
    }
}

class Solution {
    
    int[][] triangle;
    int currentHeightIndex = 0;
    int currentWidthIndex = 0;
    int currentNumber = 0;
    
    public int[] solution(int n) {
        triangle = new int[n][n];
        int lastNumber = n * (n + 1) / 2;
        int[] answer = new int[lastNumber];
        while(n >= 1) {
            down(n);
            if(checkNumber(lastNumber)) break;
            right(n);
            if(checkNumber(lastNumber)) break;
            up(n);
            if(checkNumber(lastNumber)) break;
            n -= 3;
        }
        int k = 0;
        for(int i = 0; i < triangle.length; i++) {
            for(int j = 0; j < i + 1; j++) {
                answer[k] = triangle[i][j];
                k++;
            }
        }

        return answer;
    }

    public void down(int n){
        for(int i = 0; i < n -1; i++) {
            currentNumber++;
            triangle[currentHeightIndex][currentWidthIndex] = currentNumber;
            currentHeightIndex++;            
        }
    }

    public void right(int n){
        for(int i = 0; i < n -1; i++) {
            currentNumber++;
            triangle[currentHeightIndex][currentWidthIndex] = currentNumber;
            currentWidthIndex++;            
        }
    }

    public void up(int n){
        for(int i = 0; i < n -2; i++) {
            currentNumber++;
            triangle[currentHeightIndex][currentWidthIndex] = currentNumber;
            currentHeightIndex--;            
            currentWidthIndex--;            
        }
        currentNumber++;
        triangle[currentHeightIndex][currentWidthIndex] = currentNumber;
        currentHeightIndex++;
    }

    boolean checkNumber(int lastNumber) {
        return currentNumber == lastNumber;
    } 

}
