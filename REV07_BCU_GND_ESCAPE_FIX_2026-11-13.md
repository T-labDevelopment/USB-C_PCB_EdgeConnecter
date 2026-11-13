# Rev.0.7 B.Cu 配線開始・GND帰路修正監査（2026-11-13）

## 変更の目的
KiCad 10の下側銅箔(B.Cu)でUSB-C接点の配線開始がDRC違反になる事象と、GNDの正しい取り扱いが不明瞭だった問題に対応した。

## 1. B.Cuの独立引き出し配線を追加
- PCB実データ `USB_C_Loop_Tester.kicad_pcb` に**B.Cu 24本の短い銅箔配線（segment）**を追加。J1/J2は各7本、J3/J4は各5本。
- 線幅：0.20mm。パッドに重ねた基点は局所座標 `X=-0.200mm`、引出し終端 `X=+2.540mm`。各接点のY、ネット番号、F/B層を変えず、その同一B.Cuネットへ割り当てた。
- GND検査接点B1GND/B12GNDを含む。全て各々別ネットであり、隣の信号・GNDへ接続しない。
- 前段で延長した露出銅パッドは維持。配線禁止領域（Keepout）もそのまま維持し、禁止領域の外で配線の次の区間を引き出せる構造。
- GND外側接点Y=±2.75mmの0.2mm配線と、内側に移動済みKeepout境界Y=±3.375mmの間隔は理論上0.525mm。最も近い他のB.Cu配線との間隔は0.30mm（いずれも実寸静的照合でありDRCではない）。
- 0.2mmの配線は既存netclassクリアランス0.2mmを満たせるよう、各パッド中心からまっすぐ引き出す。

## 2. GND検査線とLED共通帰路を分離
本基板はUSB接点の導通試験治具であり、USB機器そのものではない。**USB側のGND接点を直接`BAT_NEG`へまとめることは禁止**とする。

- USB側GND接点：`SRC_J1_A1GND` / `DST_J2_A1GND` 等の**16個の独立検査ネット**。
- 8個のGND検査経路は、`BAT_POS -> Rn -> USB-C source GND test pad -> cable -> destination GND test pad -> Dn(anode) -> Dn(cathode) -> BAT_NEG` を構成。
- `BAT_NEG` はコイン電池マイナスと全24 LEDカソードだけを結ぶ**LED帰路専用ネット**。USB側のGND検査端子とは銅箔・ラベル上直接接続しない。
- `BAT_NEG` (#2) の専用B.Cu銅箔ゾーン `BAT_NEG_LED_RETURN` を追加。対象範囲 `(20.8,10.8)-(106.2,104.2)` mm、0.2mmクリアランス、0.3mm thermal parameters。電池BT1-2およびLED D1～D24のカソード側through-hole端子から接続する構想。
- このゾーンは、`B.Cu`で他ネットの接点・トラックを自動的に避けて充填されることが必須。KiCadの**ゾーン再フィル（Bキー）＋DRC検証が必要**。ゾーンソースを追加しただけでは最終的な銅接続の実証にはならない。
- 過去の独立LED24系統・抵抗24本は維持し、回路図・部品数・ピン番号は変更していない。
- 対応表 `gnd_sense_map_rev07.csv` を参照。

## 3. USB-Cケーブル側の共通GND制約
USB Type-C標準ケーブルのプラグではGNDのA1/B1/A12/B12が内部接続されるため、**4本が独立配線であっても個々の1接点の良否をLEDで保証できない**。現在のGND4灯はグループの通電可能性を参考表示するもので、4灯すべてが独立した正常確認という意味ではない。VBUS端子にも同様の内部共通化がある。これは「検査器側で全GND端子をGND面へ短絡してよい」ことを意味しない。

## 4. 検査実績と残課題
**静的確認済み**
- PCBの146パッド・全50ネットは保持。
- B.Cu 24引出し配線のネット名／ネット番号が当該接点と一致する。
- GND16接点（8ペア）ごとに抵抗R、LED Dへの対応を回路図・PCB・CSVで照合。
- GND検査ネットと`BAT_NEG`の混線なし。共通ゾーンのnet番号は2。
- 既存の16箇所のラッチKeepout領域を維持し、新規`BAT_NEG`銅箔ゾーンを追加（総ゾーン17）。

**未検証（製造承認不可）**
- KiCad 10でのネイティブERC、DRC、銅箔ゾーンの実際のフィル、未接続検査、実際の配線開始操作。
- GND線以外の全経路とBAT_POSの配線は未完成。B.Cuの24本は**各パッドからの引出しだけ**である。
- 製造時の銅箔とEdge.Cuts間の約0.17mmクリアランス、露出銅パッドの長さと機械嵌合。
- `main`への統合を行わない。

## 参考
- USB-IF Type-C 2.0 Cable Assembly Wiring（GND端子共通接続）：https://www.usb.org/sites/default/files/USB%20Type-C%20Spec%20R2.0%20-%20August%202019.pdf
- KiCad 10 PCB Editor、Keepout / Copper Zone / DRC：https://docs.kicad.org/10.0/en/pcbnew/pcbnew.html
