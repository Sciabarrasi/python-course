#logic operators
#and
#example:
age = 20
have_experience = True

if age > 18 and have_experience:
    print("You can apply for the job")
else:
    print("You cannot apply for the job")

#or
#example:
is_student = True
is_employed = False

if is_student or is_employed:
    print("The person is either a student or employed")
else:
    print("The person is not a student and not employed")

#if not
raining = False

if not raining:
    print("You can go for a walk")
else:
    print("Better stay inside")