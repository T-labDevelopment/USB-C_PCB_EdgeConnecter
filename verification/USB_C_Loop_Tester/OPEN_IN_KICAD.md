# KiCad 10 プロジェクトの開き方

USB-C 14P/10Pの6灯式ケーブル導通検証基板です。

1. `USB_C_Loop_Tester_KiCad10_6LED_2026-11-12.zip` を展開します。
2. 作成された `USB_C_Loop_Tester` フォルダーの `USB_C_Loop_Tester.kicad_pro` を開きます。
3. KiCad プロジェクトマネージャーから回路図またはPCBを開きます。

含まれるファイルの主な種類：
- `.kicad_pro`：プロジェクト設定
- `.kicad_sch`：回路図
- `.kicad_pcb`：PCB配置（配線未実施）
- `USB_C_PCB_Edge.kicad_sym`：専用シンボル
- `USB_C_PCB_Edge.pretty/`：14P/10P専用フットプリント
- `fp-lib-table`／`sym-lib-table`：ライブラリ登録情報
- `bom.csv`、`TEST_PROCEDURE.md`：部品表・試験手順

**注意：製造データとしては未完成です。** 17フットプリント、74パッド、16ネットの配置とネット割当のみです。銅箔配線0本・KiCad 10実動作／ERC／DRC未実施。動作／製造承認済みではありません。

電池搭載中はPCやUSB電源へ接続しないでください。無通電のe-marker非搭載パッシブC-Cケーブルのみを接続します。

## Rev.0.3の回路図

回路図はラベル接続ではなく、直接ワイヤーで電気接続しています。上段が14P、下段が10Pで、電池＋抵抗→USB-C送出端子→外部ケーブル→受け端子→LED→GND帰路の順に並べています。

PCB画面は部品位置のみ整理されており、**配線済みではありません**。KiCad 10での読み込みとERC/DRCは未検証です。
