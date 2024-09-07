import time

def greet():
    current_hour = time.localtime().tm_hour

    if 5 <= current_hour < 12:
        print("Good Morning")
    elif 12 <= current_hour < 18:
        print("Good Afternoon")
    else:
        print("Good Evening")
    
print(greet())