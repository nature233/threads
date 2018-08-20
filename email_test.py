import smtplib
from email.mime.text import MIMEText
from dbruntest.decorator import loggerInFile



class Email_Warning(object):
    def __init__(self,subject,content):
        self.subject=subject
        self.content=content
        #Set server information
        self.mail_host = 'smtp.163.com'
        #username
        self.mail_user = 'wtwwww123456'
        #password
        self.mail_pass = 'wwwwt123'
        #the address of mail sender
        self.sender = 'wtwwww123456@163.com'
        #the address of mail recipient
        self.receivers = ['418187270@qq.com']
        self.send_message()


    @loggerInFile("/Users/wutong/PycharmProjects/framework/log/email_warning")
    def send_message(self):
        #content
        message = MIMEText(self.content,'plain','utf-8')
        message['Subject'] = self.subject
        message['From'] = self.sender
        message['To'] = self.receivers[0]

        #登录并发送邮件
        try:
            smtpObj = smtplib.SMTP()
            #连接到服务器
            smtpObj.connect(self.mail_host,25)
            #登录到服务器
            smtpObj.login(self.mail_user,self.mail_pass)
            #发送
            smtpObj.sendmail(
                self.sender,self.receivers,message.as_string())
            #退出
            smtpObj.quit()
            print('success')
        except smtplib.SMTPException as e:
            print('error',e) #打印错误
        print(message['Subject'] )
        return message['Subject']
if __name__ == '__main__':
    a='wewewewew'
    t=Email_Warning('error of connection',a)
    # e.send_message()

