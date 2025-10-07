import streamlit as st
import pandas as pd # Used for better display of contacts

# -------------------------------
# 1. DATA PERSISTENCE SETUP
# -------------------------------
# The contacts dictionary must be stored in Streamlit's Session State
# so it doesn't get erased every time the script reruns.
if 'contacts' not in st.session_state:
    st.session_state['contacts'] = {}

# Use a reference to simplify the function code below
contacts = st.session_state['contacts']

# -------------------------------
# Function: Add Contact (Refactored for Streamlit)
# -------------------------------
def add_contact_logic(name, phones_input, emails_input, whatsapp, linkedin, facebook, instagram):
    # Ensure inputs are not empty and names are stripped
    if not name:
        st.error("Name cannot be empty.")
        return

    name = name.strip()
    if name in contacts:
        st.warning(f"Contact '{name}' already exists.")
        return

    # Process and limit phones
    phones = [p.strip() for p in phones_input.split(",") if p.strip()][:3]

    # Process emails
    emails = [e.strip() for e in emails_input.split(",") if e.strip()]

    # Add contact to the session state dictionary
    contacts[name] = {
        "phone": phones,
        "email": emails,
        "whatsapp": whatsapp.strip(),
        "linkedin": linkedin.strip(),
        "facebook": facebook.strip(),
        "instagram": instagram.strip()
    }
    st.session_state['last_action_status'] = f"✅ Contact '{name}' added successfully!"

# -------------------------------
# Function: Delete Contact (Refactored for Streamlit)
# -------------------------------
def delete_contact_logic(name):
    if name in contacts:
        del contacts[name]
        st.session_state['last_action_status'] = f"✅ Contact '{name}' deleted successfully!"
    else:
        st.session_state['last_action_status'] = "❌ Contact not found."

# -------------------------------
# Function: Edit Contact (Refactored for Streamlit)
# -------------------------------
def edit_contact_logic(name, new_phones_input, new_emails_input, new_whatsapp, new_linkedin, new_facebook, new_instagram):
    if name not in contacts:
        st.session_state['last_action_status'] = "❌ Contact not found."
        return

    # Update phones if new input is provided
    if new_phones_input:
        contacts[name]["phone"] = [p.strip() for p in new_phones_input.split(",") if p.strip()][:3]

    # Update emails if new input is provided
    if new_emails_input:
        contacts[name]["email"] = [e.strip() for e in new_emails_input.split(",") if e.strip()]

    # Update single fields only if new input is provided
    if new_whatsapp:
        contacts[name]["whatsapp"] = new_whatsapp.strip()
    if new_linkedin:
        contacts[name]["linkedin"] = new_linkedin.strip()
    if new_facebook:
        contacts[name]["facebook"] = new_facebook.strip()
    if new_instagram:
        contacts[name]["instagram"] = new_instagram.strip()

    st.session_state['last_action_status'] = f"✅ Contact '{name}' updated successfully!"

# -------------------------------
# Main Streamlit App Layout
# -------------------------------
st.title("📞 Coordinate Consolidator")

# Display status of the last action (Add, Edit, Delete)
if 'last_action_status' in st.session_state:
    st.success(st.session_state['last_action_status'])
    # Clear the status after displaying
    del st.session_state['last_action_status']


# --- Menu Selection ---
menu_options = [
    "Add Contact", 
    "View All Contacts", 
    "Edit Contact", 
    "Delete Contact", 
    "Search by Name", 
    "Search by Keyword"
]
choice = st.sidebar.selectbox("Select Operation", menu_options)

# -----------------------------------
# 1. ADD CONTACT INTERFACE
# -----------------------------------
if choice == "Add Contact":
    st.header("➕ Add New Contact")
    with st.form("add_contact_form", clear_on_submit=True):
        name = st.text_input("Name:", key='add_name')
        phones_input = st.text_input("Phone Numbers (comma-separated, max 3):", key='add_phones')
        emails_input = st.text_input("Emails (comma-separated):", key='add_emails')
        whatsapp = st.text_input("WhatsApp Number:", key='add_whatsapp')
        linkedin = st.text_input("LinkedIn Profile Link:", key='add_linkedin')
        facebook = st.text_input("Facebook Profile Link:", key='add_facebook')
        instagram = st.text_input("Instagram Profile Link:", key='add_instagram')
        
        submitted = st.form_submit_button("Add Contact")
        if submitted:
            # Call the core logic function
            add_contact_logic(name, phones_input, emails_input, whatsapp, linkedin, facebook, instagram)
            st.rerun()

