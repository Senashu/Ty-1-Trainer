import customtkinter as ctk
import keyboard
from TyAttributes import *
from Movement import *
from Position import *
from Fun import *

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
    elif event.name == '3' and event.event_type == keyboard.KEY_DOWN and keyboard.is_pressed('ctrl'):
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
                AirborneSpeedButton, AirborneSpeedSlider, JumpPeakButton, TyStateButton,
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
button4 = ctk.CTkButton(frame_buttons, text_color="Black", text="FUN", font=TyFontS,
                        command=lambda: select_frame(3))
button5 = ctk.CTkButton(frame_buttons, text_color="Black", text="CheatCodes", font=TyFontS,
                        command=lambda: select_frame(4))

toggle_button = ctk.CTkButton(frame_buttons, text="Hide Me", text_color="Black", font=TyFontS, command=toggle_window)
exit_button = ctk.CTkButton(frame_buttons, text="Close [X]", text_color="Black", font=TyFontS, command=quit)
label_empty = ctk.CTkLabel(frame_buttons, text="\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

title_label.pack()
button1.pack()
button2.pack()
button3.pack()
button4.pack()
button5.pack()
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

SelectLevel = ctk.CTkLabel(frame5, font=TyFontS,
                           text="-Level Select-\nL R L R ACTION ACTION BITE BITE ACTION BITE BITE ACTION",
                           text_color="black")
SelectLevel.pack()
Elemental = ctk.CTkLabel(frame5, font=TyFontS,
                         text="-Elemental Rangs-\nL R L R  ACTION ACTION THROW THROW ACTION THROW",
                         text_color="black")
Elemental.pack()
Techno = ctk.CTkLabel(frame5, font=TyFontS, text="-Techno Rangs-\nL R L R ACTION ACTION ACTION THROW ACTION THROW",
                      text_color="black")
Techno.pack()
Collect = ctk.CTkLabel(frame5, font=TyFontS,
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
    "1. Rainbow Cliffs": ["Spawn Z1", "Hub1", "Hub 2", "Hub 3", "Fence Skip", "Fence Skip Reverse", "Julius",
                          "Gate Skip", "Behind Gate"],
    "2. Two Up": ["Spawn A1", "Bilby1", "Two Up Swim", "Spyeggs", "Bite Slide", "Two Up Skip", "Buttons", "2nd Rang",
                  "EndA1", "PortalA1"],
    "3. Walk": ["Spawn A2", "Buzchy Swim", "Walk Skip", "Ken", "TurkeyA2", "EndA2", "PortalA2"],
    "4. Ship Rex": ["Spawn A3", "Lost Kids Mission", "Ship Clip", "Nest Swim", "Coconuts", "Bilby Bite", "Spire Gate",
                    "Spire Swim", "Top Spire"],
    "5. Bull's Pen": ["Pillar 1", "Pillar 2", "Pillar 3", "Pillar 4", "Pillar 5"],
    "6. Bridge": ["Spawn B1", "BridgeSwim", "Flick/Dennis", "Rex Mission", "Neddy", "Turkey",
                  "Old BridgeSwim", "Old BridgeSwim GS"],
    "7. Snow Worries": ["Spawn B2", "Kid6", "IceBlock", "Yabby", "LawnSwim", "Icicles", "Mountain", "MillSkip",
                        "MillFlick"],
    "8. Outback Safari": ["Empty"],
    "9. Crikey": ["WIP"],
    "10. Lyre Lyre": ["WIP", "Option1", "Option2", "Option3", "Option4", "Option5", "Option6", "Option7", "Option8",
                      "Option9"],
    "11. Black Stump": ["WIP", "Option1", "Option2", "Option3", "Option4", "Option5", "Option6", "Option7", "Option8",
                        "Option9"],
    "12. Rex Marks": ["WIP", "Option1", "Option2", "Option3", "Option4", "Option5", "Option6", "Option7", "Option8",
                      "Option9"],
    "13. Fluffy": ["Empty"],
    "14. Cass Pass": ["Spawn E1", "Pass Jump", "Pass Tree", "Pass Swim", "Portal E1"],
    "15. Cass Crest": ["Spawn D2", "Start Shadow", "Button1 D2", "Button2 D2", "Button3 D2", "End D2"],
    "16. Final Battle": ["DoomClip", "Option2", "Option3", "Option4", "Option5"],
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
            elif text == "Fence Skip Reverse":
                command = Reverse_Fence_Skip
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
            elif text == "TurkeyA2":
                command = TurkeyA2
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
            elif text == "BridgeSwim":
                command = BridgeSwim
            elif text == "Flick/Dennis":
                command = Flick_Dennis
            elif text == "Rex Mission":
                command = RexMission
            elif text == "Neddy":
                command = Neddy
            elif text == "Turkey":
                command = Turkey
            elif text == "Old BridgeSwim":
                command = Old_BridgeSwim
            elif text == "Old BridgeSwim GS":
                command = Old_Swim
            elif text == "Spawn B2":
                command = Spawn_B2
            elif text == "Kid6":
                command = Kid6
            elif text == "IceBlock":
                command = IceBlock
            elif text == "Yabby":
                command = Yabby
            elif text == "LawnSwim":
                command = LawnSwim
            elif text == "Icicles":
                command = Icicles
            elif text == "Mountain":
                command = Mountain
            elif text == "MillSkip":
                command = MillSkip
            elif text == "MillFlick":
                command = MillFlick
            elif text == "Empty":
                command = Outback
            elif text == "WIP":
                command = WIP
            elif text == "Spawn E1":
                command = Spawn_E1
            elif text == "Pass Jump":
                command = OOB_Jump
            elif text == "Pass Tree":
                command = On_Tree
            elif text == "Pass Swim":
                command = Pass_Swim
            elif text == "Portal E1":
                command = Portal_E1
            elif text == "Portal D2":
                command = Spawn_D2
            elif text == "Start Shadow":
                command = EnableBoss
            elif text == "Button1 D2":
                command = D2_Button1
            elif text == "Button2 D2":
                command = D2_Button2
            elif text == "Button3 D2":
                command = D2_Button3
            elif text == "End D2":
                command = D2_End
            elif text == "DoomClip":
                command = Doom_Clip
            if command:
                btn = ctk.CTkButton(frame3, text=text, command=command)
                btn.pack()


HealthButton_running = False


def repeat_Health():
    if HealthButton_running:
        Health()
        HealthButton.configure(fg_color="green", text="Freeze Health")
        root.after(100, repeat_Health)


def toggle_HealthButton_running():
    global HealthButton_running
    HealthButton_running = not HealthButton_running
    if HealthButton_running:
        Health()
        HealthButton.configure(fg_color="green", text="Freeze Health")
        root.after(100, repeat_Health)
    else:
        HealthButton.configure(fg_color="red", text="Freeze Health Disabled")


HealthButton = ctk.CTkButton(frame4, font=TyFontS, width=155, fg_color="blue", text="Toggle Health",
                             text_color="black", command=toggle_HealthButton_running)
HealthButton.pack()

# Fun

HealthWaterButton_running = False


def repeat_HealthWater():
    if HealthWaterButton_running:
        HealthWater()
        HealthWaterButton.configure(fg_color="green", text="Freeze Health Water")
        root.after(100, repeat_HealthWater)


def toggle_HealthWaterButton_running():
    global HealthWaterButton_running
    HealthWaterButton_running = not HealthWaterButton_running
    if HealthWaterButton_running:
        HealthWater()
        HealthWaterButton.configure(fg_color="green", text="Freeze Health Water")
        root.after(100, repeat_HealthWater)
    else:
        HealthWaterButton.configure(fg_color="red", text="Freeze Health Water Disabled")


HealthWaterButton = ctk.CTkButton(frame4, font=TyFontS, width=155, fg_color="blue", text="Toggle Health Water",
                                  text_color="black", command=toggle_HealthWaterButton_running)
HealthWaterButton.pack()

SuperBiteButton = ctk.CTkButton(frame4, font=TyFontS, width=155, text="Give Super Bite", fg_color="green",
                                text_color="black", command=SuperBite)
SuperBiteButton.pack()

# Define the options for the combobox
options = ["Select One", "1. Rainbow Cliffs", "2. Two Up", "3. Walk", "4. Ship Rex", "5. Bull's Pen",
           "6. Bridge", "7. Snow Worries", "8. Outback Safari", "9. Crikey", "10. Lyre Lyre", "11. Black Stump",
           "12. Rex Marks", "13. Fluffy", "14. Cass Pass", "15. Cass Crest", "16. Final Battle"]

# Create the combobox
combobox = ctk.CTkOptionMenu(frame3, values=options, command=optionmenu_callback)
combobox.pack()

root.mainloop()
