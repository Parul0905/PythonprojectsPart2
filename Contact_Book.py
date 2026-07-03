import csv
import os

FILENAME='contacts.csv'

if not os.path.exists(FILENAME):
    with open(FILENAME, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Phone', 'Email'])
def add_contact():
    name=input('Name: ').strip()
    phone=input('Phone: ').strip()
    email=input('Email: ').strip()

    with open(FILENAME,'r',encoding='utf-8') as f:
        reader=csv.DictReader(f)
        for row in reader:
            if row['Name'].lower()==name.lower():
                print('Contact name already exists')
                return
    with open(FILENAME,'a',encoding='utf-8') as f:
        writer=csv.writer(f)
        writer.writerow([name,phone,email])
        print('Contact Added ✅')
    
def view_contact():
        with open(FILENAME,'r',encoding='utf-8') as f:
            reader=csv.reader(f)
            rows=list(reader)

            if len(rows)<1:
                print('No contacts found')
                return
            print('\n Your Contacts:\n')
            
            for row in rows[1:]:
                print(f'{row}')
            print()
def search_contact():
        term =input("Enter the name to search ").strip().lower()
        found=False

        with open(FILENAME,'r',encoding='utf-8') as f:
            reader=csv.DictReader(f)
            for row in reader:
                if term in row['Name'].lower():
                    print(f'{row["Name"]} |{row["Phone"]}')
                    found=True

        if not found:
            print('No matching contact found')

def delete_contact():
    cut = input("Enter the name to delete: ").strip().lower()

    remaining = []
    found = False

    # Read all contacts
    with open(FILENAME, 'r', encoding='utf-8', newline='') as f:
        reader = csv.DictReader(f)

        for row in reader:
            if row['Name'].lower() == cut:
                found = True
            else:
                remaining.append(row)

    # Rewrite file without deleted contact
    with open(FILENAME, 'w', encoding='utf-8', newline='') as f:
        fieldnames = ['Name', 'Email', 'Phone']
        writer = csv.DictWriter(f, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(remaining)

    if found:
        print("Contact deleted successfully.")
    else:
        print("No matching contact found.")

    

def main():
    while True:
        print("\n Contact Book")
        print('1.Add Contact')
        print('2.View All Contacts')
        print('3.Search a contact')
        print('4.Delete a contact')
        print('5.Exit')

        choice=input("Choose an option(1-4)").strip()
        if choice=="1": add_contact()
        elif choice=="2": view_contact()
        elif choice=="3": search_contact()
        elif choice=="4": delete_contact()
        elif choice=="5": break
        else: print('Invalid choice.')

if __name__=="__main__":
    main()
