import pyautogui
import time

predefined_messages = [
    "Hello, how are you?",
    "I'll be right there.",
    "Can you please send me the file?",
    "Thank you!",
]

print("Choose a message to type:")
for i, msg in enumerate(predefined_messages):
    print(f"{i + 1}. {msg}")

print(f"{len(predefined_messages) + 1}. Type a custom message")

choice = 0
while True:
    try:
        choice_input = input(f"Enter your choice (1-{len(predefined_messages) + 1}): ")
        choice = int(choice_input)
        if 1 <= choice <= len(predefined_messages) + 1:
            break
        else:
            print("Invalid choice. Please enter a number from the list.")
    except ValueError:
        print("Invalid input. Please enter a number.")

if choice <= len(predefined_messages):
    message_to_type = predefined_messages[choice - 1]
else:
    message_to_type = input("Enter the custom message you want to type automatically: ")

delay_seconds = 5

print(f"You have {delay_seconds} seconds to switch to the window where you want the message to be typed.")
time.sleep(delay_seconds)

# Type the message
# Add an interval (in seconds) between each key press.
# For example, 0.1 seconds for a slightly slower typing speed.
pyautogui.typewrite(message_to_type, interval=0.1)

print("Message typed!")