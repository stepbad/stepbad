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

# Add in CLAIM section

# Enter claim section.


  # Set up Counter and Accumulator
  Claim_Amt_Acc = 0.0
  Claim_Num_Ctr = 0

  while True:
    Continue = input("Do you want to enter client's claim information? (Y / N): ").upper()
    print()

    if Continue != "Y" and Continue != "N":
        print("   Data Entry Error - prompt to continue must be a Y or an N.")
    
    elif Continue == "Y":
      print("Client's Information Entry System")
      print()
      Claim_Num_Ctr += 1

    # Open the Claim.dat file in append mode. Write the client's information and the claims to the file.
      h = open("Claim.dat", "a")
      
      Claim_Date = input("Enter the claim date (YYYY,MM,DD): ")
      print()

      Claim_Amt = input("Enter the claim amount: ")

        
      # I am creating a complex claim number containing relative information.

      Year_Sec, Mon_Sec, Day_Sec = Claim_Date.strip().split(",")

      Claim_Num = f"{Year_Sec}{Mon_Sec}{Day_Sec}-{random.randint(1000, 9999)}-{NEXT_POLICY_NUM}{First_Name[0]}{Last_Name[0]}0{Claim_Num_Ctr}"

      h.write(f"{Claim_Num}, ")
      h.write(f"{Claim_Date}, ")

      # Update Counter and Accumulator
      Claim_Amt = float(Claim_Amt)
      Claim_Amt_Acc += Claim_Amt
      h.write(f"{Claim_Amt}\n")
      h.close()

      print()
  
    else:
      Claim_Num = "00000000-0000-0000aa00"
      Claim_Date = "0000,00,00"
      Claim_Amt = 0
      break     
  
  print("Exiting Claim Information Entry System.") 
  print()

  # Close the files and add blinking message
  g.close()
  
  # 1. Blinking message for the user. Directly from class.
  # Simple progress bar - just a blinking message.
  # Need to import sys and time.

  print()

  Message = "Saving Client Information  ..."
  for _ in range(5):  # Change to control no. of 'blinks'
      print(Message, end='\r')
      time.sleep(.3)  # To create the blinking effect
      sys.stdout.write('\033[2K\r')  # Clears the entire line and carriage returns
      time.sleep(.3)

  print()
  print()
  print("Client information has been successfully saved to ClientInfo.dat & Claim.dat ...")
  print()
  print()

  # added OUTPUT section

# Display results

  print()
  print(f"One Stop Insurance Company     Phone: 1-800-123-4567     Email: customerassistant@onestop.com      Date: {CURRENT_DATE}")
  print(f"=======================================================================================================================")
  print()
  print(f"Client Information")
  print(f"-----------------------------------------------------------------------------------------------------------------------")
  print(f"Policy Number:      Name                             Address:                                        Phone:")
  print(f"{NEXT_POLICY_NUM:>4d}             {First_Name:>12s}  {Last_Name:<20s} {St_Address:>14s} , {City:<14s} {Prov:>2s} {Postal_Code}       {Phone_Number:14s}")
  print()
  print(f"Payment Information")
  print(f"-----------------------------------------------------------------------------------------------------------------------")

  print(f"Payment Method:        Total Premium:    HST:        Total Cost:    Processing Fee:       Payment Amount:  ")
  print(f"{Payment_Method:<20s}   {(FV.FDollar2(Total_Premium)):<10s}        {(FV.FDollar2(Hst)):<8s}    {(FV.FDollar2(Total_Cost)):<10s}     {(FV.FDollar2(Proc_Fee)):<7s}               {(FV.FDollar2(Pay_Amount)):<11s}")
  print(f"-----------------------------------------------------------------------------------------------------------------------")

  print()
  print(f"Claims:")
  print(f"Claim Number:                      Date:              Amount:  ")
  print(f"-----------------------------------------------------------------------------------------------------------------------")


# Call Function to Open Claims.dat to print claims data
  claims = OpenReadClaimFile("Claim.dat")

  for claim in claims:
    Claim_Num, Claim_Amt, Claim_Date = claim
    Date_Sec, Tot_Sec, Pol_Sec = Claim_Num.strip().split("-")
    if str(NEXT_POLICY_NUM) in str(Pol_Sec):
        print(f"{Claim_Num:<10s}             {Claim_Date:<10s}        {FV.FDollar2(float(Claim_Amt))}")
  print(f"-----------------------------------------------------------------------------------------------------------------------")
  print()
  print(f"Total Number of Claims : {Claim_Num_Ctr}")
  print(f"Total Claimed Amount: {FV.FDollar2(Claim_Amt_Acc)}")
  print()

