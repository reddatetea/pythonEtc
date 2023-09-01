import time
import sys

def log(info):
    """输出日期信息"""
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()), info)
    sys.stdout.flush()

if __name__ == "__main__":
    add_message = '新增数据'
    log(add_message)
    time.sleep(1)
    update_message = '更新数据'
    log(update_message)
    time.sleep(1)
    delete_message = '删除数据'
    log(delete_message)
