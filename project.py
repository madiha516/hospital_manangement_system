

patients = []
doctors = []
appointments = []

def add_patient():
    name = input("Enter patient name: ")
    age = input("Enter patient age: ")
    disease = input("Enter disease: ")
    patients.append({"Name": name, "Age": age, "Disease": disease})
    print(" Patient added successfully!\n")

def view_patients():
    if not patients:
        print("No patients found.\n")
    else:
        print("\n--- Patient List ---")
        for p in patients:
            print(f"Name: {p['Name']}, Age: {p['Age']}, Disease: {p['Disease']}")
        print()

def add_doctor():
    name = input("Enter doctor name: ")
    specialization = input("Enter specialization: ")
    doctors.append({"Name": name, "Specialization": specialization})
    print(" Doctor added successfully!\n")

def view_doctors():
    if not doctors:
        print("No doctors found.\n")
    else:
        print("\n--- Doctor List ---")
        for d in doctors:
            print(f"Name: {d['Name']}, Specialization: {d['Specialization']}")
        print()

def book_appointment():
    if not patients or not doctors:
        print(" Need at least 1 patient and 1 doctor to book appointment.\n")
        return
    patient_name = input("Enter patient name: ")
    doctor_name = input("Enter doctor name: ")
    appointments.append({"Patient": patient_name, "Doctor": doctor_name})
    print(" Appointment booked successfully!\n")

def view_appointments():
    if not appointments:
        print("No appointments booked.\n")
    else:
        print("\n--- Appointments ---")
        for a in appointments:
            print(f"Patient: {a['Patient']}  ->  Doctor: {a['Doctor']}")
        print()

while True:
    print("\n Hospital Management Menu ")
    print("1. Add Patient")
    print("2. View Patients")
    print("3. Add Doctor")
    print("4. View Doctors")
    print("5. Book Appointment")
    print("6. View Appointments")
    print("7. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_patient()
    elif choice == "2":
        view_patients()
    elif choice == "3":
        add_doctor()
    elif choice == "4":
        view_doctors()
    elif choice == "5":
        book_appointment()
    elif choice == "6":
        view_appointments()
    elif choice == "7":
        print("Exiting... Thank you!")
        break
    else:

        print("Invalid choice! Try again.\n")

