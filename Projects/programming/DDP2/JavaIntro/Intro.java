public class Intro {
    public static void main(String[] args) {
        System.out.println("Hello Java!");
        // forloop();
        // whileloop();
        // arrays();
		String result = mom_told_me_to_make_a_method_that_reverses_a_string("Jeez this is cancer");
		System.out.println(result);
    }
    public static void forloop() {
        for (int i = 0; i < 5; i++) {
            System.out.print("halo! ");
        }
        System.out.println();
        
        // size of stuff
        final int SIZE = 5;
        
        // print out triangle
        for (int row = 1; row <= SIZE; row++) {
            int spaces = SIZE - row;
            int stars = row;
            for (int i = 0; i < spaces; i++) {
                System.out.print(' ');
            }
            for (int i = 0; i < stars; i++) {
                System.out.print('*');
            }
            System.out.println();
        }
        
        // print out diamond
        for (int row = 0; row < SIZE; row++){
            int spaces = Math.abs((SIZE / 2) - row);
            /* integer / integer will result in integer */
            int stars = SIZE - (2 * spaces);
            for (int i = 0; i < spaces; i++) {
                System.out.print(' ');
            }
            for (int i = 0; i < stars; i++) {
                System.out.print('*');
            }
            System.out.println();
        }       
    }
    public static void whileloop() {
        // interesting thing: do/while loop
        int n = 57;
        do {
            n -= 8;
            System.out.println(n);
        } while (n > 0);
        System.out.println();
    }
    public static void arrays() {
        int[] nums = {4,2,5,6};
        int total = sumall(nums);
        System.out.println(total);
		
        // print inverse of a matrix
        int[][] matrix= {{1, 2, 3}, {4, 5, 6}};
        for (int col_n = 0; col_n < matrix[0].length; col_n ++) {
            for (int[] row: matrix) {
                System.out.print(row[col_n] + " ");
            }
            System.out.println();
        }
    }
    public static int sumall(int[] nums) {
        int total = 0;
        for (int num: nums) {
            total += num;
        }
		return total;
    }
	public static String mom_told_me_to_make_a_method_that_reverses_a_string(String str) {
		int str_length = str.length();
		
		String[] str_array = new String[str_length];
		for (int i = 0; i < str_length; i += 1) {
			int new_index = str_length - 1 - i;
			// sin 1: had to convert char to String
			str_array[new_index] = String.valueOf(str.charAt(i));
		}
		// sin 2: had to search up how to join
		return String.join("", str_array);
		
		
		/* // sad attempt at recursion
		if (str.length <= 0) {
			return "";
		} else {
			// ...now how the hell do i slice
			return mom_told_me_to_make_a_method_that_reverses_a_string(slice here) + str.charAt(0);
		} */
	}
}