# Rev.0.3 — Explicit schematic wiring and placement audit

## Scope

- Design: 14P PCB-edge receptacles J1/J2; 10P receptacles J3/J4; one CR2032 BT1; R1-R6 = 22kΩ; low-current red LEDs D1-D6.
- No switching button. USB-C cable insertion is the continuity switch.
- 0.8mm FR-4 2-layer ENIG and 6.2mm provisional tab geometry unchanged.

## Schematic

- Original labels replaced by physical orthogonal KiCad wire objects (94) plus junction objects (18).
- Every segment endpoint and schematic pin on 50mil / 1.27mm grid.
- Symbol references and pin numbers preserved; standard Device:R / Device:LED / Device:Battery_Cell symbols and USB-C local custom library retained.
- J1/J2 at top for 14P; J3/J4 below for 10P; resistors next to source pins and LEDs next to receiver pins; BT1 common to two signal groups.
- J1 ↔ J2 and J3 ↔ J4 **not wired together on PCB**; insertion of passive, unpowered C-C cable provides the required path.
- Static graph match against PCB pad-net assignments: 74 pins, 16 distinct nets, zero unconnected pin endpoints, zero mixed-net connected components, zero foreign-net wire endpoints landing inside another net's segment.

## PCB placement

- J1, J2, J3, J4 remain at board edges; BT1 remains at (76,90)mm.
- R1-R4 moved to source-side row Y=44mm at X=33,47,61,75mm.
- D1-D4 moved to receiver-side row Y=55mm at X=46,60,74,88mm.
- R5/R6 moved to (34,96)/(50,96)mm; D5/D6 moved to (44,83)/(59,83)mm.
- Net assignment unchanged. `pad_positions.csv` follows the new footprint coordinates.

## Important limitations

- PCB `*.kicad_pcb` has **0 routed copper tracks**. This is a placed layout draft, not a completed/testable manufacturing design.
- The 0.17mm GND copper-to-edge clearance remains pending manufacturing confirmation.
- KiCad 10 GUI, CLI ERC and DRC, Gerber inspection, real cable insertion and LED current/brightness are **not verified**.
- The user must not connect any PC/charger/powered USB device while battery is installed.

## Deliverable

Open the local `USB_C_Loop_Tester.kicad_pro` after extracting the entire ZIP, preserving `sym-lib-table`, `fp-lib-table`, `USB_C_PCB_Edge.kicad_sym` and `USB_C_PCB_Edge.pretty/` alongside it.
