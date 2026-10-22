# USB-C PCBエッジ Rev.0.4: 寸法精度・ラッチ付近の銅箔保護

更新日: 2026-10-23。対象: `USB_C_Edge_14P_USB2_NoSilk`（推奨）/ `USB_C_Edge_10P_Power_NoSilk`（試験用）。

## 実行したCAD改善

2層フットプリント双方に **各4個**（F.Cu/B.Cu × 上下側面）のKiCad Rule Area Keepoutを追加。

- 名前: `USB_C_LATCH_KEEPOUT_F_TOP` など
- 範囲（フットプリント座標）: X=-6.835～-0.635mm、Y=+2.950～+4.500mm／Y=-4.500～-2.950mm
- 制限: Tracks / Vias / Copper pourを禁止、既存Padは許可
- `Cmts.User` に製造上の注意を記載。**F.SilkS/B.SilkSと銅箔接点、Edge.Cuts形状は変更なし**。
- 禁止エリアは外形の外側にも重なる（切削済み部分には銅箔がないため）。実際に基板が存在する部分でのみ効きます。
- GNDパッド幅0.25mm、中心Y=±2.75mm、最外縁±2.875mm。Rule Areaの端Y=±2.950mmとは0.075mm離れています。**既存パッドは侵さないが、接点脇の銅箔自動流し込みや不要ビアを抑止する目的**です。

KiCad 10のRule Areaは通常PCBに配置したフットプリントへ引き継がれます。ただし、CLI版DRCの一部バージョンでkeepout違反を自動検出しない報告（kicad-tools #6039、2026-10-07）があります。従って**keepoutだけを根拠に安全確認済みとしない**でください。配置後、PCBエディターでレイヤー表示して確認してください。

## 発見した精度リスク・未修正点

### 1. GND接点から基板Edge.Cutsまで最短約0.170mm

- GND(A1/A12/B1/B12)の横中心 |Y|=2.750mm、幅0.250mm → 銅箔外端 |Y|=2.875mm。
- 接点が通る範囲のラッチ切り欠きEdge.Cuts内側は |Y|=3.045mm → 0.170mm（最短）。
- JLCPCBの**通常のルーター加工の銅箔・基板エッジ間隔は≧0.200mm**との公開値があり、現行0.170mmはこれを0.030mm下回ります。
- エッジ端子向け加工例外の可否は未確認。通常の配線と金端子では製造側の処理条件が異なる可能性があるため、**パッド中心を直ちに移動せず、JLCPCBへ製造可否確認を要する**。
- この問題は既存銅箔のものなので、側面Keepoutの追加では解消されません。

### 2. 板厚0.8mm・ENIGおよび6.2mm突出部

- 0.8mmは本ライブラリの設計基準。国内先行例があるが、元のUSB-IF舌片厚の規定や全ケーブルへの適合は保証しない。
- 6.200mmの「先端―基板肩」距離は暫定値。USB-Cの有効シェル長6.20mmをPCBの挿入深さ規格値と取り違えない。
- シルクなし、後端パッドなし、金属シールドなしは要求仕様として維持。仕上げはENIG、接点部分には半田ペーストを出さない。

### 3. 2層配線と配線ルール（14P版）

- A6D+ と B6D+ を同じD+、A7D- と B7D- を同じD-に接続する。短絡させる位置はできるだけレセプタクル近傍、USB-IF参考注記でUSB2分岐の短絡配線長は最大3.5mm以下が望ましい。
- CC1(A5)/CC2(B5)は電源を受ける機器なら独立した約5.1kΩのRd（PD受電ICが終端内蔵なら重複実装しない）。
- 10P簡略型は**USB Type-C規格のPower-Only Receptacleではない**。正式のPower-Only Receptacleは14接点＋D+/D-間短絡を要求する（USB Type-C Specification R2.4 §3.3 item 17）。10Pは試作・低頻度給電を目的とする独自構成として残す。
- このフットプリント単体には回路上のD+短絡・CC抵抗・電源保護回路は含まれない。組み込み回路で設計する。

### 4. 製造時の嵌合評価

- 複数のUSB-Cケーブルを表裏両方向で挿入、**先端が底突きしない／短すぎて差し込み不足にならない**ことを確認。
- 物理寸法の実測、5V導通、CC抵抗確認、USB列挙、ESP32書き込み試験を記録。
- 0.8mm板厚／6.2mm長さの適合性を実測してから製造確定とする。

## 根拠

- AnasMalas PCB-edge-usb-c: https://github.com/AnasMalas/pcb-edge-usb-c （ラッチ摩耗・金属ラッチから露出導体への接触）
- JLCPCB製造能力: https://jlcpcb.com/jp/capabilities/Capabilities （ルーター銅箔―基板外形≧0.2mm）
- JLCPCB Gold Fingers: https://jlcpcb.com/jp/help/article/jlcpcb-gold-fingers （ENIG、マスク開口、面取りの制限）
- KiCad 10 Rule Areas: https://docs.kicad.org/10.0/ja/pcbnew/pcbnew.pdf
- KiCad File Format Zone: https://dev-docs.kicad.org/en/file-formats/sexpr-intro/
- KiCad kicad-tools issue #6039: https://github.com/rjwalters/kicad-tools/issues/6039
- USB Type-C R2.4 (2024): https://www.usb.org/documents
