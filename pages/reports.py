
import customtkinter as ctk


class ReportsPage(ctk.CTkFrame):

    def __init__(self, parent, backend=None):
        super().__init__(
            parent,
            fg_color="#F4F6F9",
            corner_radius=0
        )

        self.backend = backend

        self.pack(fill="both", expand=True, padx=30, pady=25)

        # Page Title
        ctk.CTkLabel(
            self,
            text="Reports & Statistics",
            font=("Arial", 28, "bold"),
            text_color="#172B4D"
        ).pack(anchor="w", pady=(0, 5))

        ctk.CTkLabel(
            self,
            text="Overview of Blood Bank performance",
            font=("Arial", 14),
            text_color="gray"
        ).pack(anchor="w", pady=(0, 25))

        # Statistics
        stats_frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )
        stats_frame.pack(fill="x", pady=10)

        self.create_card(
            stats_frame, "Total Donors", "250", 0
        )

        self.create_card(
            stats_frame, "Total Patients", "120", 1
        )

        self.create_card(
            stats_frame, "Total Donations", "180", 2
        )

        self.create_card(
            stats_frame, "Blood Units", "85", 3
        )

        # Blood Group Report
        ctk.CTkLabel(
            self,
            text="Blood Group Statistics",
            font=("Arial", 20, "bold"),
            text_color="#172B4D"
        ).pack(anchor="w", pady=(35, 15))

        self.report_frame = ctk.CTkFrame(self)
        self.report_frame.pack(fill="x", pady=10)

        blood_data = [
            ("A+", 12),
            ("A-", 5),
            ("B+", 10),
            ("B-", 4),
            ("AB+", 8),
            ("AB-", 3),
            ("O+", 15),
            ("O-", 6)
        ]

        for row, (blood, units) in enumerate(blood_data):

            ctk.CTkLabel(
                self.report_frame,
                text=blood,
                font=("Arial", 14, "bold"),
                width=70
            ).grid(
                row=row,
                column=0,
                padx=20,
                pady=8
            )

            progress = ctk.CTkProgressBar(
                self.report_frame,
                width=300
            )
            progress.grid(
                row=row,
                column=1,
                padx=15,
                pady=8
            )

            progress.set(units / 20)

            ctk.CTkLabel(
                self.report_frame,
                text=f"{units} Units",
                font=("Arial", 13)
            ).grid(
                row=row,
                column=2,
                padx=15,
                pady=8
            )

    def create_card(self, parent, title, value, column):

        card = ctk.CTkFrame(
            parent,
            corner_radius=12,
            width=180,
            height=120
        )

        card.grid(
            row=0,
            column=column,
            padx=8,
            sticky="ew"
        )

        parent.grid_columnconfigure(column, weight=1)

        ctk.CTkLabel(
            card,
            text=title,
            font=("Arial", 13),
            text_color="gray"
        ).pack(pady=(20, 8))

        ctk.CTkLabel(
            card,
            text=value,
            font=("Arial", 26, "bold"),
            text_color="#172B4D"
        ).pack()
