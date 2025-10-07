# -------------------------------
# Project: Coordinate Consolidator
# -------------------------------

# Data structure: Hash Table (Dictionary)
contacts = {}

# -------------------------------
# Function: Add Contact
# -------------------------------
def add_contact():
    name = input("Enter Name: ").strip()
    if name in contacts:
        print("Contact already exists.")
        return

    phones = input("Enter phone numbers (comma-separated, max 3): ").split(",")
    phones = [p.strip() for p in phones[:3]]  # limit to 3 numbers

    emails = input("Enter emails (comma-separated): ").split(",")
    emails = [e.strip() for e in emails]

    whatsapp = input("Enter WhatsApp number: ").strip()
    linkedin = input("Enter LinkedIn profile link: ").strip()
    facebook = input("Enter Facebook profile link: ").strip()
    instagram = input("Enter Instagram profile link: ").strip()

    contacts[name] = {
        "phone": phones,
        "email": emails,
        "whatsapp": whatsapp,
        "linkedin": linkedin,
        "facebook": facebook,
        "instagram": instagram
    }
    print(f"\n✅ Contact '{name}' added successfully!\n")

# -------------------------------
# Function: View All Contacts
# -------------------------------
def view_contacts():
    if not contacts:
        print("\nNo contacts available.\n")
        return

    print("\n------ Contact List ------")
    for name, info in contacts.items():
        print(f"\nName: {name}")
        print(f"Phone: {', '.join(info['phone'])}")
        print(f"Email: {', '.join(info['email'])}")
        print(f"WhatsApp: {info['whatsapp']}")
        print(f"LinkedIn: {info['linkedin']}")
        print(f"Facebook: {info['facebook']}")
        print(f"Instagram: {info['instagram']}")
    print("--------------------------\n")

# -------------------------------
# Function: Edit Contact
# -------------------------------
def edit_contact():
    name = input("Enter the name of the contact to edit: ").strip()
    if name not in contacts:
        print("❌ Contact not found.")
        return

    print("Leave blank to keep old value.")

    phones = input("Enter new phone numbers (comma-separated, max 3): ")
    if phones:
        contacts[name]["phone"] = [p.strip() for p in phones.split(",")[:3]]

    emails = input("Enter new emails (comma-separated): ")
    if emails:
        contacts[name]["email"] = [e.strip() for e in emails.split(",")]

    whatsapp = input("Enter new WhatsApp number: ").strip()
    if whatsapp:
        contacts[name]["whatsapp"] = whatsapp

    linkedin = input("Enter new LinkedIn link: ").strip()
    if linkedin:
        contacts[name]["linkedin"] = linkedin

    facebook = input("Enter new Facebook link: ").strip()
    if facebook:
        contacts[name]["facebook"] = facebook

    instagram = input("Enter new Instagram link: ").strip()
    if instagram:
        contacts[name]["instagram"] = instagram

    print(f"\n✅ Contact '{name}' updated successfully!\n")

# -------------------------------
# Function: Delete Contact
# -------------------------------
def delete_contact():
    name = input("Enter the name of the contact to delete: ").strip()
    if name in contacts:
        del contacts[name]
        print(f"\n✅ Contact '{name}' deleted successfully!\n")
    else:
        print("❌ Contact not found.")

# -------------------------------
# Function: Search by Name
# -------------------------------
def search_contact():
    name = input("Enter name to search: ").strip()
    if name in contacts:
        info = contacts[name]
        print(f"\nName: {name}")
        print(f"Phone: {', '.join(info['phone'])}")
        print(f"Email: {', '.join(info['email'])}")
        print(f"WhatsApp: {info['whatsapp']}")
        print(f"LinkedIn: {info['linkedin']}")
        print(f"Facebook: {info['facebook']}")
        print(f"Instagram: {info['instagram']}\n")
    else:
        print("❌ Contact not found.")

# -------------------------------
# Function: Keyword Search
# -------------------------------
def keyword_search():
    keyword = input("Enter keyword to search: ").lower()
    found = False

    print(f"\n🔍 Contacts matching '{keyword}':")
    for name, info in contacts.items():
        for value in info.values():
            if isinstance(value, list):
                for v in value:
                    if keyword in v.lower():
                        print(f"- {name}")
                        found = True
                        break
            elif keyword in str(value).lower():
                print(f"- {name}")
                found = True
                break

    if not found:
        print("No matches found.\n")
    print()

# -------------------------------
# Main Menu
# -------------------------------
def main():
    while True:
        print("\n===== Coordinate Consolidator =====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Search by Name")
        print("6. Search by Keyword")
        print("7. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            edit_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            search_contact()
        elif choice == "6":
            keyword_search()
        elif choice == "7":
            print("Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid choice, please try again.")

# Run the program
if __name__ == "__main__":
    main()
