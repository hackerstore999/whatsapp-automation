import pywhatkit as kit
import time

# Define the phone number and messages
phone_number = "+123456789"  # Replace with the recipient's phone number
messages = ["Hii", "How are you?", "This is a test message.", "Goodbye!"]  # List of messages to send
hour = 23  # The hour you want to start sending messages (24-hour format)
minute = 35  # The minute you want to start sending messages

# Loop through the messages and send each one
for i, message in enumerate(messages):
    # Send the message
    kit.sendwhatmsg(phone_number, message, hour, minute + i)  # Increment minute for each message
    time.sleep(10)  # Wait for 10 seconds before sending the next message