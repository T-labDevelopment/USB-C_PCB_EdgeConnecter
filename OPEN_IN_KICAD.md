# KiCad 10での開き方 — Rev.0.7短パス配布

`pkg-r07` はGitHubからのダウンロード時に不要な旧版と深いディレクトリ階層を含まないようにした現行プロジェクトです。

## Windowsへの展開

1. `https://github.com/T-labDevelopment/USB-C_PCB_EdgeConnecter/archive/refs/heads/pkg-r07.zip` をダウンロード。
2. `C:\PCB\` など短いパスに展開。以前の長い `...-feature-usb-c-rev07-inboard-contact-extensions\verification\USB_C_Loop_Tester\...` は使用しない。
3. 展開フォルダー直下の `USB_C_Loop_Tester.kicad_pro` をKiCad 10.x安定版で開く。
4. `sym-lib-table`と`fp-lib-table`がプロジェクト直下にあり、シンボル/フットプリントライブラリを相対パスで参照していることを確認。

## 検証コマンド例

```powershell
kicad-cli sch erc --severity-all --exit-code-violations -o erc_rev07.rpt USB_C_Loop_Tester.kicad_sch
kicad-cli pcb drc --severity-all --exit-code-violations -o drc_rev07.rpt USB_C_Loop_Tester.kicad_pcb
```

このコマンドは実行手順であり、本配布版のERC/DRC実行結果ではありません。現在のPCBは配線0本であり、製造可能な基板ではありません。

## 旧ホルダーデータ

`BatteryHolder_COMF_CH25_2032LF.kicad_mod` はRev.0.7では不使用の旧案です。この配布版には含めず、元のGit履歴から参照可能です。外付けBT1の2線はんだ付け部には公式 `Connector_Wire:SolderWire-0.25sqmm_1x02_P4.2mm_D0.65mm_OD1.7mm` を使用しています。
