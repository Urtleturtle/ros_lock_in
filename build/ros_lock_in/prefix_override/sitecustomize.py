import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/andywang/auvc_ws/src/ros_lock_in/install/ros_lock_in'
