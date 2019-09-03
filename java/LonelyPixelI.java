// 531. 孤独像素 I
// https://leetcode-cn.com/problems/lonely-pixel-i/
public class LonelyPixelI {
    public int findLonelyPixel(char[][] picture) {
//        boolean[][] visit = new boolean[picture.length][picture[0].length];
//        boolean[] row = new boolean[picture.length];
//        boolean[] col = new boolean[picture[0].length];
        int result = 0;
        for (int i = 0; i < picture.length; i++) {
            int B = -1;
            for (int j = 0; j < picture[0].length; j++) {
                if (picture[i][j] == 'B') {
                    if (B == -1) {
                        B = j;
                    } else {
                        B = -1;
                        break;
                    }
                }
            }
            if (B != -1) {
                int B2 = i;
                for (int j = 0; j < picture.length; j++) {
                    if (j == i) continue;
                    if (picture[j][B] == 'B') {
                        if (j != B2) {
                            B2 = -1;
                            break;
                        }
                    }
                }
                if (B2 != -1) {
                    result++;
                }
            }
        }
        return result;
    }

    public static void main(String[] args) {
        LonelyPixelI solution = new LonelyPixelI();
        char[][] test = {{'W', 'W', 'B'},
                {'W', 'B', 'W'},
                {'B', 'W', 'W'}};
        assert solution.findLonelyPixel(test) == 3;
    }
}
