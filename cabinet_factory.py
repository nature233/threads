

import os
import simulator.cabinet.signature_cabinet.monitorProgram as monitorProgram
import simulator.cabinet.signature_cabinet.run as R
import simulator.cabinet.signature_cabinet.monitorProgram as T
import simulator.cabinet.huicun_cabinet.implement.frame_use as R_H
import createid
import threading
import re
import multiprocessing
import simulator.cabinet.huicun_cabinet.implement.frame_use as frame_use
import FrameworkUtils.createid_h as createid_h
import time

class Cabient_Factory(multiprocessing.Process):
       def __init__(self):
           super().__init__()
           self.spid=''
           self.hpid=''
           # self.db = m.Mysql_Helper(dbconfig={'host': '127.0.0.1',
           #                                    'port': 3306,
           #                                    'user': 'root',
           #                                    'passwd': '123456',
           #                                    'dbname': 'frameworkdb',
           #                                    'charset': 'utf8'
           #                                    })

           print('Please select the cabinet you want to test, you can also choose multiple, '
                 'please use space to separate, if you need to add a new cabinet, please enter add:all signature_cabinet,huicun_cabinet')
           str_intercabinet = input()

           cabinets = list(map(str, str_intercabinet.strip().split()))
           for c in cabinets:

               t=multiprocessing.Process(target=self.run_cabinet,args=(c,))
               t.start()

       def run_cabinet(self,cabinet):
           # print(os.getppid(), os.getpid())
           file_abs = '/Users/wutong/PycharmProjects/framework/run_log/' + cabinet + '.log'
           f = open(file_abs, 'w')
           f.write(str(os.getpid()))
           f.close()
           list_id = createid.create(1)
           if re.search(cabinet, 'signature_cabinet', re.IGNORECASE):
              print(cabinet+':'+str(os.getpid()))

              for i in list_id:
                  t = threading.Thread(target=monitorProgram.MonitorProgram(i, '/Users/wutong/PycharmProjects/framework/cabinet_logs/'+cabinet+self.local_time()+'.log').run, args=())
                  # self.list_ex.append(monitorProgram.MonitorProgram(i, '../server.log'))
                  # t.setDaemon(True)
                  t.start()
              t.join()
           elif  re.search(cabinet, 'huicun_cabinet', re.IGNORECASE):
               # file_abs = '/Users/wutong/PycharmProjects/framework/' + cabinet + '.log'
               # f = open(file_abs, 'w')
               # f.write(cabinet + ':' + str(os.getpid()))
               # f.close()
               self.hpid=os.getpid()
               list_hid=createid_h.create(2)
               for i in list_hid:
                   t = threading.Thread(
                       target=frame_use.huicun(i, '/Users/wutong/PycharmProjects/framework/cabinet_logs/'+cabinet+self.local_time()+'.log').run,
                       args=())
                   t.start()
               t.join()

       def local_time(self):
           t = time.strftime('%Y-%m-%d-%H:%M:%S', time.localtime(time.time()))
           return t




       #     if s=='1':
       #         # h=input('请选择您要模拟的协议：1. singature_cbianet 2.huicun_cabinet 3.add')
       #         # h='1'
       #         # num=input('请输入能要启动的设备数：')
       #         # num2=str(num)
       #         # num2 = 1000
       #
       #         # sql = 'select cabinet_id from cabinet limit 0,' + num
       #         # self.list_id2 = self.get_name(self.db.select_all(sql))
       #
       #
       #         # self.list_id2=crateid_h.create(num2)
       #
       #         if h=='1':
       #             self.list_ex=[]
       #
       #             self.list_pid=os.getpid()
       #             for i in self.list_id:
       #                 t=threading.Thread(target=monitorProgram.MonitorProgram(i, '../server.log').run,args=())
       #                 self.list_ex.append(monitorProgram.MonitorProgram(i, '../server.log'))
       #                 t.setDaemon(True)
       #                 t.start()
       #
       #             print('-----------------------------------over-----------------------------------------------------------')
       #             sss = input()
       #             self.close(sss)
       #
       #
       #             # self.close('stop')
       #
       #
       #
       #         elif h=='2':
       #             pass
       #             # # f=R_H.huicun('111111')
       #             # # f.start()
       #             # # print(self.list_id2)
       #             # for i in self.list_id2:
       #             #
       #             #
       #             #     f = R_H.huicun(i)
       #             #     f.start()
       #             #
       #             #     self.list_process.append(f.pid)
       #
       #     elif s=='2':
       #          pass
       #     elif s=='3':
       #         pass
       #     else:
       #         print('您的输入有误')
       #         Cabient_Factory()
       #
       #
       #
       # def run(self):
       #      mod = importlib.import_module('simulator.cabinet.signature_cabinet.run')
       #      f = inspect.getmembers(mod, inspect.isfunction)
       #      print(self.get_name(f))
       #
       #
       # # f.join()
       # def close(self,cmd=' '):
       #     #
       #     if cmd=='stop':
       #         # for m in self.list_ex:
       #         #     m.close_connection()
       #
       #
       #
       #         os.kill(self.list_pid,signal.SIGKILL)
       #         # print('colse')
       #         # # T.generate_report(self.list_id)
       #
       # def get_name(self, list1):
       #      list2 = []
       #      for a in list1:
       #          list2.append(a[0])
       #      return list2
       #      # connect to center
       #
       # # def connect_to_center(self):
       # #     try:
       # #         self.clisock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
       # #         self.clisock.connect((gl.get_value('server_ip'), gl.get_value('server_port')))
       # #         self.socks.append(self.clisock)
       # #         self.sockDes.append((self.clisock, self.ide, time.time()))
       # #         logs.logger("success connect to monitor center:" + gl.get_value('server_ip') + "(" + str(
       # #             gl.get_value('server_port')) + ")")
       # #         (nsock, nmsg) = self.handling.handling(self.clisock, self.ide + "|reg_self|000")
       # #         if len(nmsg) > 0:
       # #             self.send_message(nsock, nmsg)
       # #     except:
       # #         e = sys.exc_info()
       # #         logs.logger("connect_to_center ERROR:" + str(e))


if __name__ == '__main__':
    c=Cabient_Factory()
    # sss=input()
    # c.close(sss)

