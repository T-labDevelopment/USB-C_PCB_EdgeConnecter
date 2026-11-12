# KiCad 10 プロジェクトの開き方 — Rev.0.6

> Rev.0.6: BT1は標準`Connector_Wire`フットプリントによる外付け2線給電。基板側にCH25専用ライブラリ登録は不要です。

1. GitHubの `feature/usb-c-external-cr2032-wire-pads` ブランチからリポジトリを取得し、`verification/USB_C_Loop_Tester/` の**フォルダー構成を維持**して使用します。`verification/releases/` の従来ZIPはRev.0.6反映前の履歴版なので混同しないでください。
2. `USB_C_Loop_Tester/USB_C_Loop_Tester.kicad_pro` をKiCad 10.x安定版で開きます。
3. プロジェクトマネージャーから `.kicad_sch` と `.kicad_pcb` を開きます。
4. `sym-lib-table`、`fp-lib-table`、`USB_C_PCB_Edge.kicad_sym`、`USB_C_PCB_Edge.pretty/` を移動・削除しないでください。
5. 回路図エディターのERCを実行し、エラー・警告の件数とレポートを記録します。

CLIによるERC例（KiCad 10.x）：

```powershell
kicad-cli sch erc --severity-all --exit-code-violations -o erc_rev06.rpt USB_C_Loop_Tester.kicad_sch
```

**注意：** PCBはまだ配線0本でDRCは未実施、実機も未検証です。回路図が開けることと製造・動作可能であることは別です。

---

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

## ERC修正後の再検査（Rev.0.4）

1. `USB_C_Loop_Tester.kicad_pro` を開き、回路図エディターでERCを再実行してください。
2. レポートに残るエラー・警告の全件を新たな `.rpt` に保存し、以前の `ERC(2).rpt` と区別します。
3. 回路図は `USB_C_Test_*_NoShield` のプロジェクト専用シンボルを使います。元の製品用 `USB_C_PCB_Edge_*_NoShield` のデータは保持しています。
4. **ERC完了とPCB配線は別工程です。** PCBの配線は未実施（0本）です。
