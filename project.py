Days = [ "Wednesday","Monday","Tuesday","Thursday","Friday"]

Message_list = [
    "Successful",
    "Unsuccessful",
    "Not Successful"
]

mid_day = ["Yes","No"]

def message_from_employee(day,message):
    if (Days_input == Days[0]) and (Message_list[0] in message_to_Professor  ) and noon_validay == mid_day[0]:
        return ("Thank you for offering me this opportunity!!")

    if (Days_input in  Days[1:]) and (Message_list[1] in message_to_Professor) and noon_validay == mid_day[1]:
        return ("wo ni twaaasede! Aboatoriwa")
    
    return ("Sorry to disappoint you i don't have the email yet")


Days_input = input("What day is it ? : ")

message_to_Professor = input("Type the message to be sent to Profess? :")

noon_validay = input("Yes or No :")




final_message = message_from_employee(Days_input,message_to_Professor)
print(final_message)




