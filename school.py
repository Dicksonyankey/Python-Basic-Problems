def school():
    name = 'John'
    print (f"His name in school {name}")
    
def college():
    name = 'Max'
    print (f"His name in college {name}")
    school()
    
def work():
    name = 'Peter'
    print(f"His name in work location {name}")
    college()

work()