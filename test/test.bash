#!/bin/bash -xv
#SPDX-FileCopyrightText: 2024 Yusuke Oka
#SPDX-License-Identifier: BSD-3-Clause
dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/.bashrc
timeout 10 ros2 launch mypkg talk_listen.launch.py > /tmp/mypkg.log

cat /tmp/mypkg.log |
grep -E "Round: 5, Direction: (上|下|左|右), The day we are playing: (Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday)"
cat /tmp/mypkg.log |
grep -E "Round: 10, Direction: (上|下|左|右), The day we are playing: (Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday)"
