# Copyright 2015 Google Inc.
#
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
# GYP for "dm" (Diamond Master, a.k.a Dungeon master, a.k.a GM 2).
{
    'includes': [ 'apptype_console.gypi' ],

    'targets': [{
        'target_name': 'dm',
        'type': 'executable',
        'includes': [
          'dm.gypi',
        ],
        'conditions': [
          ['skia_android_framework', {
              'libraries': [
                  '-lskia',
                  '-landroid',
                  '-lhwui',
                  '-lutils',
              ],
              'include_dirs': [
                  '../../../frameworks/base/libs/hwui/',
              ],
              'sources': [
                '../dm/DMSrcSinkAndroid.cpp',
              ],
              'dependencies': [
                'tools.gyp:android_utils',
              ],
          }],
        ],
    }]
}
