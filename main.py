import pywhatkit as kit

# Define the phone number and message
phone_number = "+123456789"  # Replace with the recipient's phone number
message = "Hii"  # The message you want to send
hour = 23  # The hour you want to send the message (24-hour format)
minute = 19  # The minute you want to send the message

# Send the message
kit.sendwhatmsg(phone_number, message, hour, minute)