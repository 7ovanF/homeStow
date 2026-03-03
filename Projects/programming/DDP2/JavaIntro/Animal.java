public abstract class Animal{
    // Abstract classes cant be instantiated.
	// (But it can; only constructing from the subclass works [like super()])
	// Sort of a template
	
	protected String name;
	protected String gender;
	protected int aff_level;
	
	protected Animal(String name, String gender) {
    	this.name = name;
		this.gender = gender;
		this.aff_level = 0;
	}
	
	// abstract methods MUST be implemented
	protected abstract void feed(); // cant be private, btw
	// when implemented, it can become more accessible (protected->public), but not less
	
	// it can also have normal methods
	public String getName() {
		return this.name;
	}
	public String getGender() {
		return this.gender;
	}
	public int getAffinityLevel() {
		return this.aff_level;
	}
}