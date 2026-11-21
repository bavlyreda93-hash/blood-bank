
import customtkinter as ctk


class InventoryPage(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)

        self.pack(fill="both", expand=True, padx=30, pady=25)

        self.inventory = [
            {"id": 1, "blood": "A+", "units": 12},
            {"id": 2, "blood": "A-", "units": 5},
            {"id": 3, "blood": "B+", "units": 10},
            {"id": 4, "blood": "B-", "units": 4},
            {"id": 5, "blood": "AB+", "units": 8},
            {"id": 6, "blood": "AB-", "units": 3},
            {"id": 7, "blood": "O+", "units": 15},
            {"id": 8, "blood": "O-", "units": 6}
        ]

        ctk.CTkLabel(
            self,
            text="Blood Inventory",
            font=("Arial", 28, "bold"),
            text_color="#172B4D"
        ).pack(anchor="w", pady=(0, 5))

        ctk.CTkLabel(
            self,
            text="Monitor available blood units",
            font=("Arial", 14),
            text_color="gray"
        ).pack(anchor="w", pady=(0, 25))

        self.total_label = ctk.CTkLabel(
            self,
            text="",
            font=("Arial", 18, "bold")
        )
        self.total_label.pack(anchor="w", pady=10)

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

        total_units = sum(
            item["units"] for item in self.inventory
        )

        self.total_label.configure(
            text=f"Total Blood Units: {total_units}"
        )

        headers = [
            "ID",
            "Blood Group",
            "Available Units",
            "Status"
        ]

        for col, header in enumerate(headers):
            ctk.CTkLabel(
                self.table_container,
                text=header,
                font=("Arial", 15, "bold")
            ).grid(
                row=0,
                column=col,
                padx=30,
                pady=20
            )

        for row, item in enumerate(self.inventory, start=1):

            if item["units"] <= 3:
                status = "Low Stock"
                color = "#DC2626"
            elif item["units"] <= 7:
                status = "Medium Stock"
                color = "#D97706"
            else:
                status = "Available"
                color = "#16A34A"

            values = [
                item["id"],
                item["blood"],
                item["units"]
            ]

            for col, value in enumerate(values):
                ctk.CTkLabel(
                    self.table_container,
                    text=str(value),
                    font=("Arial", 14)
                ).grid(
                    row=row,
                    column=col,
                    padx=30,
                    pady=15
                )

            ctk.CTkLabel(
                self.table_container,
                text=status,
                text_color=color,
                font=("Arial", 14, "bold")
            ).grid(
                row=row,
                column=3,
                padx=30,
                pady=15
            )

