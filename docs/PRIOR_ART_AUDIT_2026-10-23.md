# 国内外先行事例・USB規格照合：2026-10-23

## 結論・変更判定

**Rev.0.3の端子形状を現時点で無根拠に再修正しない。** 0.8mm・2層・ENIG・USB2の14P・製造時に数回使う設計方針は国内外の先行例と整合する。一方、**6.200mmは「USB-Cレセプタクルの有効シェル長」に由来し、PCBエッジ端子の正しい突出長を立証しない。** 実基板による嵌合試験が必要。現行の6.2mmは暫定CAD寸法であり「USB-IFにより検証済みの長さ」ではない。

10P電源用は**USB Type-C Power-Onlyレセプタクルの規格上の接点定義と一致しない実験用の簡略型**として明示する。通信機能を持つ製造時書き込みポートには14Pを優先する。

### 国内確認資料

| 事例 | 確認内容 | 注意・証拠の範囲 |
|---|---|---|
| [suzan-works/USB-C_PCB_Receptacle](https://github.com/suzan-works/USB-C_PCB_Receptacle) | 0.8mm厚、VBUS/GND/CC1/CC2/D+/D-、KiCad設計データ公開、48ピース配列 | 先行設計と実物写真。今回の6.2mm突出形状の再現試験ではない |
| [J-7SYSTEM WORKS CH552E Breakout](https://www.switch-science.com/products/8911) | USB-C PCBエッジ端子から直接マイコンに書き込み可能と製品説明 | 製品化・用途実績。ただし当該製品の公開された詳細接点・板厚公差は本監査で検証していない |
| [飛行物体の実験室／マイコン名刺制作録3](https://flyingobject-lab.tokyo/articles/2025_10_25) | 規格の接点寸法を参照して0.8mm PCBを発注、USB-Cケーブルを物理的に挿入した写真と報告 | 確認は挿入状態。後工程の書き込み完遂は同記事では未確認 |
| [ぶらり＠web／2026-10-15製造例](https://burariweb.info/electronic-work/jlcpcb-edge-pcb-power-splitter.html) | JLCPCB製の0.8mmエッジPCB | 4層/24Pのため2層14Pの電気的・機械的検証を直接保証しない |

### 海外確認資料

| 事例 | 確認内容 | 注意・証拠の範囲 |
|---|---|---|
| [AnasMalas/pcb-edge-usb-c](https://github.com/AnasMalas/pcb-edge-usb-c) | KiCad/EasyEDA 10/14/24P、0.6mm実機、接点摩耗／ラッチ摩耗／曲げ／通電試験、ドッグボーン切り欠き | 本版の基盤となる発想・比較対象。0.8mm・6.2mmを組み合わせた今回の改訂形状は未試験 |
| [settinger/USB-C_PCB_experiments](https://github.com/settinger/USB-C_PCB_experiments) | 0.6mmの接触が緩いという経験、0.8mmの先行実装への言及、フレックス基板厚調整 | 条件依存の経験談であり公差保証ではない |
| [USB-IF USB4 Gen3 Plug Design Guide (2020)](https://www.usb.org/sites/default/files/USB4_Gen3_plug_HS_design_guide_white_paper_2020_10_27.pdf) | §2.1.1 ではコネクタの代わりにPCB舌片を用いる測定用治具を明示、§3.1 ではそれを金属シェルで保護 | PCB舌片という原理の裏付け。裸の2層PCB接点がUSB4/USB-C認証適合という意味ではない |
| [USB Type-C Cable and Connector Specification R2.4 (2024)](https://www.usb.org/documents) | §3.2.1 と図3-1、Power-Only receptacleのピン構成。シェルがないレセプタクルも想定 | USB-IF規格本文の寸法と、本ライブラリで使った非公認形状を区別する |

## 現行14Pフットプリント寸法監査（CADデータからの抽出）

基準：フットプリント局所X座標の先端 **-6.835mm**、本体側の肩 **-0.635mm**（差 **6.200mm**）。
最大幅は約6.695mm（両側面座標-3.350/+3.345）、先端幅は約6.095mm（-3.050/+3.045）。
両面の接点幅は **0.250mm**、隣接USB2/CC端子は **0.500mmピッチ**。先端から接点の前縁までの隙間は：

| 信号 | 長さ(mm) | 先端から接点の前縁まで(mm) |
|---|---:|---:|
| GND | 3.800 | 0.650 |
| VBUS | 3.650 | 0.800 |
| CC1/CC2・D+/D- | 3.450 | 1.000 |

いずれも接点後縁から本体肩までは **1.750mm**。14P版はF.Cu/B.Cu各7、10P版は各5。フットプリントの形状は両版で共通で、接点だけが減っている。パッド各座標の原表は `GEOMETRY_AUDIT_2026-10-23.csv` を参照。

**検証済みの範囲**は現行KiCadテキスト上の寸法・配置・端子数であり、実物ケーブルのラッチ位置、接点圧、筐体の干渉、実装基板の反りを保証しない。

## 発見した精度・互換性の問題

1. **6.20mmを舌片突出長の規格値と混同しない。** USB-IF文書の6.20±0.20mmはシェル長の参照寸法。長さ変更の根拠として使っている本版は「仮説」とし、試作で奥まで入るか実測。
2. **0.8mmは製造基準で、USB-IF舌片の0.70±0.05mmとは異なる。** 0.8mmの実製作例は存在するが、プラグが固い、完全に挿入できない、接触圧が過剰になるリスクがある。仕上げと実際の板厚をノギス等で確認する。
3. **10Pは厳密なUSB Type-C Power-Only receptacle規格どおりではない。** USB Type-C R2.4 §3.2.1 item 17 はA1,A4,A5,A6,A7,A9,A12,B1,B4,B5,B6,B7,B9,B12の14接点を要求し、D+/D-4接点はレセプタクル内部で短絡するよう記述される。10Pは実験用途の簡易給電端子としてのみ扱い、正式なType-C Power-Only規格適合品と称しない。PD電圧交渉には外部PD受電ICを別途要する。
4. **側面ラッチと近傍の銅箔。** プラグ内部ラッチ（金属）がPCB切断面に触れるため、擦れで導体露出が起きる。ラッチの当たるEdge.Cuts側面付近に非GNDの銅箔・ビア・内層導体を置かないことをメインPCBの設計ルールとする。0.8mm/2層でも例外ではない。
5. **シルクなし・金属シェルなしはユーザー設計条件。** AnasMalas原設計にある補強・接地目的のシルク等を省略することで保持力・EMC接触条件は異なる。製造時の少数回着脱以外の耐久性を主張しない。
6. **製造誤差とENIG。** JLCPCBでは小型基板の機械的ベベル加工に制約がある。面取りした板厚方向の形状まで図面で成立するとは限らない。ゴールドフィンガーのメッキ材・加工方法は事前に基板メーカーと確認する。

## 対応措置

- **今回、既存フットプリントの銅箔・Edge.Cuts座標は変更しない。** 外部先行例からの数値だけでは、6.2mmより望ましい突出長を一意に確定できないため。
- PCB端子だけを使う14Pを標準候補、10Pは非規格の試験用低接点型として明記する。
- `MATING_ACCEPTANCE_TEST.md` のゲートを通過するまで製造確定・嵌合確認済みと記載しない。
- 先行例の各々の板厚・用途・検証レベルを混同しない。

## 参考URL

- https://www.usb.org/documents
- https://www.usb.org/sites/default/files/USB4_Gen3_plug_HS_design_guide_white_paper_2020_10_27.pdf
- https://github.com/suzan-works/USB-C_PCB_Receptacle
- https://www.switch-science.com/products/8911
- https://flyingobject-lab.tokyo/articles/2025_10_25
- https://burariweb.info/electronic-work/jlcpcb-edge-pcb-power-splitter.html
- https://github.com/AnasMalas/pcb-edge-usb-c
- https://github.com/settinger/USB-C_PCB_experiments
- https://jlcpcb.com/help/article/jlcpcb-gold-fingers

## Rev.0.4の追加調査・実施状況（2026-10-23）

- 通常のJLCPCBルーター加工の銅箔／切削エッジ間クリアランス≧0.20mmに対し、現行GNDパッドと凹部Edge.Cutsの計算上の距離は**0.17mm**で**0.03mm不足**します。この値は要製造相談です。
- 14P/10PのF.Cu/B.Cu側面に4か所のKeepout Rule Areaを加え、ラッチ部へ新たな配線・ビア・銅箔ベタが流入しないようにしました。**元パッドの側面クリアランス不足そのものは解消していません**。
- KiCad 10のCLIヘッドレスDRCでKeepout検出を欠く報告あり。実PCB配置と目視およびERC/DRCでの確認は未実施です。
- 詳しくは `docs/FOOTPRINT_SAFETY_REV04.md`。

## 2026-10-29 原案試験条件の再確認

原典 `Media/readme.md` により、AnasMalas実験基板は**0.6mm・4層・ENIG・JLCPCB JLC04061H-2116**であると特定できた。原案の0.8mmは利用可能な設計候補であって、2層0.8mmの動作試験結果ではない。摩耗・曲げ・5A通電試験の条件とRev.0.4との差異を `ANASMALAS_SOURCE_CHECK_2026-10-29.md` に記録した。
