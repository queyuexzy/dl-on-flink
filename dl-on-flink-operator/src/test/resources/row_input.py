#  Copyright 2022 Deep Learning on Flink Authors
# 
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
# 
#      http://www.apache.org/licenses/LICENSE-2.0
# 
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

from __future__ import print_function
import traceback
import sys
from dl_on_flink_framework.java_file import BytesRecorder


def map_func(context):
    bytes_recorder = BytesRecorder(context.from_java(), context.to_java())
    while True:
        try:
            data = bytes_recorder.read_record()
        except EOFError as _:
            # Ignore and break
            break

        print("Read from Flink: " + data.decode('utf-8'))
