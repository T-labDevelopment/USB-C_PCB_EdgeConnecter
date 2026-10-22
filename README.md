# USB-C PCB Edge / KiCad 10.x / Rev 0.1

KiCad 10.x用のPCB一体型USB-Cレセプタクル・ライブラリです。**試作・未検証**です。完成した製品では通常使用せず、ESP32の製造時ファームウェア書き込み、および必要に応じた簡易給電に使うことを想定します。

## ライブラリ

| 種類 | シンボル | フットプリント |
| --- | --- | --- |
| USB 2.0書き込み用 | `USB_C_PCB_Edge_14P_USB2_NoShield` | `USB_C_Edge_14P_USB2_NoSilk` |
| 給電専用 | `USB_C_PCB_Edge_10P_Power_NoShield` | `USB_C_Edge_10P_Power_NoSilk` |

- 2層基板に対応する表裏接点。14Pは各面7接点、10Pは各面5接点。
- **コネクター反対側の取付パッド、固定穴、実装用ランドは設けない**。
- **F.SilkS/B.SilkSにコネクター外形枠を設けない**。
- `Edge.Cuts` はUSB差込部の切り欠きだけで、採用先PCBの外形と接続して閉じる必要があります。
- 基板厚は0.6mm由来の形状で、0.8mmを候補とします。実物での0.8mm適合性は未確認です。
- 金属シールド端子のないPCB端子なので、KiCad標準USB-Cシンボルの機械的なS1端子を除いた派生物です。

## KiCadへの導入

採用先のKiCadプロジェクトへ `USB_C_PCB_Edge.kicad_sym` と `USB_C_PCB_Edge.pretty/` をコピーし、`sym-lib-table` と `fp-lib-table` の登録行を**追加**してください。既存のライブラリテーブルを上書きしないでください。

このフットプリントは単独で閉じたPCB輪郭を作りません。ローカル座標の端点 **(-0.635, -4.450)** と **(-0.635, +4.445)** から採用先PCBのEdge.Cutsに接続します。ケーブル挿入端はX負方向です。

### USB2.0 14P配線

| PCB接点 | 接続 |
| --- | --- |
| A1, A12, B1, B12 | GND |
| A4, A9, B4, B9 | VBUS |
| A5 | CC1（5.1kΩでGNDへ） |
| B5 | CC2（5.1kΩでGNDへ） |
| A6, B6 | D+ |
| A7, B7 | D− |

CC1とCC2にはそれぞれ独立したRdが必要です。ESP32-S3やESP32-C6などネイティブUSB書き込み対応品向けです。初代ESP32などは別途USB-UART変換を要します。VBUSをESP32の3.3V端子へ直接接続してはいけません。

### 給電専用10P

USB2のデータ用4接点を省略し、VBUS・GND・CC1・CC2だけを設けます。5V超のUSB PD給電にはPD受電コントローラーが必要で、コントローラー内蔵CC終端と外付け抵抗の二重実装には注意してください。

## 製造・検証状態

- **KiCad 10での実読み込み、ERC、DRC、Gerber、JLCPCBでの実製造、挿抜、USB通信、PD交渉は未検証**。
- ENIGを候補とし、HASLのような厚い仕上げは避けます。端面切削公差、保持力、ラッチとの接触は試作評価が必要です。
- 通常の1.6mm厚基板へそのまま適用することはできません。
- シルクによる厚み補助を除いているため、参照した公開設計より接触保持力が低くなる可能性があります。

## ライセンスと出典

- フットプリントのPad/Edge.Cuts形状: [vasya-zh/PCB-Edge-USB-connector-KiCad-library](https://github.com/vasya-zh/PCB-Edge-USB-connector-KiCad-library)（GPL-3.0）。本版はUSB2・給電に必要な接点へ削減した派生物。
- シンボル: KiCad公式 `Connector:USB_C_Receptacle_USB2.0_14P` に由来するグラフィック、ピン・属性（CC BY-SA 4.0）。実在しない金属シールドのS1を除外。
- 設計比較資料: [AnasMalas/pcb-edge-usb-c](https://github.com/AnasMalas/pcb-edge-usb-c)（CC0-1.0）。

ソースに由来するライセンス条件と帰属表示を保持してください。詳しくは `licenses/NOTICE.txt` を参照してください。
