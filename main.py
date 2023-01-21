import os, winshell
from win32com.client import Dispatch
print(os.environ["PATH"])


apps = {
    "CrossOver": r"d:\Program Files\CrossOver\CrossOver.exe",
    "Dungeons": r"d:\Program Files\daominhha.com.minecraft.dungeons.v1.12.1.0\Dungeons.exe",
    "PotPlayerMini": r"d:\Program Files\DAUM\PotPlayer\PotPlayerMini64.exe",
    "DroidCamApp": r"D:\Program Files\DroidCam\DroidCamApp.exe",
    "fdm": r"D:\Program Files\Free Download Manager",
    "ImageGlass": r"d:\Program Files\ImageGlass\ImageGlass.exe",
    "InstantEyedropper": r"d:\Program Files\InstantEyedropper\InstantEyedropper.exe",
    "Obs": r"d:\Program Files\obs-studio\bin\64bit\obs64.exe",
    "Osu": r"d:\Program Files\osu!\osu!.exe",
    "paintdotnet":r"d:\Program Files\paint.net\paintdotnet.exe",
    "UniKeyNT": r"d:\Program Files\unikey\UniKeyNT.exe",
    "launcher": r"d:\Program Files\Wallpaper.Engine\launcher.exe",
    
}



def add_python_path():
    list_path = os.environ["PATH"].split(';')
    python_path = filter(lambda x: x.lower().count("python"), list_path)
    if len(list(python_path)) > 0:
        return

    os.environ["PATH"] = os.environ["PATH"] + r"D:\Program_code\Python37;"


def setup_shortCut():
    for i in apps.items():
        with winshell.shortcut(winshell.folder("APPDATA") + fr"\Microsoft\Windows\Start Menu\Programs\{i[0]}.lnk") as link:
            link.path = i[1]
            link.icon_location = (i[1] , 0)
    
            
def install_app():
    pass

if __name__ == "__main__":
    setup_shortCut()
