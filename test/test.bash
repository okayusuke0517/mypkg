#!/bin/bash -xv
#SPDX-FileCopyrightText: 2024 Yusuke Oka
#SPDX-License-Identifier: BSD-3-Clause


dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build

source $dir/.bashrc

# ノードを直接起動
timeout 10 ros2 run mypkg hoistatuspublisher > /tmp/mypkg.log &

ros2 topic echo /game_status > /tmp/game_status.log &

cat /tmp/game_status.log | grep -E "Direction: (上|下|左|右)"

cat /tmp/game_status.log | grep 'Round: 5'

cat /tmp/game_status.log | grep -E "The day and month we are playing on: (Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday), (January|February|March|April|May|June|July|August|September|October|November|December)"
