import tkinter as tk

class GameApp:
    """Create and control the game interface."""

    def __init__(self, window):
        self.window = window
        self.selected_object = None
        self.inventory = []

        #Main window
        self.window.title("Monday, Again")
        self.window.geometry("1100x650")
        self.window.minsize(950,580)
        self.window.configure(bg="#10131c")

        #Make the middle section expand when the window is resized
        self.window.grid_rowconfigure(1, weight=1)
        self.window.grid_columnconfigure(0, weight=1)

        self.create_header()
        self.create_main_area()
        self.create_footer()

    def create_header(self):
        """Create the title and status bar."""
        header = tk.Frame(self.window, bg="#171c29", height=80)
        header.grid(row=0, column=0, sticky="ew")
        title = tk.Label(
            header, 
            text="MONDAY, AGAIN", 
            bg="#171c29", 
            fg="#f4f4f4", 
            font=("Arial", 24, "bold")
        )
        title.pack(
            pady=20,
            side = "left",
            padx = 30
        )

        status = tk.Label(
            header, 
            text="MONDAY 07:00   •   BEDROOM", 
            bg="#171c29", 
            fg="#8ea0ca", 
            font=("Arial", 11, "bold")
        )
        status.pack(
            pady = 20,
            side = "right",
            padx = 30
        )

    def create_main_area(self):
        """Create the scene and story panels."""
        main_area = tk.Frame(self.window, bg="#10131c")
        main_area.grid(row=1, column=0, sticky="nsew", padx=25, pady=20)
        main_area.grid_rowconfigure(0, weight=1)
        main_area.grid_columnconfigure(0, weight=7, uniform="main_content")
        main_area.grid_columnconfigure(1, weight=3, uniform="main_content")

        #Left side: room and clickable objects
        self.scene_frame = tk.Frame(
            main_area, 
            bg="#242b3d",
            highlightbackground="#3b4662",
            highlightthickness=1
        )
        self.scene_frame.grid(
            row=0,
            column=0,
            sticky="nsew",
            padx=(0, 12)
        )
        scene_title = tk.Label(
            self.scene_frame, 
            text="BEDROOM", 
            bg="#242b3d", 
            fg="#aebce0", 
            font=("Arial", 13, "bold")
        )
        scene_title.place(
            relx=0.05, 
            rely=0.06
        )
        room_description = tk.Label(
            self.scene_frame, 
            text=(
                "Pale moring light enters the room.\n"
                "Your phone buzzes quietly beside the bed, while the alarm clock reads 7:00 AM."
                  ), 
            bg="#242b3d", 
            fg="#8994ae", 
            font=("Arial", 11), 
            justify="left"
        )
        room_description.place(
            relx=0.05, 
            rely=0.14
        )

        #Clickable objects in the bedroom
        self.create_object_button(
            "WINDOW",
            0.15,
            0.38,
            lambda: self.select_object("Window")
        )
        self.create_object_button(
            "ALARM CLOCK",
            0.58,
            0.56,
            lambda: self.select_object("Alarm Clock")
        )
        self.create_object_button(
            "PHONE",
            0.35,
            0.76,
            lambda: self.select_object("Phone")
        )

        #Right side: story output
        story_panel = tk.Frame(
            main_area, 
            bg="#1a1f2d",
            highlightbackground="#3b4662",
            highlightthickness=1
        )
        story_panel.grid(
            row=0,
            column=1,
            sticky="nsew",
        )
        story_heading = tk.Label(
            story_panel,
            text="STORY",
            font=("Arial", 12, "bold"),
            fg="#aebce0",
            bg="#1a1f2d"
        )
        story_heading.pack(
            anchor="w",
            padx=25,
            pady=(25, 10)
        )
        self.story_text = tk.Label(
            story_panel,
            text=(
                "Your alarm rings at 7:00 AM.\n\n"
                "It is Monday morning.\n\n"
                "A bird taps twice against the window, "
                "and your phone vibrates on the bedside table."
            ),
            font=("Arial", 13),
            fg="#eeeeee",
            bg="#1a1f2d",
            justify="left",
            anchor="nw",
            wraplength=240
        )
        self.story_text.pack(
            fill="both",
            expand=True,
            padx=25,
            pady=(10, 25)
        )

    def create_object_button(self, text, x_position, y_position, command):
        """Create a clickable object inside the scene."""
        button = tk.Button(
            self.scene_frame,
            text=text,
            command=command,
            bg="#394768",
            fg="white",
            font=("Arial", 10, "bold"),
            relief="flat",
            activebackground="#6076aa",
            activeforeground="white",
            padx=16,
            pady=10
        )
        button.place(
            relx=x_position,
            rely=y_position
        )

    def create_footer(self):
        """Create the selected object and menu area."""
        footer = tk.Frame(self.window, bg="#171c29", height=85)
        footer.grid(row=2, column=0, sticky="ew")
        footer.grid_propagate(False)
        self.selected_label = tk.Label(
            footer,
            text="SELECTED: None",
            bg="#171c29",
            fg="#8ea0ca",
            font=("Arial", 10, "bold")
        )
        self.selected_label.pack(
            side="left",
            padx=30
        )
        interaction_frame = tk.Frame(
            footer,
            bg = "#171c29"
        )
        interaction_frame.pack(
            side = "left",
            padx = 10
        )

        self.inspect_button = tk.Button(
            interaction_frame,
            text = "INSPECT",
            command = self.inspect_selected,
            bg = "#394768",
            fg = "white",
            activebackground="#6076aa",
            activeforeground="white",
            disabledforeground="#697086",
            relief="flat",
            cursor="hand2",
            width=10,
            state="disabled"
        )
        self.inspect_button.pack(
            side="left",
            padx=5
        )

        self.take_button = tk.Button(
            interaction_frame,
            text="TAKE",
            command=self.take_selected,
            bg="#394768",
            fg="white",
            activebackground="#6076aa",
            activeforeground="white",
            disabledforeground="#697086",
            relief="flat",
            cursor="hand2",
            width=10,
            state="disabled"
        )
        self.take_button.pack(
            side="left",
            padx=5
        )

        self.use_button = tk.Button(
            interaction_frame,
            text="USE",
            command=self.use_selected,
            bg="#394768",
            fg="white",
            activebackground="#6076aa",
            activeforeground="white",
            disabledforeground="#697086",
            relief="flat",
            cursor="hand2",
            width=10,
            state="disabled"
        )
        self.use_button.pack(
            side="left",
            padx=5
        )

        journal_button = tk.Button(
            footer,
            text="JOURNAL",
            command=self.open_journal,
            bg="#2c354d",
            fg="white",
            activebackground="#53618e",
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            width=12
        )
        journal_button.pack(
            side="right",
            padx=(8, 30),
            pady=22
        )

        inventory_button = tk.Button(
            footer,
            text="INVENTORY",
            command = self.open_inventory,
            bg = "#2c354d",
            fg = "white",
            activebackground="#53618e",
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            width=12
        )
        inventory_button.pack(
            side="right",
            padx=8,
            pady=22
        )

    def show_object(self, object_name, story):
        """Select an object and display its description."""
        self.selected_object = object_name
        self.selected_label.config(
            text=f"SELECTED: {object_name}"
        )
        self.story_text.config(text=story)

    def inspect_window(self):
        self.show_object(
            "Window",
            (
                "You pull back the curtain.\n\n"
                "The number 17 bus stops across the road. "
                "Nobody gets off.\n\n"
                "The bird taps the glass twice, then flies away."
            )
        )

    def inspect_clock(self):
        self.show_object(
            "Alarm Clock",
            (
                "The alarm clock reads 07:00.\n\n"
                "Its battery cover is slightly loose.\n\n"
                "The second hand pauses for a moment, "
                "then continues moving."
            )
        )

    def inspect_phone(self):
        self.show_object(
            "Phone",
            (
                "Three unread messages from work.\n\n"
                "\"Don't be late again. We need to discuss "
                "your performance.\"\n\n"
                "You put the phone down. It is going to be "
                "another long Monday."
            )
        )

    def select_object(self, object_name):
        """Select an object without immediately interacting with it."""
        self.selected_object = object_name

        self.selected_label.config(
            text=f"SELECTED: {object_name}"
        )

        self.inspect_button.config(state="normal")
        self.use_button.config(state="normal")

        if object_name == "Phone" and "Phone" not in self.inventory:
            self.take_button.config(state="normal")
        else:
            self.take_button.config(state="disabled")

        self.story_text.config(
            text=(
                f"You focus your attention on the {object_name.lower()}.\n\n"
                "What would you like to do?"
            )
        )

    def inspect_selected(self):
        """Inspect the currently selected object."""
        if self.selected_object == "Window":
            self.inspect_window()

        elif self.selected_object == "Alarm Clock":
            self.inspect_clock()

        elif self.selected_object == "Phone":
            self.inspect_phone()

    def take_selected(self):
        """Take the selected object when possible."""
        if self.selected_object == "Phone":
            if "Phone" not in self.inventory:
                self.inventory.append("Phone")

                self.story_text.config(
                    text=(
                        "You pick up the phone and put it in your pocket."
                    )
                )

                self.take_button.config(state="disabled")

            else:
                self.story_text.config(
                    text=(
                        "You already have the phone."
                    )
                )

        else:
            self.story_text.config(
                text=(
                    "You cannot take that."
                )
            )

    def use_selected(self):
        """Use the currently selected object."""
        if self.selected_object == "Window":
            self.story_text.config(
                text=(
                    "The window is locked.\n\n"
                    "There is no reason to open it right now."
                )
            )

        elif self.selected_object == "Alarm Clock":
            self.story_text.config(
                text=(
                    "You press the button on top of the alarm clock.\n\n"
                    "The alarm stops."
                )
            )

        elif self.selected_object == "Phone":
            self.inspect_phone()

    def open_inventory(self):
        """Display the items currently carried by the player."""
        self.selected_object = None
        self.selected_label.config(text="SELECTED: Inventory")

        self.inspect_button.config(state="disabled")
        self.take_button.config(state="disabled")
        self.use_button.config(state="disabled")

        if self.inventory:
            item_list = "\n".join(
                f"• {item}" for item in self.inventory
            )

            self.story_text.config(
                text=(
                    "You are carrying:\n\n"
                    f"{item_list}"
                )
            )
        else:
            self.story_text.config(
                text=(
                    "Your inventory is currently empty."
                )
            )
        

    def open_journal(self):
        self.show_object(
            "Journal",
            (
                "Monday\n\n"
                "Nothing unusual has been recorded yet."
            )
        )

def main():
        """Start the program."""
        window = tk.Tk()
        game = GameApp(window)
        window.mainloop()

if __name__ == "__main__":
    main()