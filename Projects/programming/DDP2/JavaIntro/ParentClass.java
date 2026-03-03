
public class ParentClass {
	protected String attr;
	protected static String staticAttr = "Static attr!";
	
	public ParentClass(String attr) {
		this.attr = attr;
		System.out.println(this.attr);
		
	    System.out.println(InnerClass.attr);
		
		// Staticity! dont read if u think ur gonna get confused from this
		InnerClass inner = new InnerClass(); // wait, why this still workin? aint it static
		System.out.println(inner.innerUnstaticAttr); // this works
		System.out.println(inner.attr); // this works as well (natuarlly, from instance to class)
		inner.innerUnstaticMethod(); // this properly calls it as well. more explanation below
		
		InnerClass.innerMethod();
		System.out.println();
	}
	protected void doSomething(int x) {
		System.out.println(x * 5);
	}
	public String getName() {
		return "My name is Vlad"; // POLYMORPHISM: this method has been "overwritten" by the one in Dawg.java
	} // can still be called with super.getName(); 
	// overwriting also applies to attributes
	
	
	// Inner Classes! or Nested Class.
	// + Big insight on staticity!
	private static class InnerClass { // private inner classes CAN be used by the outer! (since its the same file)
	    private static String attr = "InnerClass's attr!"; // static attr!
		private String innerUnstaticAttr = "huh, very static indeed"; // this aint a static
		
		private static void innerMethod() {
			System.out.println(ParentClass.staticAttr); // explicit calling. for non-static, use ParentName.this.attrName
		}
		// AND... Inner can access Outer's private!
		
		private void innerUnstaticMethod() {
			// System.out.println(ParentClass.this.attr); // this doesnt work. soo...
			// a static class will make all occurences (methods, etc) inside it static too.
		}
		
		/* STATIC VS NON-STATIC
		Static == Class, Non-static == Instance.
		From an instance you can access class attrs (and modify them, and class changes will be 
		shared between all instances.)
		However, from a static state (class) you can't access instances.
		*/
	}
}