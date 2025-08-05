
gradebook = {}
detail = {}

print('''** Options **
1: View All Records
2: Add New Student
3: Add/Update Subject Grade
4: Remove Student
5: Calculate Average Grade
6: Exit''')

while True:
    option = int(input("Enter the option: "))
    if option == 1:
        print(gradebook)
    elif option == 2:
        student = input("Enter the name of the student: ")
        if student == "":
            print("The Input is empty")
            continue
        else:
            detail = {}
        gradebook[student] = detail
    elif option == 3:
        updateStudent = input("Enter the name of the student to update: ")
        if updateStudent not in gradebook:
            print("Student Not Found !")
            continue
        else:
            subject = input("Enter the name of subject: ")
        try:
            mark = int(input("Enter the marks: "))
            if 0 <= mark <= 100:
                print('Entered grades are valid')
                break
            else:
                print('The entered grades are out of the range:0-100')
        except ValueError:
            print("The entered data is non-numeric! Please try again")
        else:
            gradebook[updateStudent][subject] = mark
    elif option == 4:
        rstudent = input("Enter the name of the student to remove: ")
        if rstudent not in gradebook:
            print('Student Not Found !')
        else:
            gradebook.pop(rstudent)
    elif option == 5:
        avgstudent = input("Enter the student's name: ")
        averageMarks = (sum(gradebook[avgstudent]))/len(detail)
        print("The average marks of ",avgstudent," is ",averageMarks)
    elif option == 6:
        print("Exiting the Gradebook...")
        break



