class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def __init__(self, firstName, lastName, idNum, scores):
        Person.__init__(self, firstName, lastName, idNum)
        self.scores = scores
	


    def calculate(self):
        y = sum(scores) / len(scores)

        if 90<= y <= 100:
            return 'O'
        elif 80<= y < 90:
            return 'E'
        elif 70<= y < 80:
            return 'A'
        elif 55<= y < 70:
            return 'P'
        elif 40<= y < 55:
            return 'D'
        elif y < 40:
            return 'T'
        
line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
scores = list(map(int, input().split()))
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())