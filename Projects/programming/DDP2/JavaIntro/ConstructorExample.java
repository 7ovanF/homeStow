public class ConstructorExample {
    // 1. DEFAULT VALUES (before anything runs)
    // All instance fields set to: 
    // int = 0, boolean = false, Object = null, etc.
    
    // 2. FIELD INITIALIZERS (in declaration order)
    private int a = 5;                 // a becomes 5
    private String b = "hello";        // b becomes "hello"
    
    // 3. INSTANCE INITIALIZER BLOCKS (in code order)
    {
        System.out.println("Initializer block 1");
        a = 10;  // Can override earlier value
    }
    
    // 4. CONSTRUCTOR EXECUTION
    public ConstructorExample() {
        // super();  // First line (implicit or explicit) - calls parent constructor
        
        // Constructor body runs
        System.out.println("Constructor body");
        a = 20;  // Can override all previous values
    }
    
    // 5. MORE INITIALIZER BLOCKS? (they run BEFORE constructor body)
    {
        System.out.println("Initializer block 2");
    }

    // Just the main
    public static void main(String[] args) {
        ConstructorExample obj = new ConstructorExample();
        System.out.println(obj.getClass());
    }
}