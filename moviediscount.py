#ask the user to input their age
age = int(input("Enter your age: "))

#ask the user to input if they are student or not
student = input("Are you a student?(yes/no): ")

#determinding if they are eligible for the discount or not base on their age and base on whether they are student or not
if age <= 12 or (13 <= age <= 18 and student == 'yes'):
    print("you are eligible for a discount on the movie ticket.")
else:
    print("you are not eligible for the discount SORRY!")