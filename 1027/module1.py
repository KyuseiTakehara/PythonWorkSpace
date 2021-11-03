import sys

major,minor,micro = list(sys.version_info[:3])
print(f'使用しているPythonのバージョンは{major}.{minor}.{micro}です。')
