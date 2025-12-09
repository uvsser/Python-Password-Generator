# gui.py
import customtkinter as ctk
from main import password_generator  # import your existing function


class PasswordApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Window setup
        self.title("Python Password Generator")
        self.geometry("520x260")
        self.resizable(False, False)

        # Global appearance
        ctk.set_appearance_mode("dark")        # "light", "dark", or "system"
        ctk.set_default_color_theme("dark-blue")

        # Grid config
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        # Main frame (card)
        frame = ctk.CTkFrame(self, corner_radius=16)
        frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        for i in range(4):
            frame.rowconfigure(i, weight=0)
        frame.columnconfigure(0, weight=1)
        frame.columnconfigure(1, weight=1)

        # Title
        title = ctk.CTkLabel(
            frame,
            text="Secure Password Generator",
            font=ctk.CTkFont(size=20, weight="bold"),
        )
        title.grid(row=0, column=0, columnspan=2, pady=(12, 4))

        subtitle = ctk.CTkLabel(
            frame,
            text="Choose length and generate a strong password.",
            font=ctk.CTkFont(size=12),
        )
        subtitle.grid(row=1, column=0, columnspan=2, pady=(0, 12))

        # Length slider + label
        self.length_var = ctk.IntVar(value=16)

        length_label = ctk.CTkLabel(frame, text="Password length", anchor="w")
        length_label.grid(row=2, column=0, sticky="w", padx=16)

        self.length_value_label = ctk.CTkLabel(
            frame,
            text=f"{self.length_var.get()} characters",
            anchor="e",
        )
        self.length_value_label.grid(row=2, column=1, sticky="e", padx=16)

        self.length_slider = ctk.CTkSlider(
            frame,
            from_=8,
            to=64,
            number_of_steps=56,
            variable=self.length_var,
            command=self._on_length_change,
        )
        self.length_slider.grid(row=3, column=0, columnspan=2,
                                padx=16, pady=(0, 12), sticky="ew")

        # Output entry
        self.password_entry = ctk.CTkEntry(
            frame,
            placeholder_text="Click Generate",
            width=340,
        )
        self.password_entry.grid(row=4, column=0, columnspan=2,
                                 padx=16, pady=(4, 8), sticky="ew")

        # Buttons row
        button_frame = ctk.CTkFrame(frame, fg_color="transparent")
        button_frame.grid(row=5, column=0, columnspan=2, pady=(4, 12))

        generate_btn = ctk.CTkButton(
            button_frame,
            text="Generate",
            command=self._generate_password,
            width=140,
        )
        generate_btn.grid(row=0, column=0, padx=8)

        copy_btn = ctk.CTkButton(
            button_frame,
            text="Copy",
            command=self._copy_to_clipboard,
            width=100,
            fg_color="transparent",
            border_width=1,
            border_color="#4f9dff",
        )
        copy_btn.grid(row=0, column=1, padx=8)

        # Status label
        self.status_label = ctk.CTkLabel(
            frame,
            text="",
            font=ctk.CTkFont(size=11),
            text_color=("gray20", "gray80"),
        )
        self.status_label.grid(row=6, column=0, columnspan=2, pady=(0, 4))

    def _on_length_change(self, value):
        value = int(value)
        self.length_value_label.configure(text=f"{value} characters")

    def _generate_password(self):
        length = self.length_var.get()
        try:
            pwd = password_generator(length)
            self.password_entry.delete(0, "end")
            self.password_entry.insert(0, pwd)
            self.status_label.configure(text="New password generated.")
        except ValueError as e:
            self.status_label.configure(text=str(e))

    def _copy_to_clipboard(self):
        pwd = self.password_entry.get()
        if not pwd:
            self.status_label.configure(text="Nothing to copy.")
            return
        self.clipboard_clear()
        self.clipboard_append(pwd)
        self.status_label.configure(text="Password copied to clipboard.")


if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")
    app = PasswordApp()
    app.mainloop()
