# -*- coding: utf-8 -*-
#  _    _   _ ___ ____
# | |  | | | |_ _/ ___|
# | |  | | | || |\___ \
# | |__| |_| || | ___) |
# |_____\___/|___|____/

from typing import List  # noqa: F401
from libqtile import bar, layout, widget, hook, qtile
from libqtile.config import Click, Drag, Group, Key, Match, Screen, Match
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
import os
import subprocess

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
        "clock":"🕓︁",
        "wifi":"",
        "arrow":"",
        "keyboard":"",
        "python":"",
        "audio":'',
        "battery":"",
        }

##############################################
##########  Atajos de teclados ###############
##############################################
#STARTKEYB
keys = [
    # Moverse entre ventanas
    Key([mod], "h", lazy.layout.left(), desc="Mover el foco de la ventana a la izquierda"),
    Key([mod], "l", lazy.layout.right(), desc="Mover el foco de la ventana a la derecha"),
    Key([mod], "j", lazy.layout.down(), desc="Mover el foco de la vanetana abajo"),
    Key([mod], "k", lazy.layout.up(), desc="Mover foco de la ventana arriba"),
    Key([mod], "space", lazy.layout.next(), desc="Mover el foco de la ventana hacia otra ventana"),

    # Mover las ventanas en un mismo espacio de trabajo
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Mover ventana a la izquierda"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Mover ventana a la derecha"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Mover ventana hacia abajo"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Mover ventana hacia arriba"),

    # Cambiar el tamano de las ventanas
    Key([mod, "control"], "h", lazy.layout.grow(), desc="Aumentar tamaño de la ventana seleccionada"),
    Key([mod, "control"], "j", lazy.layout.shrink(), desc="Disminuir tamaño de la ventana selecionada"),
    Key([mod, "control"], "k", lazy.layout.normalize(), desc="Normalizar tamaños de las ventanas"),
    Key([mod, "control"], "l", lazy.layout.maximize(), desc="Maximizar o minimizar al máximo el tamaño de la ventana seleccionada"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(), desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Lanzar un terminal"),

    # Cambiar entre diferentes esquemas de ventanas
    Key([mod], "Tab", lazy.next_layout(), desc="Cambiar entre layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Eliminar ventana enfocada"),

    # Controles de qtile
    Key([mod, "control"], "r", lazy.restart(), desc="Reiniciar Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Apagar Qtile"),
    #Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key([mod], 'x', lazy.spawn('arcolinux-logout'), desc="Cerrar sesion"),
    # Lanzador de Rofi
    Key([mod], 'r', lazy.spawn('rofi -show drun'), desc="Lanzar Rofi"),
    Key([mod], 'w', lazy.spawn('rofi -show window'), desc="Cambiar entre ventanas con Rofi"),

    # Control de audio y brillo
    Key([mod], 'F2', lazy.spawn('amixer -D pulse sset Master 5%-'), desc="Disminuir 5% volumen"),
    Key([mod], 'F3', lazy.spawn('amixer -D pulse sset Master 5%+'), desc="Aumentar 5% el volumen"),
    Key([mod], 'F4', lazy.spawn('xrandr --output eDP --brightness 0.4'), desc="Poner el brillo de la pantalla al 40%"),
    Key([mod], 'F5', lazy.spawn('xrandr --output eDP --brightness 0.9'), desc="Poner el brillo de la pantalla al 90%"),
    Key([mod],'p', lazy.spawn('flameshot gui'), desc="Realizar captura de pantalla con fireshot"),

    #Lanzar Navegador
    Key([mod], 'f', lazy.spawn('firejail firefox'), desc="Iniciar firefox en una sandbox"),
    Key([mod], 'c', lazy.spawn('firejail google-chrome-stable'), desc="Iniciar chrome en una sandbox"),
    Key([mod], 'b', lazy.spawn('firejail brave'), desc="Iniciar firefox en una sandbox"),
]
#ENDKEYB


#####################################################
############# Configuracion de grupos ###############
#####################################################

__groups = {
        1 : Group(name=""),                                                                # Grupo para los terminales
        2 : Group(name="", matches=[Match(wm_class=["firefox","brave","google-chrome"])]),                 # Grupo para los navegadores
        3 : Group(name=""),
        4 : Group(name="", matches=[Match(wm_class=["Thunar"])]),                          # Grupo para File Explorer
        5 : Group(name="", matches=[Match(wm_class=["zoom"])]),                            # Grupo para Zoom
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
        margin=4,
        change_size=5,
        ),
]

widget_defaults = dict(
    font='Fira Sans Medium',
    fontsize=16,
    padding=5,
)
extension_defaults = widget_defaults.copy()

#####################################################
########## Funciones para la barra ##################
#####################################################

def logout():
    qtile.cmd_spawn('arcolinux-logout')

def qtile_conf():
    qtile.cmd_spawn('alacritty -e vim /home/luiyvane/.config/qtile/config.py')

def wifi():
    qtile.cmd_spawn('alacritty -e nmtui')

#####################################################
##########     Barra de inicio     ##################
#####################################################

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.TextBox(text=icons["python"], background=color[0], foreground=color[2], fontsize=22, mouse_callbacks = {"Button1": qtile_conf}),
                widget.CurrentLayout( foreground=color[3], fontshadow=color[1]),
                widget.GroupBox( borderwidth = 2, highlight_method = "line", highlight_color=color[0], rounded=False, active=color[2], inactive=color[3], background=color[0], fontsize=23),
                widget.TextBox(text="      "),
                widget.WindowName(background=color[0], foreground=color[2]),
                widget.TextBox(text=icons["arrow"], background=color[0], foreground=color[2], padding=1, fontsize=102, width=38),
                widget.Net(background=color[2],interface="wlp1s0", format="{down}↓↑{up}", foreground=color[3]),
                widget.TextBox(text=icons["wifi"],background=color[2], fontsize=35, mouse_callbacks={"Button1": wifi}),
                widget.TextBox(text=icons["arrow"], background=color[2], foreground=color[3], padding=1, fontsize=102, width=38),
                widget.TextBox(text=icons["battery"],background=color[3], foreground=color[2], fontsize=27),
                widget.Battery(background=color[3], format="{percent:2.0%}",foreground=color[2]),
                widget.TextBox(text=icons["arrow"], background=color[3], foreground=color[2], padding=1, fontsize=102, width=38),
                widget.TextBox(text=icons["clock"],background=color[2], fontsize=18),
                widget.Clock(background=color[2],foreground=color[3],format='%I:%M'),
                widget.TextBox(text=icons["arrow"], background=color[2], foreground=color[3], padding=1, fontsize=102, width=38),
                widget.TextBox(text=icons["keyboard"], background=color[3], foreground=color[2], fontsize=25),
                widget.KeyboardLayout(background=color[3], foreground=color[2],configured_keyboards=["us","es"]),
                widget.TextBox(text=icons["arrow"], background=color[3], foreground=color[2], padding=1, fontsize=102, width=38),
                widget.TextBox(text="Vol:", background=color[2], foreground=color[3]),
                widget.Volume(background=color[2],foreground=color[3]),
                widget.TextBox(text="\u23FB", fontsize=18, background=color[2],mouse_callbacks={"Button1":logout}),
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

#############################################################################
##############              Ventanas Flotantes              #################
#############################################################################

floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
    Match(wm_class='yad'), #yad
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

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/scriptsq/autostart.sh'])

'''
@hook.subscribe.startup
def starting():
    ejecutar = os.path.expanduser('~/.config/qtile/scriptsq/')
    subprocess.call([home])

'''
