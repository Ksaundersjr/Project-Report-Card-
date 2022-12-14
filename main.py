################ Function Definitions ################
print("--------------------------------- Report Card----------------------------------")


# Shows the user what options they have
def displayMenu():

  # This option will involve you adding a student and a collection for their grades to a dictionary!
  print("1. Add a Student")


  # This option will involve you removing a pair from a dictionary!
  print("2. Remove a Student")

  # This option will require you to grab a student from a dictionary and add a quiz grade to it's corresponding collection of grades!
  # You'll also need to use a pre-written function that ensures the user is entering a valid grade (a decimal number)
  print("3. Add Quiz Grade for Student")
  

  # This option will require you to use a loop to list all of the grades for an INDIVIDUAL student!
  print("4. List a Student's Quiz Grades")

  # This option will have you write a function that takes in a student's grade as a number and return the letter grade equivalent!
  print("5. Get Student's Letter Grade")

  print("6. Quit")

# Prompts the user to enter a numeric grade
# This function works, and ensures the user entered a valid float for the grade
# It's not important HOW this function works, but how to USE this function
def getNumberGradeFromUser():

  val = None

  while(val == None):
    try:
      test = float(input("Enter a Grade: "))
      val = test
    except:
      val = None
  
  return val

################ Main Program ################

# Create an empty dictionary to collect student information (name, grades) 
studentDict = {}
option = ""

# Application Loop
while(option != "6"):

  # Prompt the user to select an option
  print()
  displayMenu()

  # Get the user's selection
  option = input("Enter your option: ")

######## Option 1: Add a student ########
  if(option == "1"):

    # Prompt for a student name
    name = input("Enter a student name:  ") 

    # Add that student
    studentDict[name] = []

  # else: print("This student does not exist")
    
####### Option 2: Remove a student #######
  elif(option == "2"):
  
    # Prompt for student name 
    name = input("Enter a student name: ")
    studentDict.pop(name)
    print(f"{name} has been removed")


######## Option 3: Add a grade ##########
  elif(option == "3"):

    # Prompt for student name 
    name = input("Enter a student name:  ") 

    # Add grade to the dictionary 
    if name in studentDict :
      myGrade = getNumberGradeFromUser()
      studentDict[name].append(myGrade)

      # Display the grade has been added 
      print(f"The following grade {myGrade} has been added to {name} Quizzes ")

    else: print("This student does not exist")

######## Option 4 : List the Grades #########
  elif(option == "4"):

    # Prompt for student name 
    name = input("Enter a student name:  ") 
    if name in studentDict :

      # Display the Student's Grades 
      print (f"{name} Quiz Grades:")
      for myGrade in studentDict[name]: 
        print(myGrade)

    else: print("This student does not exist ")

######## Option 5 : Display student's letter grade ########
  elif (option == "5"):

    # Promt user to enter name
    name = input("Enter a student name: ")
    if name in studentDict: 

      # Create dummy variables for sum and count .. 
      count = 0 
      sum = 0
       
      for myGrade in studentDict[name]:
       
        sum += (myGrade) 
        count += 1

      avgGrade = sum / count
      
# # sumGrade = sum /count 
    if (myGrade > 90):
      print("A")
    elif(myGrade > 80):
      print("B")
    elif(myGrade > 70):
      print("C")
    elif(myGrade <= 69):
      print("Failed")
      