
import customtkinter as ctk


class DispensingPage(ctk.CTkFrame):

    def __init__(self, parent, backend=None):
        super().__init__(
            parent,
            fg_color="#F4F6F9",
            corner_radius=0
        )

        self.backend = backend

        self.pack(fill="both", expand=True, padx=30, pady=25)

        self.dispensings = [
            {
                "id": 1,
                "patient": "Ahmed Hassan",
                "date": "2026-11-10",
                "blood": "A+",
                "quantity": 1
            },
            {
                "id": 2,
                "patient": "Mariam Ali",
                "date": "2026-11-12",
                "blood": "O+",
                "quantity": 2
            }
        ]

        ctk.CTkLabel(
            self,
            text="Blood Dispensing",
            font=("Arial", 28, "bold"),
            text_color="#172B4D"
        ).pack(anchor="w", pady=(0, 5))

        ctk.CTkLabel(
            self,
            text="Manage blood units dispensed to patients",
            font=("Arial", 14),
            text_color="gray"
        ).pack(anchor="w", pady=(0, 25))

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
            text="+ New Dispensing",
            height=40,
            command=self.open_add_form
        ).pack(side="right")

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
            "Date",
            "Blood Group",
            "Units",
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
                padx=15,
                pady=15
            )

        search = self.search_entry.get().lower()

        filtered = [
            item for item in self.dispensings
            if search in item["patient"].lower()
        ]

        for row, item in enumerate(filtered, start=1):

            values = [
                item["id"],
                item["patient"],
                item["date"],
                item["blood"],
                item["quantity"]
            ]

            for col, value in enumerate(values):
                ctk.CTkLabel(
                    self.table_container,
                    text=str(value),
                    font=("Arial", 13)
                ).grid(
                    row=row,
                    column=col,
                    padx=15,
                    pady=12
                )

            ctk.CTkButton(
                self.table_container,
                text="Delete",
                width=65,
                height=28,
                fg_color="#DC2626",
                hover_color="#B91C1C",
                command=lambda item_id=item["id"]:
                    self.delete_dispensing(item_id)
            ).grid(
                row=row,
                column=5,
                padx=5,
                pady=10
            )

    def open_add_form(self):

        window = ctk.CTkToplevel(self)
        window.title("New Dispensing")
        window.geometry("400x450")
        window.resizable(False, False)
        window.grab_set()

        ctk.CTkLabel(
            window,
            text="New Blood Dispensing",
            font=("Arial", 22, "bold")
        ).pack(pady=20)

        patient_entry = ctk.CTkEntry(
            window,
            placeholder_text="Patient Name",
            width=300
        )
        patient_entry.pack(pady=12)

        date_entry = ctk.CTkEntry(
            window,
            placeholder_text="Date (YYYY-MM-DD)",
            width=300
        )
        date_entry.pack(pady=12)

        blood_menu = ctk.CTkOptionMenu(
            window,
            values=["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"],
            width=300
        )
        blood_menu.pack(pady=12)

        quantity_entry = ctk.CTkEntry(
            window,
            placeholder_text="Number of Units",
            width=300
        )
        quantity_entry.pack(pady=12)

        def save_dispensing():

            patient = patient_entry.get().strip()
            date = date_entry.get().strip()
            quantity = quantity_entry.get().strip()

            if not patient or not date or not quantity:
                return

            try:
                quantity = int(quantity)

                if quantity <= 0:
                    return

            except ValueError:
                return

            new_item = {
                "id": max(
                    [d["id"] for d in self.dispensings],
                    default=0
                ) + 1,
                "patient": patient,
                "date": date,
                "blood": blood_menu.get(),
                "quantity": quantity
            }

            self.dispensings.append(new_item)

            self.update_table()
            window.destroy()

        ctk.CTkButton(
            window,
            text="Save Dispensing",
            width=200,
            command=save_dispensing
        ).pack(pady=20)

    def delete_dispensing(self, item_id):

        self.dispensings = [
            d for d in self.dispensings
            if d["id"] != item_id
        ]

        self.update_table()
