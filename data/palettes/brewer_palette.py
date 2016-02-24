# Colors from www.ColorBrewer.org by Cynthia A. Brewer, 
# Geography, Pennsylvania State University. See BREWER for license. 
# See www.colorbrewer.org for details.
# 
# Color names are PALETTE-NUMCOLORS-TYPE-IDX (e.g. reds-3-seq-1)
#
#  PALETTE   palette name (e.g. reds)
#  NUMCOLORS number of colors in the palette (e.g. 3)
#  TYPE      palette type (div, seq, qual)
#  IDX       color index within the palette (e.g. 1)
#
# Another version of the color index is defined where COLORCODE is the
# color's letter unique to a given PALETTE.
#
# For each palette, two color list are defined for use with heatmaps.
#
#   PALETTE-NUMCOLORS-TYPE
#   PALETTE-NUMCOLORS-TYPE-rev
#
# where the second contains colors in reversed order.
#
# Each diverging and sequential palette has all the colors used for 
# its n-color variants listed an integrated 13-color (for sequential)
# or 15-color (for diverging) palettes.
#
# http://www.personal.psu.edu/cab38/ColorBrewer/ColorBrewer_updates.html
#
# http://mkweb.bcgsc.ca/brewer


colors = [
# Set3, 12 colors
(141,211,199),
(255,255,179),
(190,186,218),
(251,128,114),
(128,177,211),
(253,180,98),
(179,222,105),
(252,205,229),
(17,217,217),
(188,128,189),
(204,235,197),
(255,237,111),

# Paired, 12 colors
(166,206,227),
(31,120,180),
(178,223,138),
(51,160,44),
(251,154,153),
(227,26,28),
(253,191,111),
(255,127,0),
(202,178,214),
(106,61,154),
(255,255,153),
(177,89,40),

# Pastel1, 9 colors
(251,180,174),
(179,205,227),
(204,235,197),
(222,203,228),
(254,217,166),
(255,255,204),
(229,216,189),
(253,218,236),
(242,242,242),

# Set1, 9 colors
(228,26,28),
(55,126,184),
(77,175,74),
(152,78,163),
(255,127,0),
(255,255,51),
(166,86,40),
(247,129,191),
(153,153,153),

# Accent, 8 colors
(127,201,127),
(190,174,212),
(253,192,134),
(255,255,153),
(56,108,176),
(240,2,127),
(191,91,23),
(102,102,102),

# Dark 2, 8 colors
(27,158,119),
(217,95,2),
(117,112,179),
(231,41,138),
(102,166,30),
(230,171,2),
(166,118,29),
(102,102,102),

# Pastel2, 8 colors
(179,226,205),
(253,205,172),
(203,213,232),
(244,202,228),
(230,245,201),
(255,242,174),
(241,226,204),
(204,204,204),

# Set2, 8 colors
(102,194,165),
(252,141,98),
(141,160,203),
(231,138,195),
(166,216,84),
(255,217,47),
(229,196,148),
(179,179,179),
]