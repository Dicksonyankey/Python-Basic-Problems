pres_medication = ["Paracetamol","Joy Ointment","Pandol"]
# List of Disease
sub_disease = ["Headache","Malaria","Cough"]
# Taking patient Disease
pat_disease = input("Please tell me your Disease: ")
# Taking patient Age
pat_age = int(input("Please Enter your Age: "))

def my_prescription(pat_age):
    # Loopig through the list of sub_disease
    for disease in sub_disease:
        # cheaking my logical statement and validating patient inputs
        if (pat_disease == sub_disease[0]) and (pat_age <= 18):
            return (f"Beacause you have {pat_disease} and under age, take 600mg of {pres_medication[0]}")
        # checking patient type of disease and age if they are above 18 but less than 40
        if  (pat_disease == sub_disease[2]) and (18 < pat_age <= 40):
            return (f"Because you have {pat_disease} and you are above 18, take 1000mg of {pres_medication[2]}")
        # checking if they are above 50....
        return (f"Go for a LAB Test and apply {pres_medication[1]} for the mean time till we get your LAB result")

# Calling the function with the needed parameter   
result = my_prescription(pat_age)

print(result)