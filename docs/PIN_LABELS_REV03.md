# Rev.0.3 Pin/Pad numbering scheme

For the KiCad symbol and footprint the **pin/pad number** (not only the pin name) is:
`<USB-C standard contact number><signal/function>`, with no separator.

The pin's electrical type and its regular KiCad **name** (GND, VBUS, CC1, CC2, D+ or D-) are unchanged.

| USB-C contact | KiCad pin/pad number | KiCad pin name |
| --- | --- | --- |
| A1 | `A1GND` | GND |
| A4 | `A4VBUS` | VBUS |
| A5 | `A5CC1` | CC1 |
| A6 | `A6D+` | D+ |
| A7 | `A7D-` | D- |
| A9 | `A9VBUS` | VBUS |
| A12 | `A12GND` | GND |
| B1 | `B1GND` | GND |
| B4 | `B4VBUS` | VBUS |
| B5 | `B5CC2` | CC2 |
| B6 | `B6D+` | D+ |
| B7 | `B7D-` | D- |
| B9 | `B9VBUS` | VBUS |
| B12 | `B12GND` | GND |

- USB-C **A1 is GND**; **A4 is VBUS**. The example `A1VBUS` is electrically incorrect.
- Names like `A6D+` and `A7D-` use literal USB signal signs for legibility.
- 14P_USB2 variant includes every row; 10P_Power excludes A6, A7, B6, B7.
- Changing a footprint alone or a symbol alone will create unmapped pads; **update both together**.
- Existing designs built with the Rev.0.2 pad numbering should be rechecked for pin/pad mapping and net assignments before fabrication.
- Contact geometry, Edge.Cuts, soldermask openings, FR-4 0.8mm nominal baseline, and no-silkscreen decision are unchanged.
- KiCad 10 GUI/ERC/DRC and physical mating have not been executed as part of this revision.
