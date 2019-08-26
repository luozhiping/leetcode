// 723. 粉碎糖果
// https://leetcode-cn.com/problems/candy-crush/
public class CandyCrush {

    final static int[] DIRECTIONS_LEFT = {0, -1};
    final static int[] DIRECTIONS_RIGHT = {0, 1};
    final static int[] DIRECTIONS_TOP = {-1, 0};
    final static int[] DIRECTIONS_BOTTOM = {1, 0};


    final static int STATUS_UNVISITED = 0;
    final static int STATUS_VISITED_HORIZONTAL = 1;
    final static int STATUS_VISITED_VERTICAL = 2;
    final static int STATUS_VISITED_ALL = 3;


    public int[][] candyCrush(int[][] board) {
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j< board[0].length;j++) {
                System.out.print(board[i][j]+" ");
            }
            System.out.println();
        }
        System.out.println("=====================");

        int[][] visited = new int[board.length][board[0].length];
        boolean isDone = true;
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[0].length; j++) {
                if (visited[i][j] == STATUS_VISITED_ALL || board[i][j] == 0) {
                    continue;
                }
//                int count = 1;
                int[] rightPosition = new int[]{i, j};
                int[] leftPosition = new int[]{i, j};
                if (visited[i][j] != STATUS_VISITED_HORIZONTAL) {
                    findLine(board, DIRECTIONS_LEFT, i, j, leftPosition);
                    findLine(board, DIRECTIONS_RIGHT, i, j, rightPosition);
                    if (rightPosition[1] - leftPosition[1] >= 2) {
                        isDone = false;
                        for (int m = leftPosition[1]; m <= rightPosition[1]; m++) {
//                            board[leftPosition[0]][m] = 0;
                            if (visited[i][j] == STATUS_UNVISITED) {
                                visited[i][j] = STATUS_VISITED_HORIZONTAL;
                            } else if (visited[i][j] == STATUS_VISITED_VERTICAL) {
                                visited[i][j] = STATUS_VISITED_ALL;
                            }
                        }
                    }
                }
                int[] topPosition = new int[]{i, j};
                int[] bottomPosition = new int[]{i, j};
                if (visited[i][j] != STATUS_VISITED_VERTICAL) {
                    findLine(board, DIRECTIONS_TOP, i, j, topPosition);
                    findLine(board, DIRECTIONS_BOTTOM, i, j, bottomPosition);
                    if (bottomPosition[0] - topPosition[0] >= 2) {
                        isDone = false;
                        for (int m = topPosition[0]; m <= bottomPosition[0]; m++) {
//                            board[leftPosition[0]][m] = 0;
                            if (visited[i][j] == STATUS_UNVISITED) {
                                visited[i][j] = STATUS_VISITED_VERTICAL;
                            } else if (visited[i][j] == STATUS_VISITED_HORIZONTAL) {
                                visited[i][j] = STATUS_VISITED_ALL;
                            }
                        }
                    }
                }
            }
        }

        if (isDone) {
            return board;
        }

        for (int j = 0; j < board[0].length; j++) {
            int index = board.length - 1;
            int zeroCount = 0;
            while (index >= 0) {
                if (visited[index][j] != STATUS_UNVISITED) {
                    zeroCount++;
                    board[index][j] = 0;
                } else {
                    if (zeroCount > 0 && index + zeroCount < board.length) {
                        board[index+zeroCount][j] = board[index][j];
                        board[index][j] = 0;
                    }
                }
                index--;
            }
        }
        for (int i = 0; i < visited.length; i++) {
            for (int j = 0; j< visited[0].length;j++) {
                System.out.print(visited[i][j]+" ");
            }
            System.out.println();
        }
        System.out.println("===================");
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j< board[0].length;j++) {
                System.out.print(board[i][j]+" ");
            }
            System.out.println();
        }
        System.out.println("*******************");
        return candyCrush(board);
    }

    public void findLine(int[][] board, int[] direction, int i, int j, int[] position) {
        int cur = board[i][j];
        int[] next = {i + direction[0], j + direction[1]};
        while (!(next[0] < 0 || next[0] == board.length || next[1] < 0 || next[1] == board[0].length)) {
            if (board[next[0]][next[1]] == cur) {
//                count++;
                position[0] = next[0];
                position[1] = next[1];
            } else {
                break;
            }
            next[0] += direction[0];
            next[1] += direction[1];
        }
    }

    public static void main(String[] args) {
        CandyCrush solution = new CandyCrush();
//        int[][] test = {{110,5,112,113,114},{210,211,5,213,214},{310,311,3,313,314},{410,411,412,5,414},{5,1,512,3,3},{610,4,1,613,614},{710,1,2,713,714},{810,1,2,1,1},{1,1,2,2,2},{4,1,4,4,1014}};
//        int[][] test = {{5,5,5,3,2},{3,4,3,2,4},{3,2,3,4,2},{1,1,2,3,1},{5,3,4,4,3}};
        int[][] test = {{1,3,2,4,3},{2,3,2,3,2},{4,4,2,5,4},{1,2,4,2,4},{3,3,5,5,1}};
        solution.candyCrush(test);
        for (int i = 0; i < test.length; i++) {
            for (int j = 0; j< test[0].length;j++) {
                System.out.print(test[i][j]+" ");
            }
            System.out.println();
        }
    }
}
