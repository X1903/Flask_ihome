# coding=gbk

# coding=utf-8

# -*- coding: UTF-8 -*-

from CCPRestSDK import REST
import ConfigParser

# ���ʺ�
accountSid = '8aaf07085fe2d98c015ff1fafe9f062c'

# ���ʺ�Token
accountToken = '51f33a8b2afe461eb1585f4ce5534215'

# Ӧ��Id
appId = '8aaf07085fe2d98c015ff1fafefe0633'

# �����ַ����ʽ���£�����Ҫдhttp://
serverIP = 'app.cloopen.com'

# ����˿�
serverPort = '8883'

# REST�汾��
softVersion = '2013-12-26'


# ����ģ�����
# @param to �ֻ�����
# @param datas �������� ��ʽΪ�б� ���磺['12','34']���粻���滻���� ''
# @param $tempId ģ��Id

class CCP(object):
    """�Լ���װ�ķ��Ͷ��ŵĸ�����"""
    # ������������������
    instance = None

    def __new__(cls):
        # �ж�CCP����û���Ѿ������õĶ������û�У�����һ�����󣬲��ұ���
        # ����У��򽫱���Ķ���ֱ�ӷ���
        if cls.instance is None:
            obj = super(CCP, cls).__new__(cls)

            # ��ʼ��REST SDK
            obj.rest = REST(serverIP, serverPort, softVersion)
            obj.rest.setAccount(accountSid, accountToken)
            obj.rest.setAppId(appId)

            cls.instance = obj

        return cls.instance

    def send_template_sms(self, to, datas, temp_id):
        """"""
        result = self.rest.sendTemplateSMS(to, datas, temp_id)
        # for k, v in result.iteritems():
        #
        #     if k == 'templateSMS':
        #         for k, s in v.iteritems():
        #             print '%s:%s' % (k, s)
        #     else:
        #         print '%s:%s' % (k, v)
        # smsMessageSid:ff75e0f84f05445ba08efdd0787ad7d0
        # dateCreated:20171125124726
        # statusCode:000000
        status_code = result.get("statusCode")
        if status_code == "000000":
            # ��ʾ���Ͷ��ųɹ�
            return 0
        else:
            # ����ʧ��
            return -1


if __name__ == '__main__':
    ccp = CCP()
    ret = ccp.send_template_sms("15999692363", ["1234", "5"], 1)
    print(ret)
