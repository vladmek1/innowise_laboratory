# PART 1: Profile Function
def generate_profile(age: int) -> str:
    if 0 <= age <= 12:
        return "Child"
    elif 13 <= age <= 19:
        return "Teenager"
    elif age >= 20:
        return "Adult"

#PART 2: User Input
CURRENT_YEAR = 2025

user_name = input("Enter your full name: ")
birth_year_str = input("Enter your birth year: ")
birth_year = int(birth_year_str)
current_age = CURRENT_YEAR - birth_year
hobbies = []

while True:
    hobby = input("Enter a favorite hobby or type 'stop' to finish: ")
    if hobby.lower().strip() == "stop":
        break
    hobbies.append(hobby)
#PART 3: Profile Processing
life_stage = generate_profile(current_age)
user_profile = {
    'name': user_name,
    'age': current_age,
    'life_stage': life_stage,
    'hobbies': hobbies
}
#PART 4: Output Display
print("-" * 15, end="")
print(f"""
Profile Summary:
Name: {user_profile['name']}
Age: {user_profile['age']}
Life Stage: {user_profile['life_stage']}""")

if len(user_profile['hobbies']) == 0:
    print("You didn't mention any hobbies.")
else:
    print(f"Favorite Hobbies ({len(user_profile['hobbies'])}):")
    for hobby in user_profile['hobbies']:
        print(f"- {hobby}")

print("-" * 15)
