import requests
import json
kd_dict = {1:'shentong',2:'ems',3:'shunfeng',4:'yuantong',5:'zhongtong',6:'yunda',7:'tiantian',8:'huitong',9:'quanfeng',10:'debang',11:'zhaijisong'}
while 1:
    print('请选择您的快递公司：')
    print('1.申通快递：')
    print('2.EMS邮政快递：')
    print('3.顺丰递运：')
    print('4.圆通快递：')
    print('5.中通快递：')
    print('6.韵达快递：')
    print('7.天天快递：')
    print('8.汇通快递：')
    print('9.全峰快递：')
    print('10.德邦物流：')
    print('11.宅急送：')
    num = int(input('选择您的快递公司：'))
    while num not in range(1,12):
        num = int(input('选项有误，请重选：'))
    type = kd_dict[num]
    postid = input('请输入您的快递单号：')
    url = 'http://www.kuaidi100.com/query?type=%s&postid=%s'%(type,postid)
    rs = requests.get(url)
    kd_info = json.loads(rs.text)
    msg = kd_info['message']
    if msg == 'ok':
        print('您的快递%s物流信息如下：'%postid)
        data = kd_info['data']
        for data_dict in data:
            time = data_dict['time']
            context = data_dict['context']
            print('时间：%s %s'%(time,context))
    else:
        if msg == '参数错误':
            print('您输入信息有误，请重输：')
        else:
            print(msg)

