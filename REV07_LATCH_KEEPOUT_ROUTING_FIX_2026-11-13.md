# USB-C Rev.0.7: latch keepout and GND pad routing correction (2026-11-13)

## Symptom
KiCad 10 showed "配線の開始点は DRC に違反しています。" when attempting to begin a trace near the outer USB-C GND pads (A1/A12/B1/B12). The screenshot showed the hatched latch keepout immediately adjacent to the edge-contact pads.

## Verified root cause from source geometry
Both 14P and 10P edge-connector footprints use GND contact pads centered at local Y=±2.750 mm, with Y extent ±0.125 mm (pad width=0.25 mm, 270° rotation). Their outer copper edges are therefore Y=±2.875 mm. The original track-keepout inner boundaries were Y=±2.950 mm, leaving only **0.075 mm** from copper to track-prohibited area. Routing with normal width and clearance can fail when starting near this boundary. This is a geometric observation; a native KiCad router/DRC invocation was not executed here.

## Modification
The pad-facing inner bounds of the four latch keepout zones per footprint have been moved:
- Upper Y: +2.950 -> **+3.375 mm**
- Lower Y: -2.950 -> **-3.375 mm**
- GND pad-to-track-keepout geometric spacing: **0.075 -> 0.500 mm** (an increase of 0.425 mm)
- The outer Y bounds ±4.500 mm and local X bounds -6.835 to -0.635 mm are unchanged.
- Each latch strip retains **1.125 mm** of Y span, subject to mechanical review.

Applied to **all four PCB-embedded USB-C footprints (J1-J4)** and to **both editable library footprints**:
- `USB_C_PCB_Edge.pretty/USB_C_Edge_14P_USB2_NoSilk.kicad_mod`
- `USB_C_PCB_Edge.pretty/USB_C_Edge_10P_Power_NoSilk.kicad_mod`

No pad coordinates/dimensions, layers, nets, board outline, component positions, PCB thickness (0.8 mm), schematic, or electrical component content was changed. All `(tracks not_allowed)`, `(vias not_allowed)`, and `(copperpour not_allowed)` protections remain enabled.

## Source-level checks
- Board still contains 146 pads, 16 keepout zones and **0 copper track segments**.
- 14P library: 14 pads, 4 zones. 10P library: 10 pads, 4 zones.
- Board source has all 8 positive-Y and 8 negative-Y rectangle occurrences at the revised positions.
- Two footprint library sources each have 2 positive-Y and 2 negative-Y revised rectangles.
- Source checks passed. **KiCad 10 native ERC and DRC were not run.** Real interactive trace-start verification and mechanical latch-mating verification remain outstanding.

## Remaining restrictions
This correction is designed to remove the over-restrictive zone boundary but **does not** mean PCB routing is complete or DRC reports zero violations. The original PCB is intentionally still unrouted. The existing USB contact edge-to-Edge.Cuts manufacturing clearance issue (~0.17 mm) is outside this change and remains unapproved. Do not fabricate as a completed functioning electrical tester yet.

## Git management
Base: `feature/usb-c-individual-pad-led-rev07`. Changes are on `fix/usb-c-rev07-latch-keepout-routing`. No merge to `main`. Retain the prior data in history. Apply native KiCad DRC and inspect both source-library and PCB-embedded geometry before merging.

## References
- KiCad PCB Editor: https://docs.kicad.org/10.0/en/pcbnew/pcbnew.html
- KiCad footprint format: https://dev-docs.kicad.org/en/file-formats/sexpr-footprint/index.html
