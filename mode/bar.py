# from libqtile import widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.bar import Bar
from qtile_extras.widget.decorations import RectDecoration, PowerLineDecoration
from qtile_extras import widget
from mode.color import nord_fox, catppuccin

decoration_group = {
    "decorations": [
        RectDecoration(colour=nord_fox["cyan"], radius=8, filled=True, padding_y=4, padding_x=10, group=True)
    ],
    "padding": 12
}

bar = Bar(
    [
        # widget.CurrentLayout(),
        widget.TextBox(
        ),
        widget.GroupBox(
            fontsize=15,
            borderwidth=3,
            highlight_method='line',
            active='#CAA9E0',
            # block_highlight_text_color="#91B1F0",
            highlight_color='#4B427E',
            inactive='#282738',
            # foreground='#4B427E',
            # background='#353446',
            this_current_screen_border='#353446',
            this_screen_border='#353446',
            other_current_screen_border='#353446',
            other_screen_border='#353446',
            urgent_border='#353446',
            rounded=True,
            disable_drag=True,
            **decoration_group,
        ),
        widget.Prompt(),
        widget.WindowName(),
        widget.Chord(
            chords_colors={
                "launch": ("#ff0000", "#ffffff"),
            },
            name_transform=lambda name: name.upper(),
        ),
        # widget.TextBox("default config", name="default"),
        # widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#d75f5f"),
        # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
        # widget.StatusNotifier(),
        widget.Systray(),
        widget.Memory(
            format='󰍛{MemUsed: .0f}{mm}/{MemTotal: .0f}{mm}',
            background=nord_fox['black'],
            foreground=nord_fox['cyan']
        ),
        widget.Clock(format="%Y-%m-%d %a %I:%M %p"),
        widget.QuickExit(),
    ],
    22,
    background="#00000000",
    # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
    # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
)


def get_widgets(primary=False):
    widgets = [
        widget.Spacer(
            length=3,
            background="#00000000",
        ),
        widget.TextBox(
            text="",
            padding=0,
            fontsize=30,
            foreground=catppuccin["mauve"],
            background="#00000000",
        ),
        widget.GroupBox(
            highlight_method="line",
            background=catppuccin["mauve"],
            highlight_color=[catppuccin["mauve"], catppuccin["mauve"]],
            inactive=catppuccin["black"],
        ),
        widget.TextBox(
            text="",
            padding=0,
            fontsize=30,
            foreground=catppuccin["mauve"],
            background="#00000000",
        ),
        widget.WindowName(
            fontsize=12,
            foreground=catppuccin["white"]
        ),
        widget.TextBox(
            text="",
            padding=0,
            fontsize=30,
            foreground=catppuccin["sky"],
            background="#00000000",
        ),
        widget.Volume(
            fmt="墳 {}",
            mute_command="amixer -D pulse set Master toggle",
            foreground=catppuccin["black"],
            background=catppuccin["sky"],
        ),
        widget.TextBox(
            text="",
            padding=0,
            fontsize=30,
            foreground=catppuccin["sky"],
            background="#00000000",
        ),
        widget.TextBox(
            text="",
            padding=0,
            fontsize=30,
            foreground=catppuccin["peach"],
            background="#00000000",
        ),
        widget.CPU(
            format=" {load_percent:04}%",
            foreground=catppuccin["black"],
            background=catppuccin["peach"],
        ),
        widget.TextBox(
            text="",
            padding=0,
            fontsize=30,
            foreground=catppuccin["peach"],
            background="#00000000",
        ),
        widget.TextBox(
            text="",
            padding=0,
            fontsize=30,
            foreground=catppuccin["maroon"],
            background="#00000000",
        ),
        widget.Clock(
            format=" %I:%M %p",
            foreground=catppuccin["black"],
            background=catppuccin["maroon"],
        ),
        widget.TextBox(
            text="",
            padding=0,
            fontsize=30,
            foreground=catppuccin["maroon"],
            background="#00000000",
        ),
    ]
    if primary:
        widgets.insert(10, widget.Systray())
    return widgets
