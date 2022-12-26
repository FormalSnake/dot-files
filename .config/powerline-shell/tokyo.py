import sys

from powerline_shell.themes.default import DefaultColor

N = []

for i, n in enumerate([47, 68, 40, 40, 40, 21]):
    N.extend([i]*n)


def rgb_to_xterm(r, g, b):
    mx = max(r, g, b)
    mn = min(r, g, b)

    if(mx-mn)*(mx+mn) <= 6250:
        c = 24 - (252 - ((r+g+b) // 3)) // 10
        if 0 <= c <= 23:
            return 232+c

    return 16 + 36*N[r] + 6*N[g] + N[b]


def hex_to_xterm(hex_color):
    r = int(hex_color[1:3], 16)
    g = int(hex_color[3:5], 16)
    b = int(hex_color[5:7], 16)
    return rgb_to_xterm(r, g, b)


# TokyoNight colors
background = '#1a1b26'
foreground = '#c0caf5'
selection_background = '#33467C'
selection_foreground = '#c0caf5'
url_color = '#73daca'
cursor = '#c0caf5'
active_tab_background = '#7aa2f7'
active_tab_foreground = '#1f2335'
inactive_tab_background = '#292e42'
inactive_tab_foreground = '#545c7e'
color0 = '#15161E'
color1 = '#f7768e'
color2 = '#9ece6a'
color3 = '#e0af68'
color4 = '#7aa2f7'
color5 = '#bb9af7'
color6 = '#7dcfff'
color7 = '#a9b1d6'
color8 = '#414868'
color9 = '#f7768e'
color10 = '#9ece6a'
color11 = '#e0af68'
color12 = '#7aa2f7'
color13 = '#bb9af7'
color14 = '#7dcfff'
color15 = '#c0caf5'
color16 = '#ff9e64'
color17 = '#db4b4b'

username_fg = '#161720'
username_bg = '#7ca4f4'
dir_bg = '#1f2334'
dir_fg = '#a9b2d5'
repo_bg = '#3b4360'
repo_fg = '#79a2ee'
black = '#15161e'
white = '#FFFFFF'

# function to convert hex color string into the nearest Xterm color between 0 and 16


class Color(DefaultColor):
    """
    color class for powerline-shell using xterm 256-color versions of the above colors
    """
    USERNAME_FG = hex_to_xterm(username_fg)
    USERNAME_BG = hex_to_xterm(username_bg)
    # USERNAME_ROOT_BG = hex_to_xterm(color1)
    # USERNAME_ROOT_FG = hex_to_xterm(color0)

    HOSTNAME_FG = hex_to_xterm(foreground)
    HOSTNAME_BG = hex_to_xterm(selection_background)

    HOME_SPECIAL_DISPLAY = True
    HOME_BG = hex_to_xterm(background)
    HOME_FG = hex_to_xterm(foreground)

    PATH_BG = hex_to_xterm(dir_bg)
    PATH_FG = hex_to_xterm(dir_fg)

    CWD_FG = hex_to_xterm(dir_fg)
    CWD_BG = hex_to_xterm(dir_bg)

    SEPARATOR_FG = hex_to_xterm(dir_fg)

    REPO_CLEAN_BG = hex_to_xterm(repo_bg)
    REPO_CLEAN_FG = hex_to_xterm(repo_fg)

    REPO_DIRTY_BG = hex_to_xterm(repo_bg)
    REPO_DIRTY_FG = hex_to_xterm(repo_fg)

    SSH_BG = hex_to_xterm(background)
    SSH_FG = hex_to_xterm(foreground)

    GIT_AHEAD_BG = hex_to_xterm(color8)
    GIT_AHEAD_FG = hex_to_xterm(black)
    GIT_BEHIND_BG = hex_to_xterm(color8)
    GIT_BEHIND_FG = hex_to_xterm(black)
    GIT_STAGED_BG = hex_to_xterm(color10)
    GIT_STAGED_FG = hex_to_xterm(black)
    GIT_NOTSTAGED_BG = hex_to_xterm(color11)
    GIT_NOTSTAGED_FG = hex_to_xterm(black)
    GIT_UNTRACKED_BG = hex_to_xterm(color9)
    GIT_UNTRACKED_FG = hex_to_xterm(black)
    GIT_CONFLICTED_BG = hex_to_xterm(color17)
    GIT_CONFLICTED_FG = hex_to_xterm(black)
    GIT_STASH_BG = hex_to_xterm(color16)
    GIT_STASH_FG = hex_to_xterm(black)

    JOBS_FG = hex_to_xterm(black)
    JOBS_BG = hex_to_xterm(color3)

    CMD_PASSED_BG = hex_to_xterm(color2)
    CMD_PASSED_FG = hex_to_xterm(black)
    CMD_FAILED_BG = hex_to_xterm(color1)
    CMD_FAILED_FG = hex_to_xterm(black)