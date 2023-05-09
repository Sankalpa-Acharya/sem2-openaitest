


subject1=int(input("enter marks of subject1"))
subject2=int(input("enter marks of subject2"))
subject3=int(input("enter marks of subject3"))
total=subject1+subject2+subject3
avg=(total/3)
if avg<39 or subject1<39 or subject2<39 or subject3<39:
	print("Fail")
else:
	print("Pass")
if avg>=80 and avg<=100:
	print("Grade: O")
elif avg>=70 and avg<80:
	print("Grade: A+")
elif avg>=60 and avg<70:
	print("Grade: A")
elif avg>=55 and avg<60:
	print("Grade: B+")
elif avg>=50 and avg<55:
	print("Grade: B")
elif avg>=45 and avg<50:
	print("Grade: C")
elif avg>=40 and avg<45:
	print("Grade: P")