import sys
import cadquery as cq
import math

##################################################
# CadQuery doesn't do a full reload, so delete all our loaded modules and reload
for f in sorted(sys.modules.keys()):
    if "keyboard_builder" in f:
        try:
            del sys.modules[f]
        except:
            pass

from keyboard_builder import keyboard, primitives

##################################################
# Build the keyboard

kb = keyboard(
    rowCounts = [4, 4, 4, 4, 4, 4, 4],
    columnDeltas = [
        #0,0,0,0,0,0,0,0,0,
        0,
        -0.25,
        -0.25,
        -0.375,
        0.125,
        0.375,
        0.5
    ],
    extraKeys = [
        primitives.point(3.375, 4.125),
        primitives.point(4.375, 4.125),
        primitives.point(5.375, 4.25),
        primitives.point(6.375, 4.625),
    ],
    outlineLocations = [
        {"position": primitives.point( 2.25, -1.375), "isDrill": True,  "convex": True,  "offsetByHandAngle": False}, # Far top of board
        {"position": primitives.point(-0.375, -0.75 ), "isDrill": True,  "convex": True,  "offsetByHandAngle": False}, # Top Left of main keys
        {"position": primitives.point(-0.375,  3.75 ), "isDrill": True,  "convex": True,  "offsetByHandAngle": False},  # Bottom left of main keys
        {"position": primitives.point( 2.625, 3.75 ), "isDrill": False, "convex": False, "offsetByHandAngle": False}, # Control point to get horizontal line
        {"position": primitives.point( 2.625, 4.75  ), "isDrill": True,  "convex": True,  "offsetByHandAngle": False}, # Left of thumb cluster
        {"position": primitives.point( 4.25,  5 ), "isDrill": False, "convex": False, "offsetByHandAngle": False}, # Control point for "steeper" 5-way outline
        {"position": primitives.point( 4.625, 6.0  ), "isDrill": True,  "convex": True,  "offsetByHandAngle": False}, # Bottom left of 5-way
        {"position": primitives.point( 6.125, 6.0  ), "isDrill": True,  "convex": True,  "offsetByHandAngle": False}, # Bottom right of 5-way
        {"position": primitives.point( 8.5,   4.75 ), "isDrill": True,  "convex": True,  "offsetByHandAngle": True }, # Far right
        {"position": primitives.point( 8.5,   0.625), "isDrill": True,  "convex": True,  "offsetByHandAngle": True }, # Top right
        {"position": primitives.point( 7.375 + ((8.5-7.375)/2), 0.625 + ((8.5-7.375)/2)), "isDrill": False, "convex": False, "offsetByHandAngle": True}, # Control point for TRS jack
        {"position": primitives.point( 7.375, 0.625), "isDrill": False, "convex": True,  "offsetByHandAngle": True }, # Right of USB -- TRS control point
        {"position": primitives.point( 6.875, 0.125), "isDrill": True,  "convex": True,  "offsetByHandAngle": True }, # Right of USB
        {"position": primitives.point( 5.9,   0.125), "isDrill": True,  "convex": False, "offsetByHandAngle": True }, # Left of USB
    ],
    extraDrills = [
        {"position": primitives.point(6.8125,2.625 ), "isDrill": True, "offsetByHandAngle": False },
    ],
    outlineOffset = 5,
    handAngleDegrees = 10,
    edgeLEDCounts = [ # how many LEDs to evenly space along each edge -- edges generated by linking the outline locations above
        0, 0, 2, 0, 1, 1, 1, 3, 3
    ],
    spacerLocations = [
        {"position": primitives.point(2.52, -1.46), "convex": True, "offsetByHandAngle": False}, # top of main keys
        {"position": primitives.point(2.52, -1.125), "convex": False, "offsetByHandAngle": False}, # top of main keys
        {"position": primitives.point(-0.125, -0.75), "convex": True, "offsetByHandAngle": False}, # top left of main keys
        {"position": primitives.point(-0.125, -0.5), "convex": False, "offsetByHandAngle": False}, # top left of main keys
        {"position": primitives.point(-0.475, -0.5), "convex": True, "offsetByHandAngle": False}, # top left of main keys
        {"position": primitives.point(-0.475, 3.5), "convex": True, "offsetByHandAngle": False}, # bottom left of main keys
        {"position": primitives.point(-0.25, 3.5), "convex": False, "offsetByHandAngle": False}, # bottom left of main keys
        {"position": primitives.point(-0.125, 3.6), "convex": True, "offsetByHandAngle": False}, # bottom left of main keys
        {"position": primitives.point(2.35, 3.6), "convex": False, "offsetByHandAngle": False}, # control point for horizontal line
        {"position": primitives.point(2.875, 4.625), "convex": True, "offsetByHandAngle": False}, # left of thumb cluster
        {"position": primitives.point(4.375, 4.85), "convex": False, "offsetByHandAngle": False}, # top left of dpad
        {"position": primitives.point(4.7, 5.75), "convex": True, "offsetByHandAngle": False}, # bottom left of dpad
        {"position": primitives.point(4.78, 5.75), "convex": False, "offsetByHandAngle": False}, # bottom left of dpad
        {"position": primitives.point(4.88, 5.85), "convex": True, "offsetByHandAngle": False}, # bottom right of dpad
        {"position": primitives.point(5.9, 5.85), "convex": True, "offsetByHandAngle": False}, # bottom right of dpad
        {"position": primitives.point(6, 5.75), "convex": False, "offsetByHandAngle": False}, # bottom right of dpad
        {"position": primitives.point(6.18, 5.75), "convex": True, "offsetByHandAngle": False}, # bottom right of dpad
        {"position": primitives.point(7.73, 4.33), "convex": False, "offsetByHandAngle": False}, # bottom of encoder
        {"position": primitives.point(8.08, 4.33), "convex": True, "offsetByHandAngle": False}, # bottom right of encoder
        {"position": primitives.point(8.08, 4.0), "convex": False, "offsetByHandAngle": False}, # right of encoder
        {"position": primitives.point(8.56, 3.55), "convex": False, "offsetByHandAngle": False}, # bottom of reset
        {"position": primitives.point(8.83, 3.55), "convex": True, "offsetByHandAngle": False}, # bottom right of reset
        {"position": primitives.point(8.83, 3.2), "convex": True, "offsetByHandAngle": False}, # right of reset
        {"position": primitives.point(8.4, 3.2), "convex": True, "offsetByHandAngle": False}, # top of reset
        {"position": primitives.point(6.55, 4.6), "convex": False, "offsetByHandAngle": True}, # bottom outer left of LCD
        {"position": primitives.point(6.0, 3.85), "convex": False, "offsetByHandAngle": True}, # bottom left of inner screw
        {"position": primitives.point(6.0, 3.54), "convex": False, "offsetByHandAngle": True}, # top left of inner screw
        {"position": primitives.point(6.4, 3.54), "convex": False, "offsetByHandAngle": True}, # top right of inner screw
        {"position": primitives.point(6.93, 4.17), "convex": True, "offsetByHandAngle": True}, # bottom inner left of LCD
        {"position": primitives.point(8.22, 4.17), "convex": True, "offsetByHandAngle": True}, # bottom inner right of LCD
        {"position": primitives.point(8.35, 4.03), "convex": True, "offsetByHandAngle": True}, # bottom inner right of LCD
        {"position": primitives.point(8.35, 1.3), "convex": True, "offsetByHandAngle": True}, # top inner right of LCD
        {"position": primitives.point(8.25, 1.2), "convex": False, "offsetByHandAngle": True}, # top inner right of LCD
        {"position": primitives.point(8.25, 0.9), "convex": True, "offsetByHandAngle": True}, # top inner right of LCD
        {"position": primitives.point(7.95, 0.9), "convex": True, "offsetByHandAngle": True}, # right of split connector
        {"position": primitives.point(7.77, 0.9), "convex": True, "offsetByHandAngle": True}, # right of split connector
        {"position": primitives.point(7.42, 1.25), "convex": False, "offsetByHandAngle": True}, # bottom right of split connector
        {"position": primitives.point(7.32, 1.25), "convex": False, "offsetByHandAngle": True}, # bottom right of split connector
        {"position": primitives.point(6.67, 0.60), "convex": True, "offsetByHandAngle": True}, # right of USB connector
        {"position": primitives.point(5.65, 0.60), "convex": False, "offsetByHandAngle": True}, # left of USB connector
        {"position": primitives.point(5.65, -0.08), "convex": True, "offsetByHandAngle": True}, # left of USB connector
    ],
    switchOrder = [
        # Normal row/col
        1, 8, 15, 22,
        2, 9, 16, 23,
        3, 10, 17, 24,
        4, 11, 18, 25,
        5, 12, 19, 26,
        6, 13, 20, 27,
        7, 14, 21, 28,
        # Extra keys
        29, 30, 31, 32
    ],
    ledFlip = [
        # Normal rows/cols (x28) -- each line is a column
        False, True, False, True,
        False, True, False, True,
        False, True, False, True,
        False, True, False, True,
        False, True, False, True,
        False, True, False, True,
        False, True, False, True,
        # Extra keys (x4)
        False, False, False, False,
        # Underglow (x11)
        False, False, False, False, False, False, False, False, False, False, False
    ],
    extraLeds = [
        43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33
    ]
)

