# starting with inputs and what i need for main program

while True:
  print()
  print("Welcome to the One Stop Insurance Company's New Policy Entry System")
  print()

  # Get customer's personal information.
  print(f"The new policy number is {str(NEXT_POLICY_NUM)}")

  print()
   
  # Gather user inputs. Write processed data to a file for future use.
  g = open("ClientInfo.dat", "a")

  while True:

    First_Name = input("Enter customer's first name: ").strip().title()
    
    if  First_Name == "":
      print("   Data Entry Error - Customer name cannot be blank.")

    elif First_Name.isalpha() == False: 
      print("   Data Entry Error - Customer first name must be letters")
    
    else:
      g.write(f"{NEXT_POLICY_NUM}, ")
      g.write(f"{First_Name}, ")

      break
  
  print()
  while True: 
    Last_Name = input("Enter customer's last name: ").strip().title()
    
    if  Last_Name == "":
      print("   Data Entry Error - Customer last name cannot be blank.")

    elif Last_Name.isalpha() == False :
      print("   Data Entry Error - Customer last name must be letters")
   
    else:
      g.write(f"{Last_Name}, ")
      break    
  
  print()

  St_Address = input("Enter the street address of the customer: ").title()
  g.write(f"{str(St_Address)}, ")

  print()

  City = input("Enter the city of the customer: ").strip().title()
  g.write(f"{City}, ")

  print()

  # Validate user input using a list of values.
  
  Prov_Lst = ["AB", "BC", "MB", "NB", "NL", "NS", "NT", "NU", "ON", "PE", "QC", "SK", "YT"]

  while True:

    Prov = input("Enter the province (XX): ").upper()

    if Prov == "":
      print("Error - Province cannot be blank - Please re-enter.")

    elif len(Prov) != 2:
      print("Error - Province is a 2 digit code - please re-enter.")

    elif Prov not in Prov_Lst:
      print("Error - Not a valid province - please re-enter.")

    else:
      g.write(f"{Prov}, ")
      break
  
  print("Province has been successfully entered.") 
  
  print()

  Postal_Code = input("Enter the postal code of the customer: ").upper()
  g.write(f"{Postal_Code}, ")
  print()

  while True: 

    Phone_Number = input("Enter the phone number (9999999999): ")

    if Phone_Number == "":
      print("   Data Entry Error - Phone Number cannot be blank.")
  
    elif len(Phone_Number) != int(MAX_PHONE_LENGTH):
      print("   Data Entry Error - Phone Number must be 10 digits.")
  
    elif Phone_Number.isdigit() == False:
      print("   Data Entry Error - Phone Number contains invalid characters.")
  
    else: 
      g.write(f"{str(Phone_Number)}, ")
      Phone_Number = "(" + Phone_Number[0:3] + ") " + Phone_Number[3:6] + "-" + Phone_Number[6:]
      break

  print()

  Num_Cars = input("Enter the number of cars covered in the policy: ")
  g.write(f"{str(Num_Cars)}, ")
  print()

  Ext_Liab = input("Does client have extra liability? (Y or N): ").upper()
  g.write(f"{str(Ext_Liab)}, ")
  
  
  print()

  Glass_Cov = input("Does client require glass coverage? (Y or N): ").upper()
  g.write(f"{str(Glass_Cov)}, ")
  
  print()

  Loan_Car = input("Does client require optional loaner car? (Y or N): ").upper()
  g.write(f"{str(Loan_Car)}, ")
  
  print()

  Pay_Method = input("Enter client payment method.  Type 1 for Pay in Full.  Type 2 for Monthly Payments.  Type 3 for Down Payment Option. : ")

  if Pay_Method == "3":
    Down_Pay_Amt = input("How much does the client wish to down pay: ")

  else:
    Down_Pay_Amt = 0
    print()

  
  g.write(f"{Pay_Method}, ")
  g.write(f"{Down_Pay_Amt}\n")

  print()
