import customtkinter as ctk
import keyboard
from TyAttributes import *
from Movement import *
from Position import *

pm = Pymem("TY.exe")

root = ctk.CTk()
root.title('TY Tool')
root.geometry('518x620+710+280+0')
root.resizable(False, False)
root.attributes('-alpha', 1)
root.attributes('-topmost', True)
root.overrideredirect(True)
TyFont = ctk.CTkFont(family="SF Slapstick Comic", size=20)
TyFontS = ctk.CTkFont(family="SF Slapstick Comic", size=14)

frame_buttons = ctk.CTkFrame(root, bg_color="white", width=100, height=500)
frame_buttons.pack(side="left", anchor="n")
frame1 = ctk.CTkFrame(root, bg_color="red", width=400, height=500)
frame2 = ctk.CTkFrame(root, bg_color="green", width=400, height=500)
frame3 = ctk.CTkFrame(root, bg_color="blue", width=400, height=500)
frame4 = ctk.CTkFrame(root, bg_color="red", width=400, height=500)
frame5 = ctk.CTkFrame(root, bg_color="green", width=400, height=500)
frame6 = ctk.CTkFrame(root, bg_color="blue", width=400, height=500)

frame1.pack_forget()
frame2.pack_forget()
frame3.pack_forget()


def toggle_window():
    root.withdraw()


def bring_window_back():
    root.deiconify()
    root.focus_force()


def handle_key_press(event):
    global isopen
    if event.name == '1':
        if isopen:
            root.withdraw()
            isopen = False
        else:
            root.deiconify()
            isopen = True
            root.focus_force()
    elif event.name == '2':
        TyStateButton.invoke()
    elif event.name == '3':
        GiveAll_Button.invoke()
    elif event.name == '4' and event.event_type == keyboard.KEY_DOWN and keyboard.is_pressed('ctrl'):
        RemoveAll_Button.invoke()


def check_input():
    keyboard.on_press(handle_key_press)


isopen = True
root.after(100, check_input)


def select_frame(frame_num):
    frames = [frame1, frame2, frame3, frame4, frame5, frame6]
    buttons = [
        GiveAll_Button, RemoveAll_Button, Test, Give_Techno_Button, Give_Elemental_Button, Test2, TwoRang_switch,
        Dive_switch, swim_switch, Aqua_switch, Frosty_switch, Flame_switch, Zappy_switch, Kaboom_switch, Doomer_switch,
        Zoomer_switch, Infra_switch, Multi_switch, Chrono_switch, Mega_switch, Glide, GlideUp, GlideSpeedNormal,
        GlideSpeedFast, RunSpeed, RunSpeedFast, JumpHeightG, JumpHeightGSlider, JumpHeightW, JumpHeightWSlider,
        SwimSurfaceButton, SwimSurfaceSlider, AirborneSpeedButton, AirborneSpeedSlider, JumpPeakButton, TyStateButton]
    for (i, frame) in enumerate(frames):
        if i == frame_num:
            frame.pack()
        else:
            frame.pack_forget()
    for button in buttons:
        if frame_num == 0:
            if button in [
                GiveAll_Button, RemoveAll_Button, Test, Give_Techno_Button, Give_Elemental_Button, Test2,
                TwoRang_switch, Dive_switch, swim_switch, Aqua_switch, Frosty_switch, Flame_switch, Zappy_switch,
                Kaboom_switch, Doomer_switch, Zoomer_switch, Infra_switch, Multi_switch, Chrono_switch, Mega_switch,
            ]:
                button.pack()
            else:
                button.pack_forget()
        elif frame_num == 1:
            if button in [
                Glide, GlideUp, GlideSpeedNormal, GlideSpeedFast, RunSpeed, RunSpeedFast, JumpHeightG,
                JumpHeightGSlider, JumpHeightW, JumpHeightWSlider, SwimSurfaceButton, SwimSurfaceSlider,
                AirborneSpeedButton, AirborneSpeedSlider, JumpPeakButton, TyStateButton
            ]:
                button.pack()
            else:
                button.pack_forget()


title_label = ctk.CTkLabel(frame_buttons, text="Ty1 Speedrun\nPractice\nMods", font=TyFont)
button1 = ctk.CTkButton(frame_buttons, text_color="Black", text="Rangs", font=TyFontS,
                        command=lambda: select_frame(0))
button2 = ctk.CTkButton(frame_buttons, text_color="Black", text="Movement", font=TyFontS,
                        command=lambda: select_frame(1))
button3 = ctk.CTkButton(frame_buttons, text_color="Black", text="Position", font=TyFontS,
                        command=lambda: select_frame(2))
button4 = ctk.CTkButton(frame_buttons, text_color="Black", text="TE/Cogs WIP", font=TyFontS,
                        command=lambda: select_frame(3))
