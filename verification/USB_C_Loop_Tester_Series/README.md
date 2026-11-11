# CR2032 USB-C PCB-edge series-loop tester

**Preferred simple version** of the USB-C connector test board: two 14P contacts and two 10P contacts integrated into a single 0.8mm/2-layer/ENIG PCB, two 2.2k resistors, two momentary 6mm tactile switches, two low-current red LEDs and one CR2032 holder.

## Cable electrical path: 14P (J1 ⟷ J2)

CR2032 + → SW1 → R1 → J1 VBUS → USB-C cable → J2 VBUS → [J2 CC1/CC2] → CC cable wire → [J1 CC1/CC2] → [J1 D+] → USB-C cable → [J2 D+] → [J2 D−] → cable → [J1 D−] → [J1 GND] → cable → [J2 GND] → LED D1 anode → D1 cathode → CR2032 −.

## Cable electrical path: 10P (J3 ⟷ J4)

CR2032 + → SW2 → R2 → J3 VBUS → cable → J4 VBUS → [J4 CC1/CC2] → CC cable wire → [J3 CC1/CC2] → [J3 GND] → cable → J4 GND → LED D2 anode → D2 cathode → CR2032 −.

All brackets indicate **intentional local loopback connections** on the test PCB, **not** a standard USB device/host wiring scheme. Each cable carries no external voltage; **never connect this tester to a PC, USB adapter, charger or USB power bank with the battery installed**. Use passive USB-C to USB-C cables only.

Lighting indicates continuity of VBUS+CC+GND (plus D+/D− for 14P) through the cable loop; **it does not prove every redundant pad individually, exact contact resistance, lack of shorting between groups, USB protocol/PD functionality, or USB-IF compliance**. Flip each end of the cable individually to exercise CC contact orientation.

This version deliberately replaces the earlier 6-LED design because two series loops are simpler and require far fewer parts and cross-connections. The 6-LED design remains in `../USB_C_Loop_Tester` as an exploratory design.

PCB outline approximately 99.4 × 95mm including 4 edge tabs. Contact geometry remains the current 0.8mm Rev.0.4 library, 6.2mm provisional protrusion length. Manufacturer approval for 0.17mm edge copper clearance remains pending.

**STATUS: schematic/net assignments and PCB placement created. PCB copper tracks are NOT routed; ERC/DRC, physical fit and electrical continuity are NOT verified. Do not order this version as a functional board until routed and checked.**
