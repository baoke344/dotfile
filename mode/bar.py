from libqtile import widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.bar import Bar
from mode.color import nord_fox

BAR_HEIGHT = 28

bar = Bar(
            [
                widget.CurrentLayout(),
                widget.GroupBox(
                    disable_drag=True,
                    active=nord_fox['magenta'],
                    inactive=nord_fox['black'],
                    highlight_method='line',
                    block_highlight_text_color=nord_fox['blue'],
                    borderwidth=0,
                    highlight_color=nord_fox['bg'],
                    background=nord_fox['bg'],
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
            size=BAR_HEIGHT,
            margin=8,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        )