button5 = ctk.CTkButton(frame_buttons, text_color="Black", text="FUN", font=TyFontS,
                        command=lambda: select_frame(4))
button6 = ctk.CTkButton(frame_buttons, text_color="Black", text="CheatCodes", font=TyFontS,
                        command=lambda: select_frame(5))

toggle_button = ctk.CTkButton(frame_buttons, text="Hide Me", command=toggle_window)
exit_button = ctk.CTkButton(frame_buttons, text="Close", command=quit)
label_empty = ctk.CTkLabel(frame_buttons, text="\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

title_label.pack()
button1.pack()
button2.pack()
button3.pack()
button4.pack()
button5.pack()
button6.pack()
label_empty.pack()
toggle_button.pack()
exit_button.pack(side="bottom", fill="x")

TyFont = ctk.CTkFont(family="SF Slapstick Comic", size=20)
GiveAll_Button = ctk.CTkButton(frame1, font=TyFont, hover=False, text="Give All ", fg_color="green", text_color="black",
                               command=lambda: Give_All(pm))
RemoveAll_Button = ctk.CTkButton(frame1, font=TyFont, hover=False, text="Remove All", fg_color="red",
                                 text_color="black",
                                 command=lambda: Remove_All(pm))
Give_Elemental_Button = ctk.CTkButton(frame1, font=TyFont, hover=False, text="Give Elemental", fg_color="orange",
                                      text_color="black",
                                      command=lambda: Give_Techno(pm))
Give_Techno_Button = ctk.CTkButton(frame1, font=TyFont, hover=False, text="Give Techno", fg_color="orange",
                                   text_color="black",
                                   command=lambda: Give_Elemental(pm))

TwoRang_switch = ctk.CTkButton(frame1, font=TyFont, hover=False, text="2nd Rang Off", fg_color="red",
                               text_color="black", command=lambda: toggle_2ndRang(pm, TwoRang_switch))

Dive_switch = ctk.CTkButton(frame1, font=TyFont, hover=False, text="Dive Off", fg_color="red",
                            text_color="black", command=lambda: toggle_dive(pm, Dive_switch))

swim_switch = ctk.CTkButton(frame1, font=TyFont, hover=False, text="Swim Off", fg_color="red",
                            text_color="black", command=lambda: toggle_swim(pm, swim_switch))

Aqua_switch = ctk.CTkButton(frame1, font=TyFont, hover=False, text="Aqua Off", fg_color="red",
                            text_color="black", command=lambda: toggle_aqua(pm, Aqua_switch))

Frosty_switch = ctk.CTkButton(frame1, font=TyFont, hover=False, text="Frosty Off", fg_color="red",
                              text_color="black", command=lambda: toggle_frosty(pm, Frosty_switch))

Flame_switch = ctk.CTkButton(frame1, font=TyFont, hover=False, text="Flame Off", fg_color="red",
                             text_color="black", command=lambda: toggle_flame(pm, Flame_switch))

Zappy_switch = ctk.CTkButton(frame1, font=TyFont, hover=False, text="Zappy Off", fg_color="red",
                             text_color="black", command=lambda: toggle_zappy(pm, Zappy_switch))

Kaboom_switch = ctk.CTkButton(frame1, font=TyFont, hover=False, text="Kaboom Off", fg_color="red",
                              text_color="black", command=lambda: toggle_kaboom(pm, Kaboom_switch))

Doomer_switch = ctk.CTkButton(frame1, font=TyFont, hover=False, text="Doomer Off", fg_color="red",
                              text_color="black", command=lambda: toggle_doomer(pm, Doomer_switch))

Mega_switch = ctk.CTkButton(frame1, font=TyFont, hover=False, text="Mega Off", fg_color="red",
                            text_color="black", command=lambda: toggle_mega(pm, Mega_switch))

Zoomer_switch = ctk.CTkButton(frame1, font=TyFont, hover=False, text="Zoomer Off", fg_color="red",
                              text_color="black", command=lambda: toggle_zoomer(pm, Zoomer_switch))

Infra_switch = ctk.CTkButton(frame1, font=TyFont, hover=False, text="Infra Off", fg_color="red",
                             text_color="black", command=lambda: toggle_infra(pm, Infra_switch))

Multi_switch = ctk.CTkButton(frame1, font=TyFont, hover=False, text="Multi Off", fg_color="red",
                             text_color="black", command=lambda: toggle_multi(pm, Multi_switch))

Chrono_switch = ctk.CTkButton(frame1, font=TyFont, hover=False, text="Chrono Off", fg_color="red",
                              text_color="black", command=lambda: toggle_chrono(pm, Chrono_switch))

Test = ctk.CTkButton(frame1, width=10, height=2, text="                                              ",
                     fg_color=["gray92", "gray14"], hover=False, command=None)
Test2 = ctk.CTkButton(frame1, width=10, height=2, text="                                              ",
                      fg_color=["gray92", "gray14"], hover=False, command=None)

# Movement Buttons
Glide = ctk.CTkButton(frame2, font=TyFontS, width=155, text="Glide Up/Down Reset", fg_color="green",
                      text_color="black", command=lambda: [Glide1(), GlideUp.set(5.5)])

GlideUp = ctk.CTkSlider(frame2, hover=False,
                        command=lambda value: Glide2(value),
                        from_=20, to=-20, width=155)
GlideUp.set(5.5)

GlideSpeedNormal = ctk.CTkButton(frame2, font=TyFontS, width=155, text="Glide Speed Reset", fg_color="green",
                                 text_color="black", command=lambda: [GlideSpeed1(), GlideSpeedFast.set(7.0)])

GlideSpeedFast = ctk.CTkSlider(frame2, hover=False,
                               command=lambda value: GlideSpeed2(value),
                               from_=-100, to=100, width=155)
GlideSpeedFast.set(7.0)

RunSpeed = ctk.CTkButton(frame2, font=TyFontS, width=155, text="Run Speed Reset", fg_color="green",
                         text_color="black", command=lambda: [RunSpeed1(), RunSpeedFast.set(10.0)])

RunSpeedFast = ctk.CTkSlider(frame2, hover=False,
                             command=lambda value: RunSpeed2(value),
                             from_=0, to=100, width=155)
RunSpeedFast.set(10.0)

JumpHeightG = ctk.CTkButton(frame2, font=TyFontS, width=155, text="Ground Jump Reset", fg_color="green",
                            text_color="black",
                            command=lambda: [JumpHeightG1(), JumpHeightGSlider.set(18.57417488)])

JumpHeightGSlider = ctk.CTkSlider(frame2, hover=False, command=lambda value: JumpHeightG2(value),
                                  from_=0, to=100, width=155)
JumpHeightGSlider.set(18.57417488)

JumpHeightW = ctk.CTkButton(frame2, font=TyFontS, width=155, text="Water Jump Reset", fg_color="green",
                            text_color="black",
                            command=lambda: [JumpHeightW1(), JumpHeightWSlider.set(10.67707825)])

JumpHeightWSlider = ctk.CTkSlider(frame2, hover=False, command=lambda value: JumpHeightW2(value),
                                  from_=0, to=50, width=155)
JumpHeightWSlider.set(10.67707825)

SwimSurfaceButton = ctk.CTkButton(frame2, font=TyFontS, width=155, text="Surface Speed Reset", fg_color="green",
                                  text_color="black",
                                  command=lambda: [SwimSurface1(), SwimSurfaceSlider.set(6.0)])

SwimSurfaceSlider = ctk.CTkSlider(frame2, hover=False, command=lambda value: SwimSurface2(value),
                                  from_=0, to=40, width=155)
SwimSurfaceSlider.set(6.0)

AirborneSpeedButton = ctk.CTkButton(frame2, font=TyFontS, width=155, text=" Airborne Speed Reset", fg_color="green",
                                    text_color="black",
                                    command=lambda: [AirborneSpeed1(), AirborneSpeedSlider.set(10.0)])

AirborneSpeedSlider = ctk.CTkSlider(frame2, hover=False, command=lambda value: AirborneSpeed2(value),
                                    from_=0, to=40, width=155)
AirborneSpeedSlider.set(10.0)

jump_peak_running = False
# CheatCodes

SelectLevel = ctk.CTkLabel(frame6, font=TyFontS,
                           text="-Level Select-\nL R L R ACTION ACTION BITE BITE ACTION BITE BITE ACTION",
                           text_color="black")
SelectLevel.pack()
Elemental = ctk.CTkLabel(frame6, font=TyFontS,
                         text="-Elemental Rangs-\nL R L R  ACTION ACTION THROW THROW ACTION THROW",
                         text_color="black")
Elemental.pack()
Techno = ctk.CTkLabel(frame6, font=TyFontS, text="-Techno Rangs-\nL R L R ACTION ACTION ACTION THROW ACTION THROW",
                      text_color="black")
Techno.pack()
Collect = ctk.CTkLabel(frame6, font=TyFontS,
                       text="-Show Collectables-\nL R L R ACTION ACTION BITE THROW THROW BITE LOCKON LOCKON",
                       text_color="black")
Collect.pack()


def repeat_jump_peak():
    if jump_peak_running:
        JumpPeak1()
        JumpPeakButton.configure(fg_color="green", text="Fall Damage Disabled")
        root.after(100, repeat_jump_peak)


def toggle_jump_peak_running():
    global jump_peak_running
    jump_peak_running = not jump_peak_running
    if jump_peak_running:
        JumpPeak1()
        JumpPeakButton.configure(fg_color="green", text="Fall Damage Disabled")
        root.after(100, repeat_jump_peak)
    else:
        JumpPeakButton.configure(fg_color="red", text="Fall Damage Enabled")


JumpPeakButton = ctk.CTkButton(frame2, font=TyFontS, width=155, fg_color="blue", text="Toggle Fall Damage",
                               text_color="black", command=toggle_jump_peak_running)

TyStateButton = ctk.CTkButton(frame2, font=TyFontS, width=155, text="Give Groundswim", fg_color="green",
                              text_color="black", command=ToggleTyState)

# Frame3
buttons = {
    "Rainbow Cliffs": ["Spawn Z1", "Hub1", "Hub 2", "Hub 3", "Fence Skip", "Julius", "Gate Skip", "Behind Gate"],
    "Two Up": ["Spawn A1", "Bilby1", "Two Up Swim", "Spyeggs", "Bite Slide", "Two Up Skip", "Buttons", "2nd Rang",
               "EndA1", "PortalA1"],
    "Walk in the Park": ["Spawn A2", "Buzchy Swim", "Walk Skip", "Ken", "Turkey", "EndA2", "PortalA2"],
    "Ship Rex": ["Spawn A3", "Lost Kids Mission", "Ship Clip", "Nest Swim", "Coconuts", "Bilby Bite", "Spire Gate",
                 "Spire Swim", "Top Spire"],
    "Bull's Pen": ["Pillar 1", "Pillar 2", "Pillar 3", "Pillar 4", "Pillar 5"],
    "Bridge on the River Ty": ["Spawn B1", ],
}


def optionmenu_callback(choice):
    for widget in frame3.winfo_children():
        if isinstance(widget, ctk.CTkButton):
            widget.pack_forget()

    if choice in buttons:
        for i, text in enumerate(buttons[choice]):
            button_name = "btn_" + text
            command = None
            if text == "Spawn Z1":
                command = Spawn_Z1
            elif text == "Hub1":
                command = Hub1
            elif text == "Hub 2":
                command = Hub2
            elif text == "Hub 3":
                command = Hub3
            elif text == "Fence Skip":
                command = Fence_Skip
            elif text == "Julius":
                command = Julius
            elif text == "Gate Skip":
                command = Gate_Skip
            elif text == "Behind Gate":
                command = Behind_Gate
            elif text == "Spawn A1":
                command = Spawn_A1
            elif text == "Bilby1":
                command = Bilby1
            elif text == "Two Up Swim":
                command = Two_Up_Swim
            elif text == "Spyeggs":
                command = Spyeggs
            elif text == "Bite Slide":
                command = Bite_Slide
            elif text == "Two Up Skip":
                command = Two_Up_Skip
            elif text == "Buttons":
                command = Two_Up_Buttons
            elif text == "2nd Rang":
                command = Second_Rang
            elif text == "EndA1":
                command = End
            elif text == "PortalA1":
                command = Two_Up_Portal
            elif text == "Spawn A2":
                command = Spawn_A2
            elif text == "Buzchy Swim":
                command = Buzchy_Swim
            elif text == "Walk Skip":
                command = Walk_Skip
            elif text == "Ken":
                command = Ken
            elif text == "Turkey":
                command = Turkey
            elif text == "EndA2":
                command = EndA2
            elif text == "PortalA2":
                command = PortalA2
            elif text == "Spawn A3":
                command = Spawn_A3
            elif text == "Lost Kids Mission":
                command = Lost_Kids_Mission
            elif text == "Ship Clip":
                command = Ship
            elif text == "Nest Swim":
                command = Nest_Swim
            elif text == "Coconuts":
                command = Coconuts
            elif text == "Bilby Bite":
                command = BilbyBite
            elif text == "Spire Swim":
                command = Spire_Swim
            elif text == "Spire Gate":
                command = Spire_Gate
            elif text == "Top Spire":
                command = Top_Spire
            elif text == "Pillar 1":
                command = Pillar1
            elif text == "Pillar 2":
                command = Pillar2
            elif text == "Pillar 3":
                command = Pillar3
            elif text == "Pillar 4":
                command = Pillar4
            elif text == "Pillar 5":
                command = Pillar5
            elif text == "Spawn B1":
                command = Bridge_Spawn

            if command:
                btn = ctk.CTkButton(frame3, text=text, command=command)
                btn.pack()


# Define the options for the combobox
options = ["Select One", "Rainbow Cliffs", "Two Up", "Walk in the Park", "Ship Rex", "Bull's Pen",
           "Bridge on the River Ty", "Snow Worries", "Outback Safari", "Crikey", "Lyre Lyre", "Black Stump",
           "Rex marks", "Fluffy", "Cass Pass", "Cass Crest", "Final Battle"]

# Create the combobox
combobox = ctk.CTkOptionMenu(frame3, values=options, command=optionmenu_callback)
combobox.pack()

root.mainloop()
