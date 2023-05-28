package boj.java.코딩은체육과목입니다;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    
    public static void main(String[] args) throws NumberFormatException, IOException{
	
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
        String answer = "";
        for(int i = 0; i < n / 4; i++) answer += "long "; 
        System.out.println(answer + "int");
		br.close();
	}
}
