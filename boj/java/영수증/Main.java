package boj.java.영수증;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    
    public static void main(String[] args) throws NumberFormatException, IOException{
	
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int totalPrice = Integer.parseInt(br.readLine());
		int productNum = Integer.parseInt(br.readLine());
        int temp = 0;
        for(int i = 0; i < productNum; i++) {
            String[] line = br.readLine().split(" ");
            temp += Integer.valueOf(line[0]) * Integer.valueOf(line[1]);
        }
        if(temp == totalPrice) System.out.println("Yes");
		else System.out.println("No");
		br.close();
	}
}
