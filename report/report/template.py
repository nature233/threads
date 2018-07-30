#-*- coding: utf-8 -*-

class Template(object):
    """html report"""
    HTML_TMPL = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>SignatureCabinetReport</title>
            <link href="http://libs.baidu.com/bootstrap/3.0.3/css/bootstrap.min.css" rel="stylesheet">
            <h1 style="font-family: Microsoft YaHei">钥匙柜运行报告</h1>
            <p class='attribute'><strong>开始时间 : </strong> %(begintime)s</p>
            <p class='attribute'><strong>结束时间 : </strong> %(endtime)s</p>
            <p class='attribute'><strong>运行结果 : </strong> %(value)s</p>
            <style type="text/css" media="screen">
        body  { font-family: Microsoft YaHei,Tahoma,arial,helvetica,sans-serif;padding: 20px;}
        </style>
        </head>
        <body>
            <table id='result_table' class="table table-condensed table-bordered table-hover">
                <colgroup>
                    <col align='left' />
                    <col align='right' />
                    <col align='right' />
                    <col align='right' />
                    <col align='right' />
                    <col align='right' />
                    <col align='right' />
                </colgroup>
                <tr id='header_row' class="text-center success" style="font-weight: bold;font-size: 14px;">
                    <th>行号</th>
                    <th>柜子类别</th>
                    <th>调用协议</th>
                    <th>柜子标识</th>
                    <th>处理次数</th>
                    <th>是否有效</th>
                    
                </tr>
                %(table_tr)s
            </table>
        </body>
        </html>"""

    TABLE_TMPL = """
        <tr class='failClass warning'>
            <td>%(id)s</td>
            <td>%(name)s</td>
            <td>%(protocol)s</td>
            <td>%(ide)s</td>
            <td>%(count)s</td>
            <td>%(use)s</td>
        </tr>"""
