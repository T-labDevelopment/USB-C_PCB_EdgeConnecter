# PCB STATUS — 6 automatic per-signal LEDs / Rev.0.3

Current preferred prototype: J1/J2 14P, J3/J4 10P, CR2032, 6×LED, 6×22kΩ. No switch. LEDs are grouped by VBUS, CC, D+, D− on 14P and VBUS, CC on 10P. All signals use the respective cable's GND as a return.

- Schematic symbol instances: 17; PCB footprints: 17; PCB pads: 74.
- PCB design contains **0 routed copper tracks** and is a placement/net assignment draft only, **NOT A FUNCTIONAL FABRICATION DESIGN**.
- Nominal PCB thickness: 0.8mm FR4, 2 layers, ENIG, connector protrusion 6.2mm provisional.
- Complete PCB routing, ERC/DRC, Gerber review, fabrication approval for 0.17mm copper-edge clearance, cable mating and LED visibility tests remain pending.
- No main integration performed; changes remain on feature branch.

## 2026-11-12 schematic direct-wire and placement update

- New schematic has **94 explicit wire segments**, **18 junctions**, **0 net labels**. Physical pin placement on the schematic is aligned to the KiCad 50mil grid.
- Verified logical graph: 74 symbol pins, 16 connected groups, matching 16 PCB pad-net groups. No missing pin endpoints or mixed-net connected sections detected in static checks.
- J1/J2 are top schematic lane (14P); J3/J4 bottom (10P); battery and six resistors are in source supply bank and six LEDs in return bank.
- Moved 12 physical components (R1-R6 and D1-D6) on the PCB for clearer source/receiver correspondence. J1-J4 and BT1 coordinates and footprints unchanged. Corresponding pad-position CSV updated.
- Board copper routing remains **0 segments**. This is not a connected or manufacturable PCB. Native KiCad 10 load, ERC, DRC and functional tests have not been run.
