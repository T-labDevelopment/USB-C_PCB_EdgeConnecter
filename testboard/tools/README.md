# CH340N・LEDのPC側確認（任意）
- 必要環境: Python 3、`pyserial==3.5` (pip: `python -m pip install -r testboard/tools/requirements.txt`)。CH340Nの対応ドライバがOSで使用可能であることを別途確認する。
- このツールは**J1=14PのUSBデータ通信**のみ検査する。J2=10Pの規格準拠性、機械的嵌合、USB CCの電圧を測定しない。
- 基板の**J1だけ**をUSB 5Vで接続する。SJ1(TXD-RXD)をはんだブリッジでショートしてループバックする。J2は未接続。
- Windows例: `python testboard/tools/ch340n_loopback.py --port COM5`
- Linux例: `python3 testboard/tools/ch340n_loopback.py --port /dev/ttyUSB0`
- LED3は**RTS#の有効(LOW)/無効**をPCから3回切り替えて目視する。RTS表示はUSB接続時に自動で点灯しないため、**試験プログラム実行時のみの確認用**である。ドライバ/OSによりRTS制御に制約がある場合は記録する。
- ループバックでは定型のバイト列を送って同じ列が受け取れたことを確認し、PASS/FAILをコンソールへ表示する。実機での動作は**未検証**。
- エラーが出た場合、**USB列挙失敗**、**COMポート開けない**、**LED3が変わらない**、**UARTループバック失敗**を分けて記録する。
