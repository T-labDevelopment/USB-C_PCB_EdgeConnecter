# 2026-11-13: USB-C contact pads extended toward PCB body

**Working branch**: `feature/usb-c-rev07-inboard-contact-extensions`

- J1-J4 all 48 USB-C contact pads now extend **2.4mm inward**, with the original mating/tip endpoints unchanged.
- Contact pad inner end moved from footprint-local X=-2.385mm to X=+0.015mm, 0.65mm beyond the last latch keepout X=-0.635mm.
- F.Cu/B.Cu widths remain 0.25mm, nearest pad gap 0.25mm, 0.20mm configured board clearance. Electrical net assignments are unchanged.
- Libraries 14P+10P, board instances and pad_positions.csv all match. Static checks PASS.
- Keepout rules (tracks/vias/pours blocked), 0.8mm PCB, edge geometry, 24 LEDs/24 resistors unchanged.
- WARNING: mask opening grows with the pads; physical mating/ENIG/mask web testing not completed.
- Board tracks=0 and no native KiCad 10 ERC/DRC. **NOT MANUFACTURING APPROVED**.
- [Source geometry audit](REV07_INBOARD_PAD_EXTENSION_2026-11-13.md).

---

# 2026-11-13 Rev.0.7 USB-C latch keepout routing ECO

**Git branch:** `fix/usb-c-rev07-latch-keepout-routing`

- At A1/A12/B1/B12 the source pad's outer Y edge is ±2.875mm; old latch keepout starts at ±2.950mm (gap 0.075mm).
- Move track-keepout inner Y edge only to ±3.375mm (gap **0.500mm**).
- Applied to J1-J4 board footprints and both 14P/10P `.kicad_mod` libraries. Retained outer boundaries, pad geometry and keepout rules.
- Source geometry and footprint counts checked; KiCad 10 ERC/DRC and actual route-start test **not yet run**. PCB copper track count remains **0**, not manufacturable.
- Full audit: [REV07_LATCH_KEEPOUT_ROUTING_FIX_2026-11-13.md](REV07_LATCH_KEEPOUT_ROUTING_FIX_2026-11-13.md).

---

# PCB STATUS — Rev.0.7: 24 isolated connector contact LED/R branches

**Current source files:** USB_C_Loop_Tester.kicad_sch / USB_C_Loop_Tester.kicad_pcb.

- J1/J2: 14 distinct source-to-destination contact paths with R1-R14 and D1-D14.
- J3/J4: 10 distinct contact paths with R15-R24 and D15-D24.
- Total: 53 footprints, 146 pads, 50 named nets (24 SRC + 24 DST + BAT_POS/BAT_NEG), all per-pad USB nets separate.
- External CR2032 BT1 moved to (31,18)mm and (35.2,18)mm. No on-board battery holder.
- PCB tracks 0 / vias 0. **NOT ROUTED, NOT MANUFACTURABLE.**
- Native KiCad 10 ERC/DRC and actual component/USB mating tests NOT RUN.
- 0.17mm copper-to-edge issue still open. Cable-internal shorted VBUS/GND pins and USB2 absent B6/B7 limit interpretation.
- Revision detail: [REV07_INDIVIDUAL_CONTACT_CIRCUIT.md](REV07_INDIVIDUAL_CONTACT_CIRCUIT.md).
- The Rev.0.6 and earlier records below are history only and do not describe the current routed-net assignments.

---

# Rev.0.6: external CR2032 on two official KiCad solder-wire pads

The board-mounted CH25-2032LF footprint and three NPTH peg holes were removed from BT1. Two KiCad Connector_Wire pads (pitch 4.2mm, drill 0.85mm) now connect an off-board CR2032 cell holder through two insulated wires. Pad1 BAT_POS, Pad2 BAT_NEG. Existing six-LED cable continuity circuit intact. Board copper routes: 0. KiCad ERC/DRC not executed.

---

# BT1 CH25-2032LF 変更 — 2026-11-12

秋月電子100706／COMF CH25-2032LFを採用予定。BT1の旧Keystoneを専用COMFフットプリントへ置換、20mm離れたTHT端子2つ＋Ø1.9mm NPTH位置決め穴3つを反映。回路図の標準電池シンボルは維持、BOMとライブラリテーブルを更新。

**プラス端子は暫定割当で、メーカー図面から確定不可。現物テスター検査が必須。**
**PCB配線0本。KiCad-native ERC/DRC 未実施。**

---

# PCB STATUS — Rev.0.5 Unified 14P + 10P

**Preferred circuit version:** Rev.0.5 (2026-11-12). 6 LED indicators, one per signal group, R1-R6 22k, CR2032. J1/J2=14P, J3/J4=10P. Cable insertion itself is the switch.

- Schematic: 17 symbols, 74 pins, 16 connected nets, 85 wires, 18 junctions and 0 labels.
- PCB: 17 footprints / 74 pads. Eight LED/resistor footprints adjusted and pad-position CSV updated. USB connector tabs and BT1 untouched.
- **PCB routed copper segments: 0. NOT MANUFACTURABLE.** ERC/DRC and real cable/LED trials NOT RUN.
- Static graph test and idealized cable presence/open-conductor test: PASS. This is not a KiCad-native ERC result.
- Nominal FR4 thickness 0.8mm, 2 layers, ENIG, protruding tab 6.2mm provisional; copper-edge clearance ~0.17mm needs fabrication verification.

All older rev entries below refer to historical files, not current schematic statistics.

---
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

## 2026-11-12: ERC(2).rpt corrections

Input KiCad ERC: 20 errors / 19 warnings: 18 open pins, 18 dangling wire endpoints, 2 undriven input-power pins, 1 Battery_Cell mismatch.

Rev.0.4 schematic: 63 explicit wires; 18 junctions; no net labels. Supply and LED returns rerouted as pin-to-pin chains. Full project-only USB-C test fixture symbol variants use passive VBUS/GND pin types; original general-purpose USB-C symbols retained. Battery_Cell embedded from KiCad 10.x official-layout symbol data.

Static connectivity graph check: 74 schematic pins == 74 PCB pads, in 16 net groups, 0 open pins, 0 mixed-net connections. Two signal lines cross without a junction (no electrical short).

**Native KiCad 10 ERC NOT RUN, ERC0/Warn0 NOT CONFIRMED**. PCB has 0 routed copper tracks, no KiCad DRC or physical tests. Do not order as a functioning PCB.
