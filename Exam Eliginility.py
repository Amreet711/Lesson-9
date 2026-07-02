#Asking if the studdent has a medical condition
medical_condition=input("Do you have a medical condition? Y/N")
#Condition
if medical_condition == "Y":
    print("Student it allowed to give the exam")
else:
    attendence=int(input("What is your attendence percentage?"))
    if attendence >= 75:
        print("Student is allowed to give the exam")
    else:
        print("Student is not allowed to give the exam")