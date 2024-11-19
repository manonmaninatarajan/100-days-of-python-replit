# Affirmation Generator
name = input("What is your name? ").strip().capitalize()
print(f"Hello, {name}! 😊")

age = input("How old are you? ").strip()
mood = input("What is your mood today (e.g., good, bad, excited)? ").strip().lower()
curr_day = input("What day is it today? ").strip().capitalize()

# Affirmations for each day
if curr_day == "Monday":
    print(
        f"Today is {curr_day}, {name}. You are off to a fresh start! No matter how {mood} you feel, you have the power to conquer anything. 🌟"
    )
elif curr_day == "Tuesday":
    print(
        f"Happy {curr_day}, {name}! Remember, progress is progress, no matter how small. Stay {mood} and keep moving forward. 🚀"
    )
elif curr_day == "Wednesday":
    print(
        f"It's {curr_day}, {name}! Halfway through the week. Whether you're feeling {mood} or not, you're closer to your goals than you think. 💪"
    )
elif curr_day == "Thursday":
    print(
        f"Hello, {name}. It's {curr_day}! Keep going—you've come so far. Even if you're feeling {mood}, take one step at a time. You're doing great! 🌈"
    )
elif curr_day == "Friday":
    print(
        f"Yay, {name}! It's {curr_day}! Time to celebrate your hard work. No matter how {mood} you feel, take a moment to appreciate yourself. 🎉"
    )
elif curr_day == "Saturday":
    print(
        f"Happy {curr_day}, {name}! Take some time to relax and recharge. Even if you're {mood}, today is for you. 🌼"
    )
elif curr_day == "Sunday":
    print(
        f"Ah, {curr_day}, {name}. A perfect day to reflect and prepare for the week ahead. Stay {mood} and focus on self-care. 🌸"
    )
else:
    print(
        f"Hmm, {curr_day} doesn't seem like a valid day, {name}. Are you feeling {mood}? Double-check the spelling!"
    )
