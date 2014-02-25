# -*- coding: utf-8 -*-
import sys
import json

print json.dumps(json.loads(sys.stdin.read()), sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False)

