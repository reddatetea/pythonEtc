import time

def save_html_code(html_file_name, htmlcode):
    # 在HTML文件底部追加写入日期
    htmlcode += "\n<br>\ncreated on %s" % time.ctime()
    print("save html file:", html_file_name, "on %s" % time.ctime())
    # 操作文件
    f = open(html_file_name, "w")
    f.write("%s" % htmlcode)
    f.close()

if __name__ == "__main__":
    # HTML代码
    htmlcode = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <h1>hello world</h1>
</body>
</html>
    """
    # 写入到HTML文件
    save_html_code('test.html',htmlcode)
