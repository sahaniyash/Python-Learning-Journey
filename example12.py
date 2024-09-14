num = int(input("Enter Units: ")) 

if num<=100 and num >=100:
    print("no charge")

#elif num>=100 :
    #print(f"Total bill amount is Rs{num*5}")

else: #num>=200 :
    print(f"Total bill amount is Rs{num*10}")