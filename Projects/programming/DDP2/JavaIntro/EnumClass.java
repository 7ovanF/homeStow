// ENUM: Contains constants, is like a Class
// (can also be declared inside of class)
// automatically public, static, and final
enum EnumClass {
	// when something calls [EnumName].[CONSTNAME], it calls the constructor for that specific const
	AN_ENUM_CONSTANT(1, "A"),
	ANOTHER_ONE;

	int num;
    String str;

	private EnumClass(int num, String str) {
		this.num = num;
		this.str = str;
	}
	private EnumClass() {
		this(0, "empty");
	}

	public String getAttr() {
		return String.format("%s: %s", this.num, this.str);
	}
}