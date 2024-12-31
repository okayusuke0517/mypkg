# HoiStatusPublisher
![test](https://github.com/okayusuke0517/mypkg/actions/workflows/test.yml/badge.svg)

HoiStatusPublisherは、ROS2ノードで「あっち向いてホイ」のゲームステータスを１秒ごとにパブリッシュする。

## ノード

- **HoiStatusPublisher**
  - ゲームのステータスをトピックにパブリッシュするノード

## トピック一覧

- **`/game_status`**（メッセージをパブリッシュするトピック）
  - **型**: `std_msgs/String`
  - **説明**: ゲームのラウンド数、方向情報（上、下、左、右）、プレイ中の日付を含むメッセージをパブリッシュする。

## ダウンロードして移動

リポジトリをクローン
```bash
git clone https://github.com/okayusuke0517/mypkg.git
```
 
## 使用方法

1. **ノードの起動**
   ```bash
   $ros2 run mypkg HoiStatusPublisher
   ```

2. **トピックの確認**
   - 別の端末で以下を実行して、トピックのデータを確認する。
   
   メッセージ例
   ```bash
   $ros2 topic echo /game_status

   data: 'Round: 13, Direction: 上, The day we are playing: Tuesday'
   ---
   data: 'Round: 14, Direction: 上, The day we are playing: Tuesday'
   ---
   data: 'Round: 15, Direction: 下, The day we are playing: Tuesday'
   ---
   data: 'Round: 16, Direction: 左, The day we are playing: Tuesday'
   ```

## 必要なソフトウェア

- Python3
  - テスト済みバージョン：3.8.10
 
## テスト環境

- ROS2
  - ディストリビューション:Humble Hawksbill
  - OS:Ubuntu 22.04 LTS

## ライセンス

* このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます．
© 2024 Yusuke Oka* このパッケージのHoiStatusPublisher.py,test.bash以外のコードは，下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを，本人の許可を得て自身の著作としたものです．
    - https://github.com/ryuichiueda/slides_marp/tree/master/robosys2024

© 2024 Yusuke Oka

## 参照サイト

- https://atmarkit.itmedia.co.jp/ait/articles/2406/18/news024.html
- http://taustation.com/python3-random-module/
- https://ja.pymotw.com/2/string/index.html
