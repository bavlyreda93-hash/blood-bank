
import customtkinter as ctk
from tkinter import messagebox


class DonorsPage(ctk.CTkFrame):

    def __init__(self, parent, backend=None):
        super().__init__(
            parent,
            fg_color="#F4F6F9",
            corner_radius=0
        )

        self.backend = backend

        self.donors = [
            {"id": 1, "name": "Ahmed Ali", "age": 25, "gender": "Male", "blood": "A+", "phone": "01012345678"},
            {"id": 2, "name": "Mohamed Samir", "age": 30, "gender": "Male", "blood": "O+", "phone": "01112345678"},
            {"id": 3, "name": "Mariam Hassan", "age": 22, "gender": "Female", "blood": "B+", "phone": "01212345678"},
            {"id": 4, "name": "Youssef Adel", "age": 28, "gender": "Male", "blood": "AB+", "phone": "01512345678"},
            {"id": 5, "name": "Nour Ahmed", "age": 24, "gender": "Female", "blood": "O-", "phone": "01098765432"}
        ]

        self.pack(fill="both", expand=True, padx=30, pady=25)

        # Page Header
        header = ctk.CTkFrame(self, fg_color="transparent")
        header.pack(fill="x", pady=(0, 25))

        ctk.CTkLabel(
            header,
            text="Donors Management",
            font=("Arial", 28, "bold"),
            text_color="#172B4D"
        ).pack(anchor="w")

        ctk.CTkLabel(
            header,
            text="Manage and view all blood donors",
            font=("Arial", 14),
            text_color="#7B8794"
        ).pack(anchor="w", pady=(5, 0))

        # Search and Filter Section
        controls = ctk.CTkFrame(self, fg_color="transparent")
        controls.pack(fill="x", pady=(0, 20))

        self.search_entry = ctk.CTkEntry(
            controls,
            placeholder_text="Search donor by name...",
            width=250,
            height=40,
            corner_radius=8
        )
        self.search_entry.pack(side="left", padx=(0, 10))

        self.search_entry.bind(
            "<KeyRelease>",
            lambda event: self.update_table()
        )

        self.blood_filter = ctk.CTkComboBox(
            controls,
            values=[
                "All Blood Groups", "A+", "A-", "B+", "B-",
                "AB+", "AB-", "O+", "O-"
            ],
            width=170,
            height=40,
            command=lambda value: self.update_table()
        )

        self.blood_filter.set("All Blood Groups")
        self.blood_filter.pack(side="left")

        add_button = ctk.CTkButton(
            controls,
            text="+ Add Donor",
            width=130,
            height=40,
            corner_radius=8,
            fg_color="#DC2626",
            hover_color="#B91C1C",
            font=("Arial", 14, "bold"),
            command=self.open_add_form
        )
        add_button.pack(side="right")

        # Donors Table
        self.table_container = ctk.CTkFrame(
            self,
            fg_color="white",
            corner_radius=12
        )
        self.table_container.pack(fill="both", expand=True)

        self.table_container.grid_columnconfigure(
            (0, 1, 2, 3, 4, 5, 6),
            weight=1
        )

        self.update_table()

    # Update Donors Table
    def update_table(self):

        for widget in self.table_container.winfo_children():
            widget.destroy()

        headers = [
            "ID", "Donor Name", "Age",
            "Gender", "Blood Group", "Phone", "Action"
        ]

        for col, header in enumerate(headers):
            ctk.CTkLabel(
                self.table_container,
                text=header,
                font=("Arial", 13, "bold"),
                text_color="#172B4D"
            ).grid(
                row=0,
                column=col,
                padx=8,
                pady=18,
                sticky="w"
            )

        search_text = self.search_entry.get().lower()
        selected_blood = self.blood_filter.get()

        filtered_donors = [
            donor for donor in self.donors
            if search_text in donor["name"].lower()
            and (
                selected_blood == "All Blood Groups"
                or donor["blood"] == selected_blood
            )
        ]

        for row, donor in enumerate(filtered_donors, start=1):

            values = [
                donor["id"],
                donor["name"],
                donor["age"],
                donor["gender"],
                donor["blood"],
                donor["phone"]
            ]

            for col, value in enumerate(values):
                ctk.CTkLabel(
                    self.table_container,
                    text=str(value),
                    font=("Arial", 12),
                    text_color="#475569"
                ).grid(
                    row=row,
                    column=col,
                    padx=8,
                    pady=15,
                    sticky="w"
                )

            # Action Buttons
            action_frame = ctk.CTkFrame(
                self.table_container,
                fg_color="transparent"
            )

            action_frame.grid(
                row=row,
                column=6,
                padx=5,
                pady=10
            )

            ctk.CTkButton(
                action_frame,
                text="Edit",
                width=55,
                height=28,
                fg_color="#2563EB",
                hover_color="#1D4ED8",
                command=lambda d=donor.copy(): self.edit_donor(d)
            ).pack(side="left", padx=2)

            ctk.CTkButton(
                action_frame,
                text="Delete",
                width=60,
                height=28,
                fg_color="#DC2626",
                hover_color="#B91C1C",
                command=lambda donor_id=donor["id"]:
                    self.delete_donor(donor_id)
            ).pack(side="left", padx=2)

        if not filtered_donors:
            ctk.CTkLabel(
                self.table_container,
                text="No donors found",
                font=("Arial", 14),
                text_color="#94A3B8"
            ).grid(
                row=1,
                column=0,
                columnspan=7,
                pady=40
            )

    # Edit Donor
    def edit_donor(self, donor):

        edit_window = ctk.CTkToplevel(self)
        edit_window.title("Edit Donor")
        edit_window.geometry("400x500")
        edit_window.resizable(False, False)
        edit_window.grab_set()

        ctk.CTkLabel(
            edit_window,
            text="Edit Donor Information",
            font=("Arial", 22, "bold")
        ).pack(pady=20)

        name_entry = ctk.CTkEntry(
            edit_window,
            placeholder_text="Donor Name",
            width=300
        )
        name_entry.pack(pady=10)
        name_entry.insert(0, donor["name"])

        age_entry = ctk.CTkEntry(
            edit_window,
            placeholder_text="Age",
            width=300
        )
        age_entry.pack(pady=10)
        age_entry.insert(0, str(donor["age"]))

        gender_menu = ctk.CTkOptionMenu(
            edit_window,
            values=["Male", "Female"],
            width=300
        )
        gender_menu.pack(pady=10)
        gender_menu.set(donor["gender"])

        blood_menu = ctk.CTkOptionMenu(
            edit_window,
            values=["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"],
            width=300
        )
        blood_menu.pack(pady=10)
        blood_menu.set(donor["blood"])

        phone_entry = ctk.CTkEntry(
            edit_window,
            placeholder_text="Phone Number",
            width=300
        )
        phone_entry.pack(pady=10)
        phone_entry.insert(0, donor["phone"])

        def save_changes():

            name = name_entry.get().strip()
            age = age_entry.get().strip()
            gender = gender_menu.get()
            blood = blood_menu.get()
            phone = phone_entry.get().strip()

            if not name or not age or not phone:
                messagebox.showerror(
                    "Error",
                    "Please fill in all fields.",
                    parent=edit_window
                )
                return

            try:
                age = int(age)

                if age <= 0:
                    raise ValueError

            except ValueError:
                messagebox.showerror(
                    "Error",
                    "Please enter a valid age.",
                    parent=edit_window
                )
                return

            for item in self.donors:
                if item["id"] == donor["id"]:
                    item["name"] = name
                    item["age"] = age
                    item["gender"] = gender
                    item["blood"] = blood
                    item["phone"] = phone
                    break

            self.update_table()
            edit_window.destroy()

        ctk.CTkButton(
            edit_window,
            text="Save Changes",
            width=200,
            command=save_changes
        ).pack(pady=20)

    # Delete Donor
    def delete_donor(self, donor_id):

        confirm = messagebox.askyesno(
            "Confirm Delete",
            "Are you sure you want to delete this donor?"
        )

        if not confirm:
            return

        self.donors = [
            donor for donor in self.donors
            if donor["id"] != donor_id
        ]

        self.update_table()

    # Add New Donor
    def open_add_form(self):

        form = ctk.CTkToplevel(self)
        form.title("Add New Donor")
        form.geometry("400x500")
        form.resizable(False, False)
        form.configure(fg_color="#F4F6F9")
        form.transient(self.winfo_toplevel())
        form.grab_set()

        ctk.CTkLabel(
            form,
            text="Add New Donor",
            font=("Arial", 24, "bold"),
            text_color="#172B4D"
        ).pack(pady=20)

        name_entry = ctk.CTkEntry(
            form,
            placeholder_text="Donor Name",
            width=300,
            height=40
        )
        name_entry.pack(pady=8)

        age_entry = ctk.CTkEntry(
            form,
            placeholder_text="Age",
            width=300,
            height=40
        )
        age_entry.pack(pady=8)

        gender_box = ctk.CTkComboBox(
            form,
            values=["Male", "Female"],
            width=300,
            height=40
        )
        gender_box.set("Male")
        gender_box.pack(pady=8)

        blood_box = ctk.CTkComboBox(
            form,
            values=["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"],
            width=300,
            height=40
        )
        blood_box.set("A+")
        blood_box.pack(pady=8)

        phone_entry = ctk.CTkEntry(
            form,
            placeholder_text="Phone Number",
            width=300,
            height=40
        )
        phone_entry.pack(pady=8)

        def save_donor():

            name = name_entry.get().strip()
            age = age_entry.get().strip()
            gender = gender_box.get()
            blood = blood_box.get()
            phone = phone_entry.get().strip()

            if not name or not age or not phone:
                messagebox.showerror(
                    "Error",
                    "Please fill in all fields.",
                    parent=form
                )
                return

            if not age.isdigit() or int(age) <= 0:
                messagebox.showerror(
                    "Error",
                    "Please enter a valid age.",
                    parent=form
                )
                return

            new_donor = {
                "id": max(
                    [d["id"] for d in self.donors],
                    default=0
                ) + 1,
                "name": name,
                "age": int(age),
                "gender": gender,
                "blood": blood,
                "phone": phone
            }

            self.donors.append(new_donor)
            self.update_table()
            form.destroy()

        ctk.CTkButton(
            form,
            text="Save Donor",
            width=300,
            height=40,
            fg_color="#DC2626",
            hover_color="#B91C1C",
            command=save_donor
        ).pack(pady=20)
