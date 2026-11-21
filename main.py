
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

        # Backend - Ready for SQL Server
        self.backend = None

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

        # Page Classes
        self.page_classes = {
            "Dashboard": DashboardPage,
            "Donors": DonorsPage,
            "Patients": PatientsPage,
            "Donations": DonationsPage,
            "Inventory": InventoryPage,
            "Dispensing": DispensingPage,
            "Reports": ReportsPage
        }

        # Sidebar Buttons
        self.sidebar_buttons = {}

        for page_name in self.page_classes:

            button = ctk.CTkButton(
                self.sidebar,
                text=page_name,
                height=45,
                corner_radius=8,
                fg_color="transparent",
                hover_color="#29456F",
                text_color="white",
                anchor="w",
                font=("Arial", 15),
                command=lambda p=page_name: self.show_page(p)
            )

            button.pack(
                fill="x",
                padx=15,
                pady=5
            )

            self.sidebar_buttons[page_name] = button

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

        # Open Dashboard
        self.show_page("Dashboard")

    # Page Navigation
    def show_page(self, page_name):

        # Reset Scroll Position
        self.scroll_area._parent_canvas.yview_moveto(0)

        # Destroy Previous Page
        if self.current_page is not None:
            self.current_page.destroy()

        # Update Active Sidebar Button
        for name, button in self.sidebar_buttons.items():

            if name == page_name:
                button.configure(
                    fg_color="#DC2626",
                    hover_color="#B91C1C",
                    text_color="white"
                )

            else:
                button.configure(
                    fg_color="transparent",
                    hover_color="#29456F",
                    text_color="white"
                )

        # Create Selected Page
        page_class = self.page_classes.get(page_name)

        if page_class is not None:

            self.current_page = page_class(
                self.scroll_area,
                backend=self.backend
            )

        # Ensure Scroll Starts at Top
        self.scroll_area._parent_canvas.yview_moveto(0)


if __name__ == "__main__":

    app = BloodBankApp()
    app.mainloop()
