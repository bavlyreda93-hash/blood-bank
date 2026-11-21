
import customtkinter as ctk


class DonationsPage(ctk.CTkFrame):

    def __init__(self, parent, backend=None):
        super().__init__(
            parent,
            fg_color="#F4F6F9",
            corner_radius=0
        )

        self.backend = backend

        self.pack(fill="both", expand=True, padx=30, pady=25)

        self.donations = [
            {
                "id": 1,
                "donor": "Ahmed Ali",
                "date": "2026-11-10",
                "blood": "A+",
                "quantity": 450
            },
            {
                "id": 2,
                "donor": "Mohamed Samir",
                "date": "2026-11-12",
                "blood": "O+",
                "quantity": 450
            },
            {
                "id": 3,
                "donor": "Mariam Hassan",
                "date": "2026-11-15",
                "blood": "B+",
                "quantity": 450
            }
        ]

        ctk.CTkLabel(
            self,
            text="Donations Management",
            font=("Arial", 28, "bold"),
            text_color="#172B4D"
        ).pack(anchor="w", pady=(0, 5))

        ctk.CTkLabel(
            self,
            text="Manage all blood donation records",
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
            placeholder_text="Search donor...",
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
            text="+ Add Donation",
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
            "Donor Name",
            "Date",
            "Blood Group",
            "Quantity (ml)",
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
            d for d in self.donations
            if search in d["donor"].lower()
        ]

        for row, donation in enumerate(filtered, start=1):

            values = [
                donation["id"],
                donation["donor"],
                donation["date"],
                donation["blood"],
                donation["quantity"]
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
                command=lambda donation_id=donation["id"]:
                    self.delete_donation(donation_id)
            ).grid(
                row=row,
                column=5,
                padx=5,
                pady=10
            )

    def open_add_form(self):

        window = ctk.CTkToplevel(self)
        window.title("Add Donation")
        window.geometry("400x450")
        window.resizable(False, False)
        window.grab_set()

        ctk.CTkLabel(
            window,
            text="Add New Donation",
            font=("Arial", 22, "bold")
        ).pack(pady=20)

        donor_entry = ctk.CTkEntry(
            window,
            placeholder_text="Donor Name",
            width=300
        )
        donor_entry.pack(pady=12)

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
            placeholder_text="Quantity in ml",
            width=300
        )
        quantity_entry.pack(pady=12)

        def save_donation():

            donor = donor_entry.get().strip()
            date = date_entry.get().strip()
            quantity = quantity_entry.get().strip()

            if not donor or not date or not quantity:
                return

            try:
                quantity = int(quantity)

                if quantity <= 0:
                    return

            except ValueError:
                return

            new_donation = {
                "id": max(
                    [d["id"] for d in self.donations],
                    default=0
                ) + 1,
                "donor": donor,
                "date": date,
                "blood": blood_menu.get(),
                "quantity": quantity
            }

            self.donations.append(new_donation)

            self.update_table()
            window.destroy()

        ctk.CTkButton(
            window,
            text="Save Donation",
            width=200,
            command=save_donation
        ).pack(pady=20)

    def delete_donation(self, donation_id):

        self.donations = [
            d for d in self.donations
            if d["id"] != donation_id
        ]

        self.update_table()
