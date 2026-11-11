# PCB placement state

`USB_C_Loop_Tester.kicad_pcb` is the **native KiCad PCB placement draft**. Four USB-C board-edge footprints are embedded using the existing 0.8mm design, and 6 switches + 6 current-limiting resistors + 6 LEDs + one Keystone 103 CR2032 THT holder are placed using the KiCad-standard libraries' full original pad/graphics definitions.

- Body outline: X=20..107mm, Y=10..94mm; four edge tabs protrude on left/right.
- Edge.Cuts lines are intended to join the four embedded connector outlines at their open shoulders.
- Connector assignments: J1 left 14P source, J2 right 14P LED return, J3 left 10P source, J4 right 10P LED return.
- PCB soldermask and copper contacts are the existing connector footprints with no added contact-zone silkscreen.
- **Tracks/vias have not yet been routed. The PCB will NOT light the LEDs if fabricated as-is.** Use the included net assignment to complete routing and run KiCad 10 DRC before order.
- Schematic embedded Device/Switch symbols are copied intact from a recent KiCad project using official Device/R, LED, Battery_Cell and Switch/SW_Push library symbols, not reconstructed pseudo symbols.
- Legacy official KiCad footprint graphic/pad geometry is converted into KiCad's modern footprint syntax on this board while keeping the pad dimensions and relative coordinates.
- **The entire physical placement remains provisional**: the true Keystone 103 holder size, body and label overlaps, edge interference, hole tolerances, copper clearance to Edge.Cuts, mask, and KiCad GUI import must be checked.
- Electrical details: see README.md in this directory.
