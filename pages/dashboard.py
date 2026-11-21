
import customtkinter as ctk


class DashboardPage(ctk.CTkFrame):

    def __init__(self, parent, backend=None):
        super().__init__(
            parent,
            fg_color="#F4F6F9",
            corner_radius=0
        )

        self.backend = backend

        self.pack(fill="both", expand=True, padx=30, pady=25)

        # Page Title
        title = ctk.CTkLabel(
            self,
            text="Dashboard",
            font=("Arial", 30, "bold"),
            text_color="#172B4D"
        )
        title.pack(anchor="w", pady=(0, 5))

        subtitle = ctk.CTkLabel(
            self,
            text="Welcome to Blood Bank Management System",
            font=("Arial", 14),
            text_color="#7B8794"
        )
        subtitle.pack(anchor="w", pady=(0, 30))

        # Statistics Cards
        cards_frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )
        cards_frame.pack(fill="x", pady=10)

        cards_frame.grid_columnconfigure(
            (0, 1, 2, 3),
            weight=1
        )

        card_data = [
            ("Total Donors", "250", "#2563EB"),
            ("Total Patients", "120", "#0891B2"),
            ("Blood Units", "85", "#DC2626"),
            ("Total Donations", "180", "#16A34A")
        ]

        for index, (name, value, color) in enumerate(card_data):

            card = ctk.CTkFrame(
                cards_frame,
                fg_color="white",
                corner_radius=12,
                height=130
            )

            card.grid(
                row=0,
                column=index,
                padx=8,
                sticky="nsew"
            )

            card.grid_propagate(False)

            ctk.CTkLabel(
                card,
                text=name,
                font=("Arial", 14),
                text_color="#64748B"
            ).pack(anchor="w", padx=15, pady=(20, 10))

            ctk.CTkLabel(
                card,
                text=value,
                font=("Arial", 28, "bold"),
                text_color=color
            ).pack(anchor="w", padx=15)

        # Recent Donations Section
        donations_title = ctk.CTkLabel(
            self,
            text="Recent Donations",
            font=("Arial", 22, "bold"),
            text_color="#172B4D"
        )

        donations_title.pack(anchor="w", pady=(40, 15))

        # Table Header
        table = ctk.CTkFrame(
            self,
            fg_color="white",
            corner_radius=10
        )
        table.pack(fill="x")

        headers = [
            "Donor Name",
            "Blood Group",
            "Quantity",
            "Date"
        ]

        for index, header in enumerate(headers):

            table.grid_columnconfigure(index, weight=1)

            ctk.CTkLabel(
                table,
                text=header,
                font=("Arial", 13, "bold"),
                text_color="#172B4D"
            ).grid(
                row=0,
                column=index,
                padx=15,
                pady=15,
                sticky="w"
            )

        donations = [
            ("Ahmed Ali", "A+", "450 ml", "20/11/2026"),
            ("Mohamed Samir", "O+", "450 ml", "19/11/2026"),
            ("Omar Hassan", "B+", "450 ml", "18/11/2026"),
            ("Youssef Adel", "AB+", "450 ml", "17/11/2026")
        ]

        for row_index, donation in enumerate(donations, start=1):

            for col_index, item in enumerate(donation):

                ctk.CTkLabel(
                    table,
                    text=item,
                    font=("Arial", 13),
                    text_color="#475569"
                ).grid(
                    row=row_index,
                    column=col_index,
                    padx=15,
                    pady=13,
                    sticky="w"
                )
