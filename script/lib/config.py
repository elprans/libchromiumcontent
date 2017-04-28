#!/usr/bin/env python

import os


def get_output_dir(source_root, target_arch, component):
  return os.environ.get('CHROMIUM_BUILD_DIR')
