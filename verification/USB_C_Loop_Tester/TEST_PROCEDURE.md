# 信号別LED試験手順（設計時点、実機未実施）

## 対象

- J1/J2：14P USB-Cエッジ端子、LED D1～D4
- J3/J4：10P USB-Cエッジ端子、LED D5～D6
- 3V CR2032、22kΩ×6、低電流赤LED×6
- **e-marker非搭載・受動型で無通電のUSB-C to USB-Cケーブル**のみ使用
- この検証基板はUSB機器ではなく単純な導通治具。PCやUSB充電器は接続しない

## 判定期待値

| 14Pケーブル | 10Pケーブル | D1 VBUS | D2 CC | D3 D+ | D4 D− | D5 VBUS | D6 CC |
|---|---|---|---|---|---|---|---|
| 未接続 | 未接続 | 消灯 | 消灯 | 消灯 | 消灯 | 消灯 | 消灯 |
| 接続 | 未接続 | 点灯 | 点灯 | 点灯 | 点灯 | 消灯 | 消灯 |
| 未接続 | 接続 | 消灯 | 消灯 | 消灯 | 消灯 | 点灯 | 点灯 |
| 接続 | 接続 | 点灯 | 点灯 | 点灯 | 点灯 | 点灯 | 点灯 |

各ケーブルは両端のプラグをそれぞれ反転し、4つの向きの組み合わせで確認すること。

## 異常時の解釈

- 14P D3のみ消灯：D+経路の断線・接触不良の候補。ただし電流不足やLED故障等は除外できていない。
- 14P D4のみ消灯：D−経路の断線・接触不良の候補。
- 14Pの4灯がすべて消灯：GND共通帰路、電池、コネクター嵌合、複数信号の問題を切り分ける必要あり。**GND単独の断線確定ではない**。
- VBUSだけ消灯：VBUS群の一部/全部の断線・接触不良の可能性。ただしパッドが並列のため、1接点だけの欠落を確定できない。
- CCのみ消灯：CC導体経路、ケーブルのe-marker/VCONN構成、接点圧などを確認。**e-marker付ケーブルは本設計の対象外**。
- 点灯しても隣接信号間の短絡、低抵抗接触の品質、USB列挙・転送・書き込み成功は保証しない。

## 必須の実作業

- 基板製造前：未配線を解消し、KiCad 10 ERC/DRCを実行。
- Edge.CutsとGNDパッドのクリアランス約0.17mmについて製造メーカーと確認。
- 通電前にVBUS/GND、D+/D−などの不要な短絡がないことを実機で確認。
- CR2032挿入後は短時間の試験のみ行い、終了時に両方のケーブルを外す。
- LEDが22kΩで肉眼視認できるかを確認。視認できない場合の抵抗変更は別改版として扱う。

現在のチェック結果は設計データの静的照合のみ。実機試験・ERC/DRCは未実施。

根拠：
- USB-CのCC1/CC2・片側CC・VCONN： https://developerhelp.microchip.com/xwiki/bin/view/applications/usb/typec-features/cc-vconn-signals/
- e-markerケーブルのRa： https://www.richtek.com/Design%20Support/Technical%20Document/AN056?sc_lang=en
- CR2032公称電圧/標準連続負荷： https://energy.panasonic.com/jp/business/products/lithium/coin-cr-standard/models/CR2032
