public class Dawg extends Animal implements AnimalStuff {
	// ENCAPSULATION! control the readabilty and modifiability of attributes.
	
	public Dawg(String name, String gender) {
		// need to initialize parent manually. (also, to use *this* keyword, super() needs to be initalized first)
		// abstract class exclusive: you can still instantiate it to assign variables.
		super(name, gender);
		System.out.println(String.format("%s, the good %s, has awakened!", 
		    this.name, this.gender));
	}
	
	// turns out main is not mandatory
	
	public void feed() {
		// you can use System.out.printf instead (needs to add %n for newline)
        System.out.println(String.format("%s has been fed. %s is a happy %s.",
        	this.name, this.name, this.gender));
		this.increaseAffLevel(5);
	}
	
	private void increaseAffLevel(int levels) {
		this.aff_level += levels;
		System.out.println(String.format("%s's affinity level is now %d!", this.name, this.aff_level));
	}
	
	public void shit() {
		System.out.println("brughrughruheijrie");
	}
	
	public void breathe() {
		System.out.println("hhhssshgsuhhehssss");
	}
	
	protected void ninja() { // any of these are normal methods, but u can override them 
	    // on a whim for a certain class with ANONYMOUS CLASSES
		System.out.println(String.format("No, %s is not a ninja...", this.name));
	}
	
	public void printEnums() {
		System.out.println(EnumClass.AN_ENUM_CONSTANT);
		System.out.println(EnumClass.AN_ENUM_CONSTANT.getAttr());
		for (EnumClass constant: EnumClass.values()){
			System.out.println(constant);
		}
	}
}