# USB-C Loop Tester Rev.0.6 — 外付けCR2032接続 再適用監査
Date: 2026-11-12 (JST)

## 目的と範囲
「フットプリント検討」チャット最終指示である、基板直付けCH25-2032LFの撤回・外付けCR2032ホルダー2線接続への仕様変更を、GitHub上の実プロジェクトに再確認・同期する。

## 現行データ
- KiCad: 10.x 安定版を対象（本環境では実行ファイル未導入）。
- 現行設計: `USB_C_Loop_Tester.kicad_sch` / `USB_C_Loop_Tester.kicad_pcb` / `USB_C_Loop_Tester.kicad_pro`。
- 使用する標準フットプリント: `Connector_Wire:SolderWire-0.25sqmm_1x02_P4.2mm_D0.65mm_OD1.7mm`。
- PCB上のBT1原点: (76.0, 90.0)mm。パッド1 (76.0,90.0) = BAT_POS (+)、パッド2 (80.2,90.0) = BAT_NEG (-)。
- パッドは2個ともスルーホール、径1.85mm、ドリル0.85mm。端子間4.2mm。
- 電池ホルダー本体は基板外に固定し、絶縁リード2本をBT1へ半田付けする。基板上にCH25-2032LF専用フットプリントや位置決めNPTHを使用しない。
- 旧 `USB_C_Test_Parts.pretty/BatteryHolder_COMF_CH25_2032LF.kicad_mod` はGit履歴・旧案検証資料としてのみ保持され、現行PCBに配置されず `fp-lib-table` でも登録されていない。

## 同期・再確認したファイル
- `USB_C_Loop_Tester.kicad_pcb`: BT1標準フットプリント実装済みを確認、タイトルブロックをRev.0.6へ修正。
- `USB_C_Loop_Tester.kicad_sch`: BT1の正式 `Device:Battery_Cell` シンボルおよびFootprintプロパティを確認、タイトルをRev.0.6へ修正。
- `net_assigned_pads.csv`: 古い `Battery:BatteryHolder_Keystone_103_1x20mm` 表記を現行標準2線パッドに同期。
- `bom.csv`: BT1の外付け電池インターフェース名とフットプリント表記を回路図に同期。
- `README.md`, `OPEN_IN_KICAD.md`, `TEST_PROCEDURE.md`: Rev.0.6を現行として明示、旧版ZIPと旧CH25案を区別、組立安全点検を追記。

## 静的監査
GitHubの現行PCB／回路図／BOM／パッド一覧を直接再読して確認した項目。
- PCBのフットプリント数: 17。PCBの配置パッド数: 74。
- USB-C J1/J2（14P）、J3/J4（10P）の4コネクターは維持。
- LED D1～D6（6灯）、R1～R6（22kΩ各1本）を維持。
- 電気ネット: 16本＋未接続ネット0。BT1パッド1がBAT_POS、BT1パッド2がBAT_NEG。
- `CH25` / `Keystone` の電池ホルダーは現行PCBの配置フットプリントに含まれない。
- PCBの銅箔トラックセグメント数0、ビア数0。現段階で通電動作しない。
- 0.17mm程度のUSB-C端面とGND接点クリアランス問題は未解決。

## 完了判定と未実施
- **Rev.0.6のフットプリント仕様変更・データ同期: 実施済み（GitHubの作業ブランチにコミット／push）。**
- **KiCad 10 ERC / DRC: 未実施。エラー0、警告0と表示しない。**
- **PCB配線・ゾーン充填・Gerber生成・製造承認: 未実施。**
- **外部ホルダーの極性・固定、USB-C嵌合、LED視認性: 実機未検証。**
- **main統合: 未実施。**
