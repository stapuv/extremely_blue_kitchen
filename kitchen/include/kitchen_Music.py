#!/usr/bin/py
# -*- coding: iso-8859-1 -*-
"""
   Copyright (C) 2010 Jef Oliver jgoliver _at_ jeago _dot_ com

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

         http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""
"""standard imports"""
import sys, os, shutil, subprocess, shlex
import __builtin__
import kitfuns

"""add your custom options here"""
playerbackground="293e66"

"""add your custom commands here"""
def custom_commands_run( apkname, apkpath, kitchenpath, apktool, smali, baksmali ):
  os.chdir(apkpath)
  kitfuns.subproc(False, apktool+" d "+apkname+".apk toold", "Could Not apktool"+apkname+".apk")
  os.chdir(os.path.join("toold", "res", "color"))
  kitfuns.fstrrep("tab_indicator_text.xml", "808080", playerbackground)
  os.chdir(os.path.join(apkpath, "toold", "res", "layout-finger"))
  kitfuns.fstrrep("audio_player_common.xml", "5a5a5a", playerbackground)
  os.chdir(apkpath)
  kitfuns.subproc(False, apktool+" b toold", "Could Not apktool"+apkname+".apk")
  os.chdir(os.path.join("toold", "dist"))
  shutil.move("out.apk", os.path.join(apkpath, "out.apk"))
  os.chdir(apkpath)
  shutil.rmtree("toold")
  kitfuns.subproc(True, "unzip -qq out.apk -d toold", "Could Not Unzip out.apk")
  os.remove("out.apk")
  shutil.move(os.path.join("toold", "res", "color", "tab_indicator_text.xml"),
              os.path.join(apkname, "res", "color", "tab_indicator_text.xml"))
  shutil.move(os.path.join("toold", "res", "layout-finger", "audio_player_common.xml"),
              os.path.join(apkname, "res", "layout-finger", "audio_player_common.xml"))
  shutil.rmtree("toold")