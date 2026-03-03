// package IntroToClasses; <- go back to packages when done
// import java.util.Scanner;

// these files are purely for study purposes. Structure aint a concern here
public class DawgGame {
	public static void main(String[] args) {
		// Scanner input = new Scanner(System.in);
		
		// System.out.println("gender?");
		// String gender = input.nextLine();
		
		// System.out.println("name?");
		// String name = input.nextLine();
		
		String gender = "boy";
		String name = "David";
		System.out.println();
		Dawg dawg = new Dawg(name, gender);
        dawg.feed();
		dawg.breathe();
		dawg.shit();
		
		Dawg anonymousDawg = new Dawg("anon", "DEATH") {
			public void ninja() {
				System.out.println(this.name + " is a ninja!");
			} // oh and, to override methods, it has to be available (PROTECTED/above)
		};
		anonymousDawg.ninja();

		try {
			int errored = 5 / 0;
			System.out.println(errored);
		}
		catch (ArithmeticException | ArrayIndexOutOfBoundsException e) {
			System.out.println("Error! " + e);
		}
		finally {
			System.out.println("try catch complete");
		}
		
		dawg.printEnums();
	}
}
// Dont forget about try with resources whenw hanlding streams, database connections, etc