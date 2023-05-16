package codingtest.programmers.level_2.교점에별만들기;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {

    public static void main(String[] args) {
        // int[][] line = {{2, -1, 4}, {-2, -1, 4}, {0, -1, 1}, {5, -8, -12}, {5, 8, 12}};
        int[][] line = {{0, 1, -1}, {1, 0, -1}, {1, 0, 1}};
        

        CoordinatePlane coordinatePlane = new CoordinatePlane();

        for(int i = 0; i < line.length - 1; i++) {
            Line lineA = new Line(line[i]);
            for(int j = i+1; j < line.length; j++) {
                Line lineB = new Line(line[j]);
                Point p = Line.findIntersection(lineA, lineB);
                if(p != null) {
                    coordinatePlane.addIntersection(p);
                }
            }
        }

        String[] answer = coordinatePlane.print();
        for(String str : answer) {
            System.out.println(str);
        }
    }

    public String[] solution(int[][] line) {
        CoordinatePlane coordinatePlane = new CoordinatePlane();

        for(int i = 0; i < line.length - 1; i++) {
            Line lineA = new Line(line[i]);
            for(int j = i+1; j < line.length; j++) {
                Line lineB = new Line(line[j]);
                Point p = Line.findIntersection(lineA, lineB);
                if(p != null) {
                    coordinatePlane.addIntersection(p);
                }
            }
        }

        return coordinatePlane.print();
    }
}

class Point {
    
    int x;
    int y;

    public Point(int x, int y) {
        this.x = x;
        this.y = y;
    }
}

class Line {

    int a;  // x의 계수(A)
    int b;  // y의 계수(B)
    int c;  // 상수(C)

    public Line(int[] l) {
        this.a = l[0];
        this.b = l[1];
        this.c = l[2];
    }
 
    /*
     * 공식으로 두 직선의 교점 구하기
     * Ax + By + E = 0
     * Cx + Dy + F = 0
     */
    public static Point findIntersection(Line line1, Line line2) {
        // AD - BC
        double denominator = line1.a * line2.b - line1.b * line2.a;  // 분모
        
        // 분모가 0이면 두 직선은 평행 또는 일치
        if(denominator == 0) {
            return null;
        }

        double x = (line1.b * line2.c - line1.c * line2.b) / denominator;  // 교점의 x 좌표
        double y = (line1.c * line2.a - line1.a * line2.c) / denominator;  // 교점의 y 좌표

        // 좌표 값이 정수가 아닌 경우
        if( (int) x != x || (int) y != y ) {
            return null;
        }

        return new Point((int) x, (int) y);
    }
}

/*
 * 교점들을 포함하고 있는 좌표 평면
 */
class CoordinatePlane {

    int maxX = -1_000_000;  // 교점들 중 x 최댓값
    int maxY = -1_000_000;;  // 교점들 중 y 최댓값
    int minX = 1_000_000;;  // 교점들 중 x 최솟값
    int minY = 1_000_000;;  // 교점들 중 y 최솟값
    List<Point> intersections = new ArrayList<>();  // 교점

    public void addIntersection(Point p) {
        intersections.add(p);
        checkMaxMin(p);
    }

    private void checkMaxMin(Point p) {
        if(maxX < p.x) maxX = p.x;
        if(maxY < p.y) maxY = p.y;
        if(minX > p.x) minX = p.x;
        if(minY > p.y) minY = p.y;
    }

    // 좌표 평면에 교점 그리기
    public String[] print() {
        int height = maxY - minY + 1;    // 최소 사각형의 세로 크기
        int width = maxX - minX + 1;     // 최소 사각형의 가로 크기
        String[] answer = new String[height];
        Arrays.fill(answer, ".".repeat(width));
        intersections.forEach(point -> {
            int yIndex = Math.abs(point.y - maxY);  // String 배열에서의 y 좌표 위치(행)
            int xIndex = point.x - minX;            // String 배열에서의 x 좌표 위치(열)
            try {
                answer[yIndex] = answer[yIndex].substring(0, xIndex) + "*" + answer[yIndex].substring(xIndex + 1);
            } catch (StringIndexOutOfBoundsException e) {
                answer[yIndex] = answer[yIndex].substring(0, xIndex) + "*";
            }
        });
        return answer;
    }
}