##################################################
# File Export

cq.exporters.dxf.CURVE_TOLERANCE = 1e-7

outline=kb.render(
           #locations=True,
           #keyswitchCuts=True,
           keyswitchOutlines=True,
           #drills=True,
           #drillPads=True,
           outline=True,
           spacer=True,
           #lcdOutline=True,
           #lcdDrills=True,
           #lcdPlateCuts=True,
           lcdSpacerCuts=True,
           lcdPinCuts=True,
           #lcdDrillPads=True,
           encoderCut=True,
           #encoderKnob=True,
           dpadCut=True,
           dpadHousing=True,
           #resetCut=True,
           resetHousing=True,
           edgeLedCuts=True,
           usbCut=True,
           splitCut=True,
           kicadScript=True
        )
cq.exporters.export(kb.render(outline=True), "../dxf/outline.dxf")
cq.exporters.export(kb.render(outline=True, drills=True), "../dxf/outline+drills.dxf")
cq.exporters.export(kb.render(outline=True, drills=True, resetCut=True), "../dxf/base_pcb.dxf")
cq.exporters.export(kb.render(
    outline=True,
    keyswitchCuts=True,
    drills=True,
    lcdPlateCuts=True,
    lcdPinCuts=True,
    encoderCut=True,
    dpadCut=True
    ), "../dxf/plate_pcb.dxf")
cq.exporters.export(kb.render(keyswitchOutlines=True), "../dxf/keyswitch_outlines.dxf")
cq.exporters.export(kb.render(keyswitchCuts=True), "../dxf/keyswitch_cuts.dxf")
cq.exporters.export(kb.render(outline=True, spacer=True, lcdSpacerCuts=True, lcdPinCuts=True, edgeLedCuts=True, usbCut=True, splitCut=True), "../dxf/acrylic_spacer.dxf")
