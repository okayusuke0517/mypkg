#!/bin/bash -xv
#SPDX-FileCopyrightText: 2024 Yusuke Oka
#SPDX-License-Identifier: BSD-3-Clause
dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/.bashrc
timeout 15 ros2 launch mypkg talk_listen.launch.py > /tmp/mypkg.log

cat /tmp/mypkg.log |
grep 'Received Count: 5 あっち向いてホイ'
cat /tmp/mypkg.log |
grep -E "Received Direction and today's day: (上|下|左|右) - (Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday)"
