package Files;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

// i forgor abt methods :skull:
public class FileWriting {
	private static final String FILE_NAME = "file.txt";
	
    public static void main(String[] args) {
        // try except is necessary if the file creation runs into an error
		Scanner scanner = new Scanner(System.in);
        try {
			// File initialization
			File file = new File(FILE_NAME);
			if (file.createNewFile()) {
				System.out.println("Created file");
			} else {
				System.out.println("File already exists");
			}
			System.out.println();
			
			// Write to file
			try (FileWriter writer = new FileWriter(FILE_NAME, true)) {
				boolean writing = true;
				while (writing) {
					System.out.println("Write a new line: ");
					String newLine = scanner.nextLine();
					
					writer.write(newLine + System.lineSeparator());

					System.out.println("\nSuccessfully written new line.");
					System.out.print("\nContinue writing? (y/n): ");
					String confirmation = scanner.nextLine();
					// cant directly do a != comparison on String.
					if (!confirmation.equalsIgnoreCase("y")) {
						writing = false;
						System.out.println("Program finished.");
					}
				}
			} // both catches will be handled by the one below
		} catch (IOException e) {
			System.out.println("An Error occured");
			e.printStackTrace(); // Print details
		} finally {
			scanner.close();
		}
    }
}
