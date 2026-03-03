public class OldDawg extends ParentClass {
	// ENCAPSULATION! control the readabilty and modifiability of attributes.
	private String name;
	private String gender;
	private int aff_level;
	
	public OldDawg(String name, String gender) {
		// need to initialize parent manually. (also, to use *this* keyword, super() needs to be initalized first)
		super("Creatin' Dawg!");
		
		this.name = name;
		this.gender = gender;
		this.aff_level = 0;
		System.out.println(String.format("%s, the good %s, has awakened!", 
		    this.name, this.gender));
	}
	
	// turns out main is not mandatory
	
	// getters (encapsulation)
	public String getName() {
		return this.name;
	}
	public String getGender() {
		return this.gender;
	}
	public int getAffinityLevel() {
		return this.aff_level;
	}
	
	public void feed() {
		// you can use System.out.printf instead (needs to add %n for newline)
        System.out.println(String.format("%s has been fed. %s is a happy %s.",
        	this.name, this.name, this.gender));
		this.increase_aff_level(5);
	}
	
	private void increase_aff_level(int levels) {
		this.aff_level += levels;
		System.out.println(String.format("%s's affinity level is now %d!", this.name, this.aff_level));
	}
	
	public void printParent() {
		System.out.println("\n" + this.attr);
		this.doSomething(this.aff_level);
		System.out.println(super.getName()); // the super keyword
		
		// inner
		// InnerClass.innerMethod(); // doesnt work bc private. else, it does
	}
}