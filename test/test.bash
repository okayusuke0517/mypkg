#!/bin/bash -xv
#SPDX-FileCopyrightText: 2024 Yusuke Oka
#SPDX-License-Identifier: BSD-3-Clause
dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/.bashrc
timeout 20 ros2 launch mypkg talk_listen.launch.py > /tmp/mypkg.log

echo "==== Checking Direction ===="
cat /tmp/mypkg.log | grep -E "Direction: (上|下|左|右)"

echo "==== Checking Round ===="
cat /tmp/mypkg.log | grep 'Round: 5'

echo "==== Checking Day ===="
cat /tmp/mypkg.log | grep -E "The day we are playing: (Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday)"