# -----------------------------------
# 2. VIEW ALL CONTACTS INTERFACE
# -----------------------------------
elif choice == "View All Contacts":
    st.header("👀 Contact List")
    if not contacts:
        st.info("No contacts available.")
    else:
        # Transform the dictionary into a Pandas DataFrame for a clean, table-like display
        df = pd.DataFrame.from_dict(contacts, orient='index')
        # Format the list columns to be displayed as comma-separated strings
        df['phone'] = df['phone'].apply(lambda x: ', '.join(x))
        df['email'] = df['email'].apply(lambda x: ', '.join(x))
        df.index.name = "Name"
        st.dataframe(df, use_container_width=True)

# -----------------------------------
# 3. EDIT CONTACT INTERFACE
# -----------------------------------
elif choice == "Edit Contact":
    st.header("✍️ Edit Existing Contact")
    edit_name = st.selectbox("Select Contact to Edit:", options=[""] + list(contacts.keys()))

    if edit_name:
        info = contacts[edit_name]
        st.markdown(f"**Editing: {edit_name}**")
        st.caption("Leave fields blank to keep current value.")

        with st.form("edit_contact_form"):
            # Provide current values as defaults for convenience
            new_phones = st.text_input("New Phones:", value=", ".join(info['phone']), key='edit_phones')
            new_emails = st.text_input("New Emails:", value=", ".join(info['email']), key='edit_emails')
            new_whatsapp = st.text_input("New WhatsApp:", value=info['whatsapp'], key='edit_whatsapp')
            new_linkedin = st.text_input("New LinkedIn:", value=info['linkedin'], key='edit_linkedin')
            new_facebook = st.text_input("New Facebook:", value=info['facebook'], key='edit_facebook')
            new_instagram = st.text_input("New Instagram:", value=info['instagram'], key='edit_instagram')

            edited = st.form_submit_button("Update Contact")
            if edited:
                # Call the core logic function
                edit_contact_logic(edit_name, new_phones, new_emails, new_whatsapp, new_linkedin, new_facebook, new_instagram)
                st.rerun()

# -----------------------------------
# 4. DELETE CONTACT INTERFACE
# -----------------------------------
elif choice == "Delete Contact":
    st.header("🗑️ Delete Contact")
    delete_name = st.selectbox("Select Contact to Delete:", options=[""] + list(contacts.keys()), key='delete_name_select')
    
    if delete_name and st.button(f"Confirm Delete '{delete_name}'", type="primary"):
        delete_contact_logic(delete_name)
        st.rerun()

# -----------------------------------
# 5. SEARCH BY NAME INTERFACE
# -----------------------------------
elif choice == "Search by Name":
    st.header("🔍 Search by Full Name")
    search_name = st.text_input("Enter exact name to search:")

    if search_name and search_name.strip() in contacts:
        info = contacts[search_name.strip()]
        st.subheader(search_name.strip())
        st.markdown(f"**Phone:** {', '.join(info['phone'])}")
        st.markdown(f"**Email:** {', '.join(info['email'])}")
        st.markdown(f"**WhatsApp:** {info['whatsapp']}")
        st.markdown(f"**LinkedIn:** {info['linkedin']}")
        st.markdown(f"**Facebook:** {info['facebook']}")
        st.markdown(f"**Instagram:** {info['instagram']}")
    elif search_name:
        st.error("❌ Contact not found.")

# -----------------------------------
# 6. SEARCH BY KEYWORD INTERFACE
# -----------------------------------
elif choice == "Search by Keyword":
    st.header("🔎 Search by Keyword")
    keyword = st.text_input("Enter keyword to search:").lower().strip()
    
    if keyword:
        found_matches = []
        for name, info in contacts.items():
            # Check name first
            if keyword in name.lower():
                found_matches.append(name)
                continue
                
            # Check contact details
            for value in info.values():
                # Handle list values (phone, email)
                if isinstance(value, list):
                    if any(keyword in str(v).lower() for v in value):
                        found_matches.append(name)
                        break  # Stop checking details for this contact
                
                # Handle single string values
                elif keyword in str(value).lower():
                    found_matches.append(name)
                    break # Stop checking details for this contact

        if found_matches:
            st.subheader(f"Contacts matching '{keyword}':")
            # Display unique names found (though logic above should prevent duplicates)
            st.success(", ".join(sorted(set(found_matches))))
        else:
            st.info("No matches found.")