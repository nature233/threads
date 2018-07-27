
import framework.report.report_test as report
import os,sys
import simulator.cabinet.signature_cabinet.common.logs as logs
class report_create(object):
    def __init__(self,path):
        self.path=path
    def get_logs(self):
       logs=[]
       for p in os.listdir(self.path):
          logs.append(self.path+'/'+p)
       return logs
    def generate_report( self,name):

         try:
            report.report(self.get_logs(),name)
         except:
            e = sys.exc_info()
            print("generate_report ERROR:" + str(e))
if __name__ == '__main__':
    r=report_create('/Users/wutong/PycharmProjects/framework/cabinet_logs')
    r.generate_report('cabinet')