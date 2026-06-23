#Requires AutoHotkey v2.0
#SingleInstance Force
;#NoTrayIcon
#MaxThreads 5

#Include classes\class.Config.ahk
#Include classes\class.Main.ahk
#Include classes\class.Spheres.ahk
#Include classes\class.Spells.ahk
#Include classes\class.Multicast.ahk

#HotIf WinActive("ahk_exe dota2.exe")

~Space::sc2B
sc2:: Spells.use "ice_wall"
sc3:: Spells.use "tornado"
sc4:: Spells.use "alacrity"
sc5:: Spells.use "forge_spirit"
sc6:: Multicast.use_3()
sc10:: Spells.use "cold_snap"
sc11:: Spells.use "emp"
sc12:: Spells.use "sun_strike"
sc13:: Spells.use "deafening_blast"
sc14:: Spells.use "chaos_meteor"
sc32:: Multicast.use_1()

sc2C:: Spheres.prepare("quas")
sc2D:: Spheres.prepare("wex")
sc2E:: Spheres.prepare("exort")

sc27:: Multicast.use_4()
XButton2:: Multicast.use_3()
XButton1:: Multicast.use_12334q5345q34()

#HotIf
