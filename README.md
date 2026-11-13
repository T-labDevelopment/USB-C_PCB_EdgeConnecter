# USB-C PCBエッジ導通検証基板 Rev.0.7（Windows短パス配布版）

## この配布版の目的

WindowsのZIP展開エラー `0x80010135` （パスが長すぎる）を防ぐため、現行KiCadプロジェクトのファイルのみを最上位へ配置したGit管理版です。

- Gitブランチ：`pkg-r07`
- 元データ：`feature/usb-c-rev07-inboard-contact-extensions`（2026-11-13）
- **旧バッテリーホルダー用 `BatteryHolder_COMF_CH25_2032LF.kicad_mod` は現行設計で不使用のため、この配布版には含めていません。** 元リポジトリには履歴が残っています。
- 現行の外付けCR2032電池は標準KiCadフットプリント `Connector_Wire:SolderWire-0.25sqmm_1x02_P4.2mm_D0.65mm_OD1.7mm` を使用します。

## 開き方

1. [pkg-r07配布用ZIP](https://github.com/T-labDevelopment/USB-C_PCB_EdgeConnecter/archive/refs/heads/pkg-r07.zip) を取得。
2. できれば `C:\PCB\` 等、**短い展開先**に展開してください。
3. ZIP内最上位の `USB_C_Loop_Tester.kicad_pro` をKiCad **10.x安定版**で開いてください。
4. `USB_C_PCB_Edge.pretty/`・`USB_C_PCB_Edge.kicad_sym`・`fp-lib-table`・`sym-lib-table` はプロジェクトと同じ階層で維持します。ライブラリ参照は `${KIPRJMOD}` による相対参照です。
5. 回路図とPCBは編集可能なKiCadソースです。

## 現行回路

- 14P J1/J2、10P J3/J4の独立接点検証、LED D1～D24、抵抗 R1～R24（22kΩ）。
- 各USB-Cの48銅接点は基板内側に2.4mm延長し、外側嵌合端は保持。
- ラッチKeepoutを維持したまま、GNDと禁止領域の距離を0.5mmへ変更。
- 外付けCR2032ホルダー（基板上BT1は2線はんだ付けパッド）。
- 0.8mm公称板厚、2層、ENIG検討仕様。

## 設計状態

**PCBは配線0本です。KiCad 10のERC/DRC、実装、プラグ嵌合、銅箔-Edge.Cutsの製造公差、LED光量は未検証であり、製造用の完成データではありません。**

24個のLEDが全点灯することを正常条件とはしないでください。USB-CケーブルのVBUS/GNDの内部共通化、CC、USB2.0ケーブルのB6/B7欠落などにより、個々の接点の良否をLEDだけで保証することはできません。

最新形状の検討は `REV07_INBOARD_PAD_EXTENSION_2026-11-13.md`、過去のKeepout修正は `REV07_LATCH_KEEPOUT_ROUTING_FIX_2026-11-13.md` を参照してください。

GitHub元リポジトリ：https://github.com/T-labDevelopment/USB-C_PCB_EdgeConnecter

