
# Add Student   ✅
# Show Student  ✅
# Grade Data    ✅
# Topper        ✅ (handles multiple toppers)
#Delete Student ✅
#Search Student ✅
#Update marks   ✅
#Sort Student   ✅
#menu Function  ✅
# The menu just calls these functions based on user choice.
#----------------start task------------------------------------
import json

main_dict={}

try:
    with open("students.json", "r") as f:
        main_dict = json.load(f)
except FileNotFoundError:
    # File does not exist, start with empty dictionary
    main_dict = {}
#====================FUNCTIONS START===================
#********1st 
def Add_Student():
 print("\n*************WELCOME***************\n")
 name=input("Enter your name: ").upper()
 if(name in main_dict):#-------------for check
    print("Student is already exsist!")
 else:
  marks=int(input("Enter your marks: "))
  while True:
   if(marks<=100 and marks>=0):
    main_dict[name]=marks
    print("Entry Successfull!")
    break
   else:
    print("Wrong input for marks, Try again")
    marks=int(input("Enter your marks: "))
 with open("student.json","w")as f:
  json.dump(main_dict,f)
#**********2nd
def show_student():
  print("\n*************WELCOME***************\n")
  for i,j in main_dict.items():
    print(f"Student: {i} , Marks: {j}")
  if(main_dict=={}):
    print("no any student exsist still")

#***********3rd
def Grade_data():
  print("\n*************WELCOME***************\n")
  for name,marks in main_dict.items():
    if marks>=85:
     grade="A+"
    elif marks>=70:
     grade="A"
    elif marks>=60:
     grade="B"
    elif marks>=50:
      grade="C"
    elif marks>=40:
      grade="D"
    else:
      grade="Fail"
    print(f"{name}: {grade} ")


#***********4th
def Topper():
 print("\n*************WELCOME***************\n")
 max_mark=max(main_dict.values())
 for name,marks in main_dict.items():
  if marks== max_mark:
   print(f"Topper {name} with {marks} marks")


#************5th
def Delete_Student():
   print("\n*************WELCOME***************\n")
   name1=input("Enter name for delete record: ").upper()
   if(name1 in main_dict):
     deleted_name= main_dict.pop(name1)
     print(f"{name1}'s record is deleted")
   else:
     print("Student not found")
 
   with open("student.json","w")as f:
    json.dump(main_dict,f)  

#***********6th
def Search_Student():
 print("\n*************WELCOME***************\n")
 while True:
  name2=input("Enter name for Details:  ").upper()
  if(main_dict.get(name2)==None):
    print("Student is not found")
  else:
    print(f"{name2} has {main_dict[name2]} marks")

  print("\nDo you want to search another Student's data??")
  while True:
   choose=input("Yes (y) OR No (n): ").lower()
   if(choose=="n"):
      print("Okay thanks...")
      return 
   elif(choose!="y"):
      print("choose correct one y/n")
   else:
     Search_Student() 

   
#--------------SearchStudent end----------------------


#*************7th
def Sort_Student():
  print("\n*************WELCOME***************\n")
  #acsendingly
  # dict=sorted(main_dict.items(),key=lambda x: x[1])
  # desecedingly
  sorted_list=sorted(main_dict.items(), key=lambda x: x[1], reverse=True)
  count=1
  for key,values in sorted_list:
   print(f"{count}. {key}: {values}")
   count+=1
#***********8th
def Update_Marks():
  name=input("Enter name for update marks: ").upper()
  if(name in main_dict):#-------------for check
    marks=int(input("Enter your marks: "))
    while True:
     if(marks<=100 and marks>=0):
      main_dict[name]=marks
      print("Entry Successfull!")
      break
     else:
      print("Wrong input for marks, Try again")
      marks=int(input("Enter your new marks: "))
  else:
   print("Student does not found")
 
#************9th
def Students_statistics():
  print("\n*************WELCOME***************\n")
  No_of_Students=len(main_dict)
  maximum_mark=max(main_dict.values())
  minimum_mark=min(main_dict.values())
  Avg_mark=sum(main_dict.values())/No_of_Students
  print("The total no. of Students: ",No_of_Students)
  print("The Maximum marks is: ",maximum_mark)
  print("The Minimum marks is: ",minimum_mark)
  print("The Average marks is: ",Avg_mark)


#************Last menu function
def Menu():
   while True:
    print("\n===== Student Management System =====")

    print("1 Add Student")
    print("2 Show Students")
    print("3 Show Grades")
    print("4 Show Topper")
    print("5 Delete Student")
    print("6 Update Marks")
    print("7 Search Student")
    print("8 Sort Students by Marks")
    print("9 Students Statistics")
    print("10 Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        Add_Student()
       # menu_part()
        break
    elif choice == 2:
        show_student()
       # menu_part()
        break
    elif choice == 3:
        Grade_data()
       # menu_part()
        break
    elif choice == 4:
        Topper()
       # menu_part()
        break
    elif choice == 5:
        Delete_Student()
       # menu_part()
        break
    elif choice == 6:
        Update_Marks()
       # menu_part()
        break
    elif choice == 7:
        Search_Student()
       # menu_part()
        break
    elif choice == 8:
        Sort_Student()
       # menu_part()
        break
    elif choice == 9:
        Students_statistics()
       # menu_part()
        break    
    elif choice == 10:
        print("Program ended")
        break
    else:
        print("Invalid choice")

   while True:
    print("\n\nDo you want to back to Menu ")
    choose1=input("yes(y) / no(n): ").lower()
    if(choose1=="y"):
     Menu()
     break
    elif(choose1=="n"):
     print("Okay! thanks for visit\n")
     return
    else:
     print("choose correct one (y/n)")
 #^^^^^^^^^^ALL FUNCTIONS ARE ENDED^^^^^^^^^^^^   
Menu()