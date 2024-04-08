print("Welcome to my German quiz!")

playing = input("Do you want to play? ")

if playing.strip().lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

questions = [
    ("Tee, bitte", "Tea, please"),
    ("Brot", "Bread"),
    ("Wasser", "Water")
]

for question, answer in questions:
    user_answer = input(f"What does \"{question}\" stand for? ")
    if user_answer.strip().lower() == answer.lower():
        print('Correct!')
        score += 1
    else:
        print(f"Incorrect! The correct answer is \"{answer}\".")

total_questions = len(questions)
print(f"You got {score} out of {total_questions} questions correct!")
percentage = (score / total_questions) * 100
print(f"You got {percentage:.2f}%.")
