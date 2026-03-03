class Pecahan:
	def __init__(self, num, denum):
	    self.__num = num
		self.__denum = denum
		
    def get_num(self):
	    return self.__num # 1
		
	def get_denum(self):
		return self.__denum # 2
        
    def get_decimal(self):
        return self.__num / self.__denum # 0.5
	
    def __str__(self):
	    return f"{self.__num}/{self.__denum}"
        
    def __add__(self, other_pecahan):
        top = self
        bot = 
        result = Pecahan(top, bot)
        
        return
        
    def sederhanakan(self):
        a = self.__num
        b = self.__denum
        while b != 0:
            a, b = b, a % b
            
        self.__num // a
        return
        
    def fpb(self):
        a = self.__num
        b = self.__denum
        while b != 0:
            a, b = b, a % b
        return a