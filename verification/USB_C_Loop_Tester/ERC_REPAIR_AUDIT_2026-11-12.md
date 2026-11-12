# ERC correction audit (KiCad 10 / 2026-11-12)

## User-reported baseline
`ERC(2).rpt` was generated 2026-11-12 11:45:08 JST by the user running KiCad ERC. The report shows:

| ERC type | Baseline |
|---|---:|
| `pin_not_connected` | 18 errors |
| `power_pin_not_driven` | 2 errors |
| `unconnected_wire_endpoint` | 18 warnings |
| `lib_symbol_mismatch` (Device:Battery_Cell) | 1 warning |
| **Total** | **20 errors + 19 warnings = 39** |

**This was a real KiCad ERC report, and overrides the earlier incorrect static-only assertion that endpoints had all been fully validated.**

## Changes

1. Replaced the source-side power and receiver-side LED GND branched stubs with sequential pin-to-pin wire chains. Each resistor's positive pin is directly on its shared supply rail; each LED cathode is directly on its own cable-return rail. The CC1/CC2 and mirrored D+/D- pins now have direct short wires along the connector pin ends rather than branches terminating at intermediate offset points.
2. Explicit real wire segments: **63**; junction objects: **18**; net label objects: **0**; component instances **17**. The battery symbol and R2/R3/R4/R6 schematic positions have been moved to suit the new wire scheme; physical PCB component placements are unchanged.
3. USB Type-C VBUS/GND pins in the **test fixture** act only as passive conductors in a CR2032 test loop, not as the input power pins of a powered USB device. Added project-local full test-only symbol variants:
   - `USB_C_PCB_Edge:USB_C_Test_14P_USB2_NoShield`
   - `USB_C_PCB_Edge:USB_C_Test_10P_Power_NoShield`
   These change only the VBUS/GND electrical pin types from `power_in` to `passive`, preserving pin numbers, geometry, CC/USB2 pin electrical types, and footprint mappings. **Original general-purpose library symbols remain unmodified and available**, preventing accidental weakening of real product designs.
4. Consequently no PWR_FLAG is added to the test fixture, since it would incorrectly present passive cable contacts as actively driven power sources. Do not copy the test-only symbols to normal USB-powered device schematics.
5. Updated embedded `Device:Battery_Cell` to its canonical KiCad 10.x symbol definition with the two original passive pins preserved. Upstream reference is the 10.x symbols repository mirror: https://github.com/buildwithtrace/trace-kicad-symbols-lib/blob/main/Device.kicad_symdir/Battery_Cell.kicad_sym ; the authoritative project is https://gitlab.com/kicad/libraries/kicad-symbols .

## Static checks executed

- 74 symbol pins connected at coordinates that are all exact 50-mil grid points.
- 74 PCB pad numbers mapped to those 74 symbol pins.
- 16 connected schematic wire groups matched 16 expected PCB net groups.
- Unconnected pin endpoint count **0**, conflicting net groups **0**, nets split into disconnected wire groups **0**.
- No net labels used. Two pure wire crossings have no junction and are intentionally NOT electrically connected.
- KiCad ERC and DRC executables **not installed in the working environment**. The above are static checks, not a KiCad-native ERC pass.

## Outstanding verification

- Re-run ERC in the actual KiCad 10 installation and capture the new report. **A claim of 0 errors / 0 warnings is prohibited until then.**
- If `lib_symbol_mismatch` remains, compare cached Battery_Cell against the actual user's KiCad 10 installed library version before replacing it again.
- PCB remains an **unrouted placement draft (0 track segments)**. Mechanically the 0.8mm nominal and 6.2mm provisional protrusion remain unverified, along with 0.17mm copper-to-edge clearance.
- Do not connect this battery-powered fixture to a computer, charger, power bank or any powered USB port.
