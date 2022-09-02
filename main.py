#1#The following list is of 10 students ages
ages=[19,22,19,24,20,25,26,24,25,24]

#sorting by using sort method
ages.sort()
print("The Sorted List of ages")
print(ages)

#finding the min age and max age values
print("The Min age value is : ")
print(min(ages))
print("The Max age value is : ")
print(max(ages))

#adding min and max values to list
ages.append(min(ages))
ages.append(max(ages))
print("The Modified list of ages: ")
print(ages)

#finding the median age
import statistics
print(statistics.median(ages))

#finding the average of ages
Average=statistics.mean(ages)
print("The Average age: ")
print(Average)

#finding the range of ages
range_of_ages=max(ages)-min(ages)
print("Range of ages is : ")
print(range_of_ages)

#2.#creating dog dictionary & Adding keys & values to the empty dog dictionary
dog=dict()
dog["Name"]="puppy"
dog["Color"]="brown"
dog["Breed"]="husky"
dog["legs"]=4
dog["Age"]=8
print(" Dog dictionary is : ",dog)
print()

#creating student dictionary
student=dict()
student["first_name"]="Ravali"
student["last_name"]="Bhoothpuram"
student["Gender"]="Female"
student["Age"]=22
student["Martial status"]="single"
student["Skills"]=["python","Java"]
student["Country"]="US"
student["City"]="NC"
student["Address"]="street no 136"
print("Student dictionary is : ",student)
print()

#The length of student dictionary
print("length of student dictionary is : ",str(len(student)));

#The value of student skills and data type
print("student skills are : ",end='')
print(student["Skills"])
print("type of student skills is : ",type(student["Skills"]))

#modifying student skills
student["Skills"].append("sailpoint")
student["Skills"].append("cybersecurity")
print("modified student skills : ",student["Skills"])

#getting dictionary keys as list
dog_keys=list(dog.keys())
print("dog dictionary keys : ",dog_keys)
dog_values=list(dog.values())
print("dog dictionary values : ",dog_values)
student_keys=list(student.keys())
print("student dictionary keys : ",student_keys)
student_values=list(student.values())
print("student dictionary values : ",student_values)

#3.#creating tuples for my brothers and sisters
sisters=("Manju","Padma")
brothers=("Dilip","Praveen","Raj")
print("My brothers are : ",brothers)
print("My sisters are : ",sisters)

#joining my brothers and sisters tuples to siblings
siblings=brothers+sisters
print("My siblings are : ",siblings)
print("The no. of siblings are : ",len(siblings))

#modifying siblings tuple by adding my father's name and mother's name
family_members=("father","mother")+siblings
print("My family members are : ",family_members)

#4.#The given it_companies are as shown below
it_companies = {"Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
print("length of it_companies are : ", len(it_companies))

# adding twitter to it_companies
it_companies.add("Twitter")
print("it_companies after adding twitter :", it_companies)

# inserting multiple it_companies
companies = ["Cotelligent", "comcast", "apple"]
it_companies.update(companies)
print("it_companies after adding multiple companies :", it_companies)

# removing one company
it_companies.remove("Twitter")
print("it_companies after removing one company : ", it_companies)

# Difference between remove and discard method
# The remove() method will raise an error if the specified item does not exist, and the discard() method will not raise error.

# joining A and B
C = A.union(B)
print("joining A and B is :", C)

# finding A intersection B
I = A.intersection(B)
print("Intersection of A and B is:", I)

# checking is A subset of B
check = A.issubset(B)
if check:
    print("A is subset of B")
else:
    print("A is not a subset of B")

# checking are A and B are disjoint sets
check1 = A.isdisjoint(B)
if check1:
    print("A and B are disjoint sets")
else:
    print("A and B are not disjoint sets")

# joining A with B and B with A
A_join_B = A.union(B)
B_join_A = B.union(A)
print("A join B is :", A_join_B)
print("B join A is :", B_join_A)

# symmetric difference between A and B
D = A.symmetric_difference(B)
print("symmetric difference between A and B is :", D)

# deleting all the sets
it_companies.clear()
A.clear()
B.clear()

# converting ages list to set
age_set = set(age)
print("length of ages list is : ", len(age))
print("length of ages set is :", len(age_set))
print("length of ages list is greater than the ages set")

#5.#area of circle
#Given radius of circle 30 meters
r=30
#assigned variable name "_area_of_circle"
_area_of_circle=3.14*(r**2)
 #printing the stored value in variabale
print("area of circle :",_area_of_circle)

#circumference of circle
#assigned variable name "_circum_of_circle"
_circum_of_circle=2*3.14*r
#printing the value
print("circumference of circle :",_circum_of_circle)

#area of circle for user input
#taking the user input
n=int(input())
#assigned variable name "area"
area=3.14*(n**2)
#printing the value
print("Area of circle with user input :",area)

#6.# given string to the variable a
x="I am a teacher and I love to inspire and teach people"
# split the given string
y=x.split()
# using set to remove duplicates
set1=set(y)
# using len to count number of words
count=len(set1)
# printing the value
print(count)

#7.#tab escape
# declaring a string to the text variable
text = "Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki"
#print the requried output
print(text)

#8.#assigned variable radius
radius=10
#assigned area of circle formula
area=3.14 * radius ** 2
#print the output using string format
print("The area of circle with radius {} is {} meters square".format(radius,area))

#9.#
n=int(input("Enter number of student's weight to be calculated"))
weights_in_lbs=[]
weights_in_kg=[]
#appending the elements into the list
for i in range(n):
    weights_in_lbs.append(int(input("weight {} \n".format(i+1))))
print(weights_in_lbs)
#converting lbs to kilogram with exactly 2 decimal places
for i in range(len(weights_in_lbs)):
    lbs=0.45359237 #1lbs= 0.45359237kg
    temp=round(weights_in_lbs[i]*lbs,2)
    weights_in_kg.append(temp)
    temp=0
print(weights_in_kg)








