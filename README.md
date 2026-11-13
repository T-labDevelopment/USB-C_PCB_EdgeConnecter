# USB-C PCBエッジ検証基板 Rev.0.7 — Windows短パス配布版

## 最新の修正（2026-11-13）
- **B.Cu接点24個から短い0.20mmの銅箔引出し配線を追加済み。** B1GND・B12GNDを含む。
- **LED帰路の`BAT_NEG`専用B.Cuベタを追加。** USB-CのGND検査端子には直接接続しない。
- GND検査は8経路（16接点）で、既存の対応する抵抗・LEDを維持。
- KiCadで銅箔ゾーンを再フィル（Bキー）してからDRCを実施する必要があります。**追加したゾーンの充填とERC/DRCは未検証です。**
- **未完成**：B.Cuの24本は引出し部分のみで、その他の全信号経路とBAT_POS給電配線は未配線です。製造承認済みではありません。

変更詳細：[GND・B.Cu接点引出し監査](REV07_BCU_GND_ESCAPE_FIX_2026-11-13.md)／[GND対応表](gnd_sense_map_rev07.csv)。

## Windows ZIP展開エラーへの対処

この`pkg-r07`は現行KiCadソースを最上位フォルダに格納し、不要な旧CH25電池ホルダーフットプリントと過去のZIPを除外した短パス配布専用ブランチです。

1. [pkg-r07 ZIP](https://github.com/T-labDevelopment/USB-C_PCB_EdgeConnecter/archive/refs/heads/pkg-r07.zip)をダウンロード。
2. `C:\PCB\`など短い場所に展開する。
3. 展開フォルダ直下の`USB_C_Loop_Tester.kicad_pro`をKiCad 10.x安定版で開く。
4. `USB_C_PCB_Edge.pretty/`・`USB_C_PCB_Edge.kicad_sym`・`fp-lib-table`・`sym-lib-table`はファイル階層を維持する。参照は`${KIPRJMOD}`相対パスです。

## 電気・機構構成

- J1/J2は14P USB2形状、J3/J4は実験用10P USB-Cエッジ接点形状。
- D1～D24の24個のLEDとR1～R24の22kΩ抵抗による個別接点導通表示。
- USB-Cの接点48パッドを基板内側へ2.4mm延長した形状を維持し、**その内側からB.Cu銅箔配線をさらに引出し**。
- ラッチKeepoutは16箇所、電池帰路B.Cuゾーンは1箇所。
- 電源は外付けCR2032×1、基板にはKiCad標準の2線はんだ付けパッド。
- 公称板厚0.8mm・2層・ENIG検討中。

**USB-CのGND接点を電池マイナスの銅箔面へ直接つなぐとLED検査を迂回するので禁止です。** ケーブルプラグ内部でGND・VBUSが共通化されるため、各LEDは接点1本ごとの良否を保証できません。

**残る必須事項**：すべての配線完成、KiCad 10 ERC/DRC、基板エッジ製造公差・マスク・機械嵌合・LED光量の実機確認。

Git管理の本開発作業ブランチ：`fix/usb-c-rev07-bcu-gnd-escape`。旧開発履歴は元リポジトリに維持し、`main`へは未統合。

