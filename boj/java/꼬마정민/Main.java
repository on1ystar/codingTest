package boj.java.꼬마정민;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main{
	public static void main(String[] args) throws NumberFormatException, IOException{
	
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] abc = br.readLine().split(" ");
		long result = 0L;
		for (String str : abc) {
			result += Long.parseLong(str);
		}
		System.out.println(result);
		br.close();
	}
}