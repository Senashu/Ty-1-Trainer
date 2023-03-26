import time

import customtkinter as ctk
import keyboard as kb
from pymem import *
from pymem.process import *

mem = Pymem("Ty.exe")
module = module_from_name(mem.process_handle, "Ty.exe").lpBaseOfDll

Glide = 0x288964        # 5.5
GlideSpeed = 0x288928   # 7.0
RunSpeed = 0x288914     # 10.0
JumpHeightG = 0x28893C  # 18.57417488
JumpHeightW = 0x288998  # 10.67707825
JumpPeak = 0x2720F4     # this is weird IDK

# TyState values 35=standing, 5=running, 6=180 slide, 7=jumping, 8=extended glide, 9=gliding, 47=jump dive, 49=enter dive?,
# 39=swim, 17=moving while swim(gs), 38=surface, 15=moving on surface, 16=dive, 1=bite, 33=collect animation 0=enter level
# 32=hit by enemy, 10 = ledgegrab, 46=slippy fall 48=recover from failed bite,31=thing on head,

TyState1 = 0x27158C
TyState2 = 0x26EE4C

X = 0x270B78
Y = 0x270B7C
Z = 0x270B80

ctk.set_default_color_theme("dark-blue")


class Trainer:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.geometry('500x500+710+280+0')
        self.root.resizable(False, False)
        self.root.attributes('-alpha', 0.95)
        self.root.attributes('-topmost', False)
        self.root.overrideredirect(True)

        # fonts
        my_font = ctk.CTkFont(family="Arial Black", size=24, weight="bold")
        my_font2 = ctk.CTkFont(family="Arial Black", size=18, weight="bold")

        self.rightbar_visible = True  # new attribute to keep track of the rightbar visibility
        self.rightbar1_visible = False  # new attribute to keep track of the rightbar visibility
        self.rightbar2_visible = False  # new attribute to keep track of the rightbar visibility

        self.leftbar = ctk.CTkFrame(self.root, width=200, height=700, fg_color="#272727")
        self.leftbar.pack(side="left", fill="y")
        self.rightbar = ctk.CTkFrame(self.root)
        self.rightbar.pack(side="left", fill="both", expand=True)
        self.rightbar1 = ctk.CTkFrame(self.root)
        self.rightbar1.pack(side="left", fill="both", expand=True)
        self.rightbar1.pack_forget()
        self.rightbar2 = ctk.CTkFrame(self.root)
        self.rightbar2.pack(side="left", fill="both", expand=True)
        self.rightbar2.pack_forget()

        # Add widgets to left
        self.title_label = ctk.CTkLabel(self.leftbar, text="   Ty1 Trainer   ", font=my_font)
        self.title_label.pack(pady=40)

        self.left_button = ctk.CTkButton(self.leftbar, text="Movement", font=my_font2, width=200, height=40,
                                         command=lambda: self.ToggleRightbar())
        self.left_button.pack()

        self.left_button1 = ctk.CTkButton(self.leftbar, text="Position", font=my_font2, width=200, height=40,
                                          command=lambda: self.ToggleRightbar1())
        self.left_button1.pack()

        self.left_button2 = ctk.CTkButton(self.leftbar, text="Fun", font=my_font2, width=200, height=40,
                                          command=lambda: self.ToggleRightbar2())
        self.left_button2.pack()

        self.exit_btn = ctk.CTkButton(self.leftbar, text="Exit", font=my_font2, width=200, height=10,
                                      command=self.root.destroy)
        self.exit_btn.pack(side="bottom")

        # widgets to Movement

        self.switch = ctk.CTkSwitch(self.rightbar, text="Glide Down/Up", onvalue=0, offvalue=1,
                                    command=lambda: self.ToggleGlide())
        self.switch.pack(side="top", anchor="w", pady=5, padx=20)
        self.switch1 = ctk.CTkSwitch(self.rightbar, text="Glide Speed", onvalue=0, offvalue=1,
                                     command=lambda: self.ToggleGlideSpeed())
        self.switch1.pack(side="top", anchor="w", ipady=5, padx=20)

        self.switch2 = ctk.CTkSwitch(self.rightbar, text="Run Speed", onvalue=0, offvalue=1,
                                     command=lambda: self.ToggleRunSpeed())
        self.switch2.pack(side="top", anchor="w", ipady=5, padx=20)

        self.switch3 = ctk.CTkSwitch(self.rightbar, text="JumpHeight Ground", onvalue=0, offvalue=1,
                                     command=lambda: self.ToggleJumpHeightG())
        self.switch3.pack(side="top", anchor="w", ipady=5, padx=20)

        self.switch4 = ctk.CTkSwitch(self.rightbar, text="JumpHeight Water/Ice", onvalue=0, offvalue=1,
                                     command=lambda: self.ToggleJumpHeightW())
        self.switch4.pack(side="top", anchor="w", ipady=5, padx=20)

        self.switch5 = ctk.CTkCheckBox(self.rightbar, text="JumpPeak (Buggy)",
                                       onvalue=1, offvalue=0, command=self.ToggleJumpPeak)
        self.switch5.pack(side="top", anchor="w", ipady=5, padx=20)

        self.groundswim_btn = ctk.CTkButton(self.rightbar, text="Groundswim", command=self.ToggleTyState)
        self.groundswim_btn.pack(side="top")

        # widgets to Position

        def optionmenu_callback(choice):
            buttons = {
                "Rainbow Cliffs": ["Spawn Z1", "Hub1", "Hub 2", "Hub 3", "Julius", "Gate Skip", "Behind Gate"],
                "Two Up": ["Spawn A1", "Bilby1", "Spyeggs", "Two Up Skip", "2nd Rang", "End"],
                "Walk in the Park": ["Spawn A2", "Walk Skip", "Ken", "Turkey"],
                "Ship Rex": ["Spawn A3", "Lost Kids Mission", "Ship", "Gate", "Spire Swim", "Top Spire"],
                "Bull's Pen": [],
                "Bridge on the River Ty": [],
                # Add more options here
            }

            for button in buttons:
                if choice == button:
                    for text in buttons[button]:
                        btn_name = "btn_" + text  # Add prefix to make button attribute name unique
                        if not hasattr(self, btn_name):
                            setattr(self, btn_name, ctk.CTkButton(self.rightbar1, text=text))
                        getattr(self, btn_name).pack()
                        if text == "Spawn Z1":
                            getattr(self, btn_name).configure(command=self.Spawn_Z1)
                        elif text == "Hub1":
                            getattr(self, btn_name).configure(command=self.Hub1)
                        elif text == "Hub 2":
                            getattr(self, btn_name).configure(command=self.Hub2)
                        elif text == "Hub 3":
                            getattr(self, btn_name).configure(command=self.Hub3)
                        elif text == "Julius":
                            getattr(self, btn_name).configure(command=self.Julius)
                        elif text == "Gate Skip":
                            getattr(self, btn_name).configure(command=self.Gate_Skip)
                        elif text == "Behind Gate":
                            getattr(self, btn_name).configure(command=self.Behind_Gate)
                        elif text == "Spawn A1":
                            getattr(self, btn_name).configure(command=self.Spawn_A1)
                        elif text == "Bilby1":
                            getattr(self, btn_name).configure(command=self.Bilby1)
                        elif text == "Spyeggs":
                            getattr(self, btn_name).configure(command=self.Spyeggs)
                        elif text == "Two Up Skip":
                            getattr(self, btn_name).configure(command=self.Two_Up_Skip)
                        elif text == "2nd Rang":
                            getattr(self, btn_name).configure(command=self.Second_Rang)
                        elif text == "End":
                            getattr(self, btn_name).configure(command=self.End)
                        elif text == "Spawn A2":
                            getattr(self, btn_name).configure(command=self.Spawn_A2)
                        elif text == "Walk Skip":
                            getattr(self, btn_name).configure(command=self.Walk_Skip)
                        elif text == "Ken":
                            getattr(self, btn_name).configure(command=self.Ken)
                        elif text == "Turkey":
                            getattr(self, btn_name).configure(command=self.Turkey)
                        elif text == "Spawn A3":
                            getattr(self, btn_name).configure(command=self.Spawn_A3)
                        elif text == "Lost Kids Mission":
                            getattr(self, btn_name).configure(command=self.Lost_Kids_Mission)
                        elif text == "Ship":
                            getattr(self, btn_name).configure(command=self.Ship)
                        elif text == "Spire Swim":
                            getattr(self, btn_name).configure(command=self.Spire_Swim)
                        elif text == "Top Spire":
                            getattr(self, btn_name).configure(command=self.Top_Spire)
                else:
                    for text in buttons[button]:
                        btn_name = "btn_" + text  # Add prefix to make button attribute name unique
                        if hasattr(self, btn_name):
                            getattr(self, btn_name).pack_forget()

        options = ["Select One", "Rainbow Cliffs", "Two Up", "Walk in the Park", "Ship Rex", "Bull's Pen",
                   "Bridge on the River Ty",
                   "Snow Worries", "Outback Safari", "Crikey", "Lyre Lyre", "Black Stump", "Rex marks", "Fluffy",
                   "Cass Pass", "Cass Crest", "Final Battle"]

        self.combobox = ctk.CTkOptionMenu(master=self.rightbar1, values=options, command=optionmenu_callback)
        self.combobox.pack()

    # widgets to Fun

    def ToggleRightbar(self):
        if not self.rightbar_visible:
            if self.rightbar1_visible:
                self.ToggleRightbar1()
            elif self.rightbar2_visible:
                self.ToggleRightbar2()
            self.rightbar.pack(side="left", fill="both", expand=True)
        else:
            self.rightbar.pack_forget()
        self.rightbar_visible = not self.rightbar_visible

    def ToggleRightbar1(self):
        if not self.rightbar1_visible:
            if self.rightbar_visible:
                self.ToggleRightbar()
            elif self.rightbar2_visible:
                self.ToggleRightbar2()
            self.rightbar1.pack(side="left", fill="both", expand=True)
        else:
            self.rightbar1.pack_forget()
        self.rightbar1_visible = not self.rightbar1_visible

    def ToggleRightbar2(self):
        if not self.rightbar2_visible:
            if self.rightbar_visible:
                self.ToggleRightbar()
            elif self.rightbar1_visible:
                self.ToggleRightbar1()
            self.rightbar2.pack(side="left", fill="both", expand=True)
        else:
            self.rightbar2.pack_forget()
        self.rightbar2_visible = not self.rightbar2_visible

    def Glide1(self):
        mem.write_float(module + Glide, 5.5)

    def Glide2(self):
        mem.write_float(module + Glide, -10.0)

    def ToggleGlide(self):
        if self.switch.get() == 1:
            self.Glide1()
        else:
            self.Glide2()

    def ToggleTyState(self):
        mem.write_int(module + TyState1, 17)
        mem.write_int(module + TyState2, 17)

    def GlideSpeed(self):
        mem.write_float(module + GlideSpeed, 7.0)

    def GlideSpeed1(self):
        mem.write_float(module + GlideSpeed, 40.0)

    def ToggleGlideSpeed(self):
        if self.switch1.get() == 1:
            self.GlideSpeed()
        else:
            self.GlideSpeed1()

    def RunSpeed(self):
        mem.write_float(module + RunSpeed, 10.0)

    def RunSpeed1(self):
        mem.write_float(module + RunSpeed, 50.0)

    def ToggleRunSpeed(self):
        if self.switch2.get() == 1:
            self.RunSpeed()
        else:
            self.RunSpeed1()

    def JumpHeightG(self):
        mem.write_float(module + JumpHeightG, 18.57417488)

    def JumpHeightG1(self):
        mem.write_float(module + JumpHeightG, 60.0)

    def ToggleJumpHeightG(self):
        if self.switch3.get() == 1:
            self.JumpHeightG()
        else:
            self.JumpHeightG1()

    def JumpHeightW(self):
        mem.write_float(module + JumpHeightW, 10.67707825)

    def JumpHeightW1(self):
        mem.write_float(module + JumpHeightW, 30.0)

    def ToggleJumpHeightW(self):
        if self.switch4.get() == 1:
            self.JumpHeightW()
        else:
            self.JumpHeightW1()

    def JumpPeak(self):
        mem.write_float(module + JumpPeak, -1050.0)
        print(JumpPeak)

    def JumpPeak1(self):
        mem.write_float(module + JumpPeak, 1050.0)
        print(JumpPeak)

    def ToggleJumpPeak(self):
        if self.switch5.get() == 1:
            self.JumpPeak()
            while self.switch5.get() == 1:
                mem.write_float(module + JumpPeak, 1050.0)
                self.root.update()
                time.sleep(0.1)  # Delay for 100 milliseconds
        else:
            self.JumpPeak1()

    def Spawn_Z1(self):
        mem.write_float(module + X, 71.0)
        mem.write_float(module + Y, 2622.94)
        mem.write_float(module + Z, 209.0)

    def Hub1(self):
        mem.write_float(module + X, 620.701416)
        mem.write_float(module + Y, 2372.052979)
        mem.write_float(module + Z, 10123.121094)

    def Hub2(self):
        mem.write_float(module + X, -2785.978760)
        mem.write_float(module + Y, 190.369247)
        mem.write_float(module + Z, 9246.270508)

    def Hub3(self):
            mem.write_float(module + X, 4762.837891)
            mem.write_float(module + Y, 984.823120)
            mem.write_float(module + Z, 8713.142578)

    def Julius(self):
        mem.write_float(module + X, -6572.090820)
        mem.write_float(module + Y, 459.320984)
        mem.write_float(module + Z, 841.825317)

    def Gate_Skip(self):
        mem.write_float(module + X, -1984.073608)
        mem.write_float(module + Y, -199.427765)
        mem.write_float(module + Z, -3441.850830)

    def Behind_Gate(self):
        mem.write_float(module + X, 38.053028)
        mem.write_float(module + Y, 64.157181)
        mem.write_float(module + Z, -7441.100586)

    def Spawn_A1(self):
        mem.write_float(module + X, -2772.0)
        mem.write_float(module + Y, 1894.0)
        mem.write_float(module + Z, 26.0)

    def Bilby1(self):
        mem.write_float(module + X, -2469.0)
        mem.write_float(module + Y, 2965.0)
        mem.write_float(module + Z, 126.0)

    def Spyeggs(self):
        mem.write_float(module + X, -2983.0)
        mem.write_float(module + Y, 3486.0)
        mem.write_float(module + Z, 18.0)

    def Two_Up_Skip(self):
        mem.write_float(module + X, -1839.0)
        mem.write_float(module + Y, 1826.0)
        mem.write_float(module + Z, 36.0)

    def Second_Rang(self):
        mem.write_float(module + X, -3112.0)
        mem.write_float(module + Y, 3760.0)
        mem.write_float(module + Z, 59.0)

    def End(self):
        mem.write_float(module + X, -3955.0)
        mem.write_float(module + Y, 2804.0)
        mem.write_float(module + Z, 33.0)

    def Spawn_A2(self):
        mem.write_float(module + X, -2486.0)
        mem.write_float(module + Y, 2897.0)
        mem.write_float(module + Z, 6.0)

    def Walk_Skip(self):
        mem.write_float(module + X, -3227.0)
        mem.write_float(module + Y, 2678.0)
        mem.write_float(module + Z, 35.0)

    def Ken(self):
        mem.write_float(module + X, -3353.0)
        mem.write_float(module + Y, 1983.0)
        mem.write_float(module + Z, 5.0)

    def Turkey(self):
        mem.write_float(module + X, -3353.0)
        mem.write_float(module + Y, 1983.0)
        mem.write_float(module + Z, 5.0)

    def Spawn_A3(self):
        mem.write_float(module + X, -3353.0)
        mem.write_float(module + Y, 1983.0)
        mem.write_float(module + Z, 5.0)

    def Lost_Kids_Mission(self):
        mem.write_float(module + X, -3353.0)
        mem.write_float(module + Y, 1983.0)
        mem.write_float(module + Z, 5.0)

    def Ship(self):
        mem.write_float(module + X, -3353.0)
        mem.write_float(module + Y, 1983.0)
        mem.write_float(module + Z, 5.0)

    def Spire_Swim(self):
        mem.write_float(module + X, -3353.0)
        mem.write_float(module + Y, 1983.0)
        mem.write_float(module + Z, 5.0)

    def Top_Spire(self):
        mem.write_float(module + X, -3353.0)
        mem.write_float(module + Y, 1983.0)
        mem.write_float(module + Z, 5.0)


def keybinds(trainer):
    OPEN = "del"
    GlideSwitchXD = "1"
    GlideSpeedXD = "2"
    RunSpeedXD = "3"
    JumpHeightGXD = "4"
    JumpHeightWXD = "5"
    JumpPeakXD = "6"

    isopen = True

    def check_input():
        nonlocal isopen
        if kb.is_pressed(OPEN):
            if isopen:
                trainer.root.withdraw()
                isopen = False
            else:
                trainer.root.deiconify()
                isopen = True
                trainer.root.focus_force()
        if kb.is_pressed(GlideSwitchXD):
            trainer.switch.toggle()
        if kb.is_pressed(GlideSpeedXD):
            trainer.switch1.toggle()
        if kb.is_pressed(RunSpeedXD):
            trainer.switch2.toggle()
        if kb.is_pressed(JumpHeightGXD):
            trainer.switch3.toggle()
        if kb.is_pressed(JumpHeightWXD):
            trainer.switch4.toggle()
        if kb.is_pressed(JumpPeakXD):
            trainer.switch5.toggle()

        trainer.root.after(110, check_input)  # check for input every 100ms

    check_input()


trainer = Trainer()
keybinds(trainer)
trainer.root.mainloop()
