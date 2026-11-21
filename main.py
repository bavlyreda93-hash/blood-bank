
import customtkinter as ctk

from pages.dashboard import DashboardPage
from pages.donors import DonorsPage
from pages.patients import PatientsPage
from pages.donations import DonationsPage
from pages.inventory import InventoryPage
from pages.dispensing import DispensingPage
from pages.reports import ReportsPage


class BloodBankApp(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Blood Bank Management System")
        self.geometry("1200x750")
        self.minsize(1000, 650)

        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")

        self.configure(fg_color="#F4F6F9")

        # Main Layout
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Sidebar
        self.sidebar = ctk.CTkFrame(
            self,
            width=220,
            corner_radius=0,
            fg_color="#172B4D"
        )

        self.sidebar.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

        self.sidebar.grid_propagate(False)

        # Application Title
        self.logo = ctk.CTkLabel(
            self.sidebar,
            text="BLOOD BANK",
            font=("Arial", 23, "bold"),
            text_color="white"
        )

        self.logo.pack(pady=(35, 40))

        # Navigation Buttons
        self.pages = [
            "Dashboard",
            "Donors",
            "Patients",
            "Donations",
            "Inventory",
            "Dispensing",
            "Reports"
        ]

        for page in self.pages:

            button = ctk.CTkButton(
                self.sidebar,
                text=page,
                height=45,
                corner_radius=8,
                fg_color="transparent",
                hover_color="#29456F",
                text_color="white",
                anchor="w",
                font=("Arial", 15),
                command=lambda p=page: self.show_page(p)
            )

            button.pack(
                fill="x",
                padx=15,
                pady=5
            )

        # Main Content Area
        self.content = ctk.CTkFrame(
            self,
            corner_radius=0,
            fg_color="#F4F6F9"
        )

        self.content.grid(
            row=0,
            column=1,
            sticky="nsew"
        )

        self.content.grid_columnconfigure(0, weight=1)
        self.content.grid_rowconfigure(0, weight=1)

        # Global Scroll Area
        self.scroll_area = ctk.CTkScrollableFrame(
            self.content,
            fg_color="#F4F6F9",
            corner_radius=0,
            scrollbar_button_color="#94A3B8",
            scrollbar_button_hover_color="#64748B"
        )

        self.scroll_area.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

        self.scroll_area.grid_columnconfigure(0, weight=1)

        self.current_page = None

        # Open Dashboard at startup
        self.show_page("Dashboard")

    # Page Navigation
    def show_page(self, page_name):

        if self.current_page is not None:
            self.current_page.destroy()

        if page_name == "Dashboard":
            self.current_page = DashboardPage(self.scroll_area)

        elif page_name == "Donors":
            self.current_page = DonorsPage(self.scroll_area)

        elif page_name == "Patients":
            self.current_page = PatientsPage(self.scroll_area)

        elif page_name == "Donations":
            self.current_page = DonationsPage(self.scroll_area)

        elif page_name == "Inventory":
            self.current_page = InventoryPage(self.scroll_area)

        elif page_name == "Dispensing":
            self.current_page = DispensingPage(self.scroll_area)

        elif page_name == "Reports":
            self.current_page = ReportsPage(self.scroll_area)


if __name__ == "__main__":
    app = BloodBankApp()
    app.mainloop()
