/* Lisences
bla bla bla
*/

package Files;

import java.io.BufferedWriter;
import java.io.File;
import java.util.Scanner;
import java.io.IOException;

public class TextEditor {
    public static void main(String[] args) {
        /*
        steps:
        1. specify filename
        2. create/just write
        3. read content
        4. make custom syntaxes for actions:
            write to specified (or last) line
            append after specified line
            delete specified or last line
            quit*/
        System.out.println("Line Editor\n");
        try (Scanner input = new Scanner(System.in)) {
            System.out.print("Enter text file name: ");
            final String FILE_NAME = input.nextLine();

            File file = new File(FILE_NAME); // kinda ancient now, optimizing to modern is a headache
            if (file.createNewFile()) {
                System.out.println("Successfully created file.\n");
            } else {
                System.out.println("File found. Reading file...\n");
                readFile(file);
            }

            // File Editing Section
            boolean editing = true;
            try (BufferedWriter writer = new BufferedWriter(FileWriter(FILE_NAME))) {
                while (editing) {
                    System.out.print(": ");
                    String actionCode = input.nextLine();

                    char action = actionCode.charAt(0);
                    switch (action) {
                        case 'w':
                            System.out.println("writing");
                            break;
                        case 'a':
                            System.out.println("appending");
                            break;
                        case 'd':
                            System.out.println("deleting");
                            break;
                        case 'q':
                            editing = false;
                            System.out.println("Program finished");
                        default:
                            System.out.println("wong");
                    }
                }
            }
        } catch (IOException e) {
            System.out.print("Something went wrong:");
            e.printStackTrace();
        }
    }

    private static void handleWrite

    private static void readFile(File file) {
        int lineNumber = 0;
        try (Scanner read = new Scanner(file)) {
            while (read.hasNextLine()) {
                lineNumber ++;
                String line = read.nextLine();
                System.out.printf("%-4d%s%n", lineNumber, line);
            }
        } catch (IOException e) {
            System.out.print("Something went wrong:");
            e.printStackTrace();
        }
    } 
}

/* notes:
- FileWriter vs BufferedWriter:
  both are i/o streams
  difference just sits in buffering (Buffered can still be flushed)
  generally BufferedWriter is better
 */