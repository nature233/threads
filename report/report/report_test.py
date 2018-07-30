#-*- coding: utf-8 -*-

# import simulator.cabinet.signature_cabinet.common.template as template
import sys
import time
import report.template as template
def report(logs,report_name):
    # try:
        d = {}
        begintime = ''
        endtime = ''
        time = []
        x = []
        for log in logs:
            fo = open(log, 'r')
            x += fo.readlines()
        fo.close()
        if len(x) > 0:
            for line in x:
                line = line.strip()
                if len(line.split('|')) == 6:
                    time.append(line.split('|')[0])
                    name=line.split('|')[1]
                    protocol =line.split('|')[1] + '|' + line.split('|')[3]+'|'+line.split('|')[4]+'|'+line.split('|')[5]
                    data = line.split('|')[5]
                    if protocol in d.keys():
                        d[protocol] = d[protocol] + 1
                    else:
                        d[protocol] = 1
            begintime = min(time)
            endtime = max(time)

        table_tr = ''

        numfail = 0
        numsucc = 0
        use='yes'
        html = template.Template()
        i = 0
        for key in d:
            print('-----------------------------',key.split('|')[3])
            if key.split('|')[2] == 'p_Unknow':
                numfail += d[key]
                use='no'
            elif str.find(key.split('|')[3],'action')==-1:
                numfail +=d[key]
                use='no'

            else:
                numsucc += d[key]
                use='yes'
            i += 1
            table_td = html.TABLE_TMPL % dict(
                id = i,
                name=key.split('|')[0],
                protocol = key.split('|')[2],
                ide = key.split('|')[1],
                count = d[key],
                use=use
            )
            table_tr += table_td

        total_str = '接收请求 %s，有效 %s，无效 %s' % (numfail + numsucc, numsucc, numfail)
        output = html.HTML_TMPL % dict(
            begintime = begintime,
            endtime = endtime,
            value = total_str,
            table_tr = table_tr,
        )

        # 生成html报告

        with open('/Users/wutong/PycharmProjects/framework/report/'+report_name+local_time()+'.html', 'wb') as f:
            f.write(output.encode('utf-8'))

def local_time():
           t = time.strftime('%Y-%m-%d-%H:%M:%S', time.localtime(time.time()))
           return t
    # except:
    #     e = sys.exc_info()
    #     print("Report ERROR:" + str(e))