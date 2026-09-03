leads = [] 

def add_lead():
    name = input("Name: ")
    email = input("Email: ")
    company = input("Company: ")
    phone = input("Phone: ")
    budget = input("Budget: ")
    status = input("Status: ")

    new_lead = {
        "id": len(leads) + 847292,
        "name": name,
        "status": status,
        "email": email,
        "company": company,
        "phone": phone,
        "budget": budget
    }

    leads.append(new_lead)

    print("Lead added successfully!")
    print(new_lead)

def show_leads():
    print("\n= ALL LEADS =")

    for lead in leads:
        print("---")
        print("ID:", lead["id"])
        print("Name:", lead["name"])
        print("Status:", lead["status"])
        print("Email:", lead["email"])
        print("Company:", lead["company"])
        print("Phone:", lead["phone"])
        print("Budget:", lead["budget"], "PKR")

add_lead()
show_leads()