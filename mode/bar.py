from libqtile import widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.bar import Bar
from mode.color import nord_fox, catppuccin

bar = Bar(
    [
        widget.Spacer(
            length=3,
            background="#00000000",
        ),
        # widget.CurrentLayout(),
        widget.TextBox(
            text="󱎕",
            fontsize=25,
            foreground=catppuccin["blue"],
            background="#00000000",
        ),
        widget.GroupBox(
            disable_drag=True,
            active=nord_fox['magenta'],
            inactive=nord_fox['black'],
            highlight_method='line',
            block_highlight_text_color=nord_fox['fg_gutter'],
            borderwidth=0,
            highlight_color=nord_fox['bg'],
            background=catppuccin['blue'],
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
