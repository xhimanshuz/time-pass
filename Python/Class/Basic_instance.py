#/bin/usr/python

class Employee:
	def __init__(self, name, lname, payee):
		self.name = name
		self.lname = lname
		self.payee = payee
		self.email = "{}.{}@chutiyapa.com".format(name, lname)

	def fullname(self):
		return "{} {}".format(self.name, self.lname)

	def fulldetail(self):
		return "First Name: {} \nLast Name: {}\nE-Mail: {}\nPayee: {}".format(self.name, self.lname, self.email, self.payee)


# DEVELOPER CLASS WITH EMPLOYEE CLASS PROPERTY
class Developer(Employee):
	def __init__(self, name, lname, payee, language):
		super().__init__(name, lname, payee)
		self.language = language
	def fulldetail(self):
		print( super().fulldetail() + "\nProgramming Language: {}".format(self.language))


# MANAGER CLASS WITH EMPLOYEE CLASS PROPERTY
class Manager(Employee):
	def __init__(self, name, lname, payee, employee=None):
		super().__init__(name, lname, payee)
		if employee is None:
			self.employee = []
		else:
			self.employee = employee
	def add_emp(self, emp):
		if emp not in self.employee:
			self.employee.append(emp)

	def remove_emp(self, emp):
		if emp in self.employee:
			self.employee.remove(emp)
		else:
			print("ERROR:404 - Employee Not Found!")
	
	def showemployee(self):
		for emp in self.employee:
			print("|-->", emp.fullname())
							 
#-----MAIN FUNCTION-----#
#def main():
	
rahul = Developer("Rahul", "Aggarwal", 100000, "Java")
ujjawal = Developer("Kumar", "Ujjawal", 100000, "Swift")
#ujjawal.fullname()
mukul = Manager("Mukul","Aswal",100000, [rahul])
print(mukul.email)
mukul.add_emp(ujjawal)
mukul.showemployee()
mukul.remove_emp(rahul)
print("-----Removed-----")
mukul.showemployee()

#main()
