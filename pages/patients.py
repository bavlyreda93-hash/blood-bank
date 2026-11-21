
import customtkinter as ctk


class PatientsPage(ctk.CTkFrame):

    def __init__(self, parent, backend=None):
        super().__init__(
            parent,
            fg_color="#F4F6F9",
            corner_radius=0
        )

        self.backend = backend

        self.pack(fill="both", expand=True, padx=30, pady=25)

        self.patients = [
            {
                "id": 1,
                "name": "Ahmed Hassan",
                "age": 35,
                "gender": "Male",
                "blood": "A+",
                "phone": "01012345678"
            },
            {
                "id": 2,
                "name": "Mariam Ali",
                "age": 28,
                "gender": "Female",
                "blood": "O+",
                "phone": "01112345678"
            },
            {
                "id": 3,
                "name": "Omar Samir",
                "age": 42,
                "gender": "Male",
                "blood": "B+",
                "phone": "01212345678"
            }
        ]

        # Page Title
        ctk.CTkLabel(
            self,
            text="Patients Management",
            font=("Arial", 28, "bold"),
            text_color="#172B4D"
        ).pack(anchor="w", pady=(0, 5))

        ctk.CTkLabel(
            self,
            text="Manage and view all registered patients",
            font=("Arial", 14),
            text_color="gray"
        ).pack(anchor="w", pady=(0, 25))

        # Search and Add
        top_frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )
        top_frame.pack(fill="x", pady=10)

        self.search_entry = ctk.CTkEntry(
            top_frame,
            placeholder_text="Search patient...",
            width=250,
            height=40
        )
        self.search_entry.pack(side="left")

        self.search_entry.bind(
            "<KeyRelease>",
            lambda event: self.update_table()
        )

        ctk.CTkButton(
            top_frame,
            text="+ Add Patient",
            height=40,
            command=self.open_add_form
        ).pack(side="right")

        # Table
        self.table_container = ctk.CTkFrame(self)
        self.table_container.pack(
            fill="both",
            expand=True,
            pady=15
        )

        self.update_table()

    def update_table(self):

        for widget in self.table_container.winfo_children():
            widget.destroy()

        headers = [
            "ID",
            "Patient Name",
            "Age",
            "Gender",
            "Blood Group",
            "Phone",
            "Action"
        ]

        for col, header in enumerate(headers):
            ctk.CTkLabel(
                self.table_container,
                text=header,
                font=("Arial", 14, "bold")
            ).grid(
                row=0,
                column=col,
                padx=10,
                pady=15
            )

        search = self.search_entry.get().lower()

        filtered = [
            p for p in self.patients
            if search in p["name"].lower()
        ]

        for row, patient in enumerate(filtered, start=1):

            values = [
                patient["id"],
                patient["name"],
                patient["age"],
                patient["gender"],
                patient["blood"],
                patient["phone"]
            ]

            for col, value in enumerate(values):
                ctk.CTkLabel(
                    self.table_container,
                    text=str(value),
                    font=("Arial", 13)
                ).grid(
                    row=row,
                    column=col,
                    padx=10,
                    pady=12
                )

            ctk.CTkButton(
                self.table_container,
                text="Delete",
                width=65,
                height=28,
                fg_color="#DC2626",
                hover_color="#B91C1C",
                command=lambda patient_id=patient["id"]:
                    self.delete_patient(patient_id)
            ).grid(
                row=row,
                column=6,
                padx=5,
                pady=10
            )

    def open_add_form(self):

        window = ctk.CTkToplevel(self)
        window.title("Add Patient")
        window.geometry("400x480")
        window.resizable(False, False)
        window.grab_set()

        ctk.CTkLabel(
            window,
            text="Add New Patient",
            font=("Arial", 22, "bold")
        ).pack(pady=20)

        name_entry = ctk.CTkEntry(
            window,
            placeholder_text="Patient Name",
            width=300
        )
        name_entry.pack(pady=10)

        age_entry = ctk.CTkEntry(
            window,
            placeholder_text="Age",
            width=300
        )
        age_entry.pack(pady=10)

        gender_menu = ctk.CTkOptionMenu(
            window,
            values=["Male", "Female"],
            width=300
        )
        gender_menu.pack(pady=10)

        blood_menu = ctk.CTkOptionMenu(
            window,
            values=["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"],
            width=300
        )
        blood_menu.pack(pady=10)

        phone_entry = ctk.CTkEntry(
            window,
            placeholder_text="Phone Number",
            width=300
        )
        phone_entry.pack(pady=10)

        def save_patient():

            name = name_entry.get().strip()
            age = age_entry.get().strip()
            phone = phone_entry.get().strip()

            if not name or not age or not phone:
                return

            try:
                age = int(age)

                if age <= 0:
                    return

            except ValueError:
                return

            new_patient = {
                "id": max(
                    [p["id"] for p in self.patients],
                    default=0
                ) + 1,
                "name": name,
                "age": age,
                "gender": gender_menu.get(),
                "blood": blood_menu.get(),
                "phone": phone
            }

            self.patients.append(new_patient)

            self.update_table()
            window.destroy()

        ctk.CTkButton(
            window,
            text="Save Patient",
            width=200,
            command=save_patient
        ).pack(pady=20)

    def delete_patient(self, patient_id):

        self.patients = [
            p for p in self.patients
            if p["id"] != patient_id
        ]

        self.update_table()
