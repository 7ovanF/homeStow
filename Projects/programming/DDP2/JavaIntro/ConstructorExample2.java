class Parent {
    private static String staticField = "Static Parent Field";
    private String parentField = "Parent Field";
    
    static {
        System.out.println("Parent static block: " + staticField);
    } // static "constructor"; this WILL be called even when theres no instantiation
    
    {
        System.out.println("Parent instance block: " + parentField);
    }
    
    public Parent() {
        System.out.println("Parent constructor");
    }
}

class ConstructorExample2 extends Parent {
    private static String staticField = "Static Child Field";
    private String childField = "Child Field";
    
    static {
        System.out.println("Child static block: " + staticField);
    }
    
    {
        System.out.println("Child instance block: " + childField);
    }
    
    public ConstructorExample2() {
        System.out.println("Child constructor");
    }

    public static void main(String[] args) {
        new ConstructorExample2();
    }
}

// When calling: new Child();
// OUTPUT:
// Parent static block: Static Parent Field
// Child static block: Static Child Field
// Parent instance block: Parent Field
// Parent constructor
// Child instance block: Child Field
// Child constructor