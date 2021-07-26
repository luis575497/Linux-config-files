# -*- coding: utf-8 -*-
#  _    _   _ ___ ____
# | |  | | | |_ _/ ___|
# | |  | | | || |\___ \
# | |__| |_| || | ___) |
# |_____\___/|___|____/

from typing import List  # noqa: F401
from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen, Match
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
import os

mod = "mod4"
terminal = guess_terminal()

# Esquema de Colores

def colores():
    return ["#222831",
            "#393E46",
            "#00ADB5",
            "#EEEEEE",
            "#FB3640",
            ]

color=colores()

# Iconos para utilizar con la fuente Awesome
icons = {
        "clock":"",
        "wifi":"",
        "arrow":"",
        "keyboard":"",
        "python":"",
        "audio":'',
        "battery":"",
        }

# Atajos de teclados

keys = [
    # Moverse entre ventanas
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),

    # Mover las ventanas en un mismo espacio de trabajo
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Cambiar el tamano de las ventanas
    Key([mod, "control"], "h", lazy.layout.grow(),
        desc="Grow window to the left"),
    Key([mod, "control"], "j", lazy.layout.shrink(),
        desc="Grow window to the right"),
    Key([mod, "control"], "k", lazy.layout.normalize(),
        desc="Grow window down"),
    Key([mod, "control"], "l", lazy.layout.maximize(), desc="Grow window up"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Cambiar entre diferentes esquemas de ventanas
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),

    # Controles de qtile
    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"),

    # Lanzador de Rofi
    Key([mod], 'r', lazy.spawn('rofi -show run')),
    Key([mod], 'w', lazy.spawn('rofi -show window')),

    # Control de audio y brillo
    Key([mod], 'F2', lazy.spawn('amixer -D pulse sset Master 5%-')),
    Key([mod], 'F3', lazy.spawn('amixer -D pulse sset Master 5%+')),
    Key([mod], 'F4', lazy.spawn('xrandr --output eDP --brightness 0.4')),
    Key([mod], 'F5', lazy.spawn('xrandr --output eDP --brightness 0.9')),

    #Lanzar Navegador
    Key([mod], 'f', lazy.spawn('firejail firefox'))
]

#groups = [Group(i) for i in '12345789']

__groups = {
        1 : Group(name=""),                                                                # Grupo para los terminales
        2 : Group(name="", matches=[Match(wm_class=["firefox","brave"])]),                 # Grupo para los navegadores
        3 : Group(name=""),
        4 : Group(name="", matches=[Match(wm_class=["Thunar"])]),                          # Grupo para File Explorer
        5 : Group(name="", matches=[Match(wm_class=["zoom"])]),                            # Grupo para Zoom
        }

groups = [__groups[i] for i in __groups]

def get_group_key(name):
    return [k for k,g in __groups.items() if g.name == name][0]

for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], str(get_group_key(i.name)), lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"], str(get_group_key(i.name)), lazy.window.togroup(i.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(i.name)),
        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
        #     desc="move focused window to group {}".format(i.name)),
    ])

layouts = [
    layout.MonadTall(
        border_width=3,
        border_focus=color[4],
        border_normal=color[1],
        single_border_width=0,
        margin=2,
        change_size=5,
        ),
]

widget_defaults = dict(
    font='Fira Sans Medium',
    fontsize=16,
    padding=5,
)
extension_defaults = widget_defaults.copy()


screens = [
    Screen(
        top=bar.Bar(
            [
                widget.TextBox(text=icons["python"], background=color[0], foreground=color[2], fontsize=22),
                widget.CurrentLayout( foreground=color[3], fontshadow=color[1]),
                widget.GroupBox( borderwidth = 2, highlight_method = "line", highlight_color=color[0], rounded=False, active=color[2], inactive=color[3], background=color[0], fontsize=23),
                widget.TextBox(text="      "),
                widget.WindowName(background=color[0], foreground=color[2]),
                widget.TextBox(text=icons["arrow"], background=color[0], foreground=color[2], padding=1, fontsize=102, width=38),
                widget.Net(background=color[2],interface="wlp1s0", format="{down}↓↑{up}", foreground=color[3]),
                widget.TextBox(text=icons["wifi"],background=color[2], fontsize=35),
                widget.TextBox(text=icons["arrow"], background=color[2], foreground=color[3], padding=1, fontsize=102, width=38),
                widget.TextBox(text=icons["battery"],background=color[3], foreground=color[2], fontsize=27),
                widget.Battery(background=color[3], format="{percent:2.0%}",foreground=color[2]),
                widget.TextBox(text=icons["arrow"], background=color[3], foreground=color[2], padding=1, fontsize=102, width=38),
                widget.TextBox(text=icons["clock"],background=color[2], fontsize=30),
                widget.Clock(background=color[2],foreground=color[3],format='%I:%M'),
                widget.TextBox(text=icons["arrow"], background=color[2], foreground=color[3], padding=1, fontsize=102, width=38),
                widget.TextBox(text=icons["keyboard"], background=color[3], foreground=color[2], fontsize=25),
                widget.KeyboardLayout(background=color[3], foreground=color[2],configured_keyboards=["us","es"]),
                widget.TextBox(text=icons["arrow"], background=color[3], foreground=color[2], padding=1, fontsize=102, width=38),
                widget.TextBox(text="Vol:", background=color[2], foreground=color[3]),
                widget.Volume(background=color[2],foreground=color[3]),
                widget.QuickExit(default_text="\u23FB", fontsize=18, countdown_format="{}", countdown_start=10,background=color[2]),
                widget.Moc(background=color[2],play_color=color[3], max_chars=20),
            ],
            25,
            background=color[0],
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.


wmname = "LG3D"

# Ejecutar programas de manera inicial

autostart = [
    "python ~/scripts/background_change.py &", # Script Creado para cambiar el fondo de pantalla de manera automatica
    "picom &",
        ]

for commands in autostart:
    os.system(commands)
