# KiCad 10 Rev.0.7 短パス版の開き方・GND検査

1. [pkg-r07.zip](https://github.com/T-labDevelopment/USB-C_PCB_EdgeConnecter/archive/refs/heads/pkg-r07.zip) をダウンロード。
2. `C:\PCB\` など短いパスに展開。ZIP最上位にある `USB_C_Loop_Tester.kicad_pro` をKiCad 10.x安定版で開く。
3. `USB_C_PCB_Edge.pretty/`、`USB_C_PCB_Edge.kicad_sym`、`fp-lib-table`、`sym-lib-table` は同梱のまま配置。旧CH25電池ホルダー用フットプリントは現行基板で不使用のため同梱していません。
4. PCBエディタでB.Cuを表示し、J1～J4の24個のB.Cuパッドから0.20mmの配線が引き出されていることを確認。
5. **Bキーを押して銅箔ゾーンの再フィル**を実行。B.Cuの`BAT_NEG_LED_RETURN`がBT1-2とD1～D24のカソード端子（パッド1）に接続され、USB側のGND接点にはつながらないことを調べる。
6. 回路図ERC／PCB DRCを実行し、残る未接続・クリアランス等の違反を記録する。

KiCad CLIの検査例（未実行の参考コマンド）:

```powershell
kicad-cli sch erc --severity-all --exit-code-violations -o erc_rev07.rpt USB_C_Loop_Tester.kicad_sch
kicad-cli pcb drc --severity-all --exit-code-violations -o drc_rev07.rpt USB_C_Loop_Tester.kicad_pcb
```

**回路はまだ未配線部分が多く、動作・製造可能な完成版ではありません。** 2端子外付けCR2032だけを使用し、PC・USB充電器と通電接続しないこと。

設計詳細：`REV07_BCU_GND_ESCAPE_FIX_2026-11-13.md` と `gnd_sense_map_rev07.csv`。
