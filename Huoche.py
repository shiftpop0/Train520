# 爬取5.20号 13：14分的火车站点
import re

import requests

#初始化 station_str
url12306 = "https://kyfw.12306.cn/otn/resources/js/framework/station_name.js"
response = requests.get(url=url12306,  timeout=10)
station_str = response.text
datetime = "05-20"

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Host': 'www.99118.com',
    # 'If-Modified-Since': 'Mon, 25 Apr 2022 02:03:19 GMT',
    # 'If-None-Match': '"e5b79aa24858d81:0"',
    'Proxy-Connection': 'close',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36 '
}

headers_status_12306 = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'close',
    'Content-Length': '59',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'https://www.12306.cn/index/otn/index12306/queryTrainStatus',
    'Host': 'www.12306.cn',
    'Origin': 'https://www.12306.cn',
    'Referer': 'https://www.12306.cn/index/view/infos/train-query-status.html',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"'
}

headers_ticket_12306 = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'close',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': '_uab_collina=171549647915002669196159; JSESSIONID=86C71948A9EF0242F5EC775F3181990D; route=9036359bb8a8a461c164a04f8f50b252; BIGipServerotn=4074176778.24610.0000; BIGipServerportal=2949906698.17695.0000; BIGipServerpassport=921174282.50215.0000; guidesStatus=off; highContrastMode=defaltMode; cursorStatus=off; tfstk=fxLSvJc9f827dTOfKghVlLo_dW7BRLgawW1psBUz9aQ8pJdO3_CdewEvcppVeQREKyNdHCRy4z7-RH96nzWRLM7IRK6faullY2LX9Chu8_WycWOMhwJBtbfdpppCL3oq7QAl-wHNdVuwZC7-hT95pwex965RpRtYoERl-wH4gynZ5Qv6J_7IVwhfk6CLywIRwZhfZ6QLyMU8D-Bc9wBppz3YD1fhw6ULJbK_16i5EQMEEw6zycUBWtaL55bR2zY0YrabktIABiBbJ_TfNg69NU0Lhd1vuEsN0WkVkCx2es_suuQ9GHp6XpmamaOp2pjXExqf3nLk99I09PRfATtvyiNLJIdcFGxBFYZle3JfjsIYOVf2QtdkynG3HQpNFaCA0Vh6MMK2rGYrHz_9jQ7yvpmamaOp2ZsPsPWskzqIWZzCGOljGkqFcnyH3DKbNYSRi_sqGjwJxgCcGOGjGkqO2sf5BjGben1..; _jc_save_toDate=2024-05-12; _jc_save_wfdc_flag=dc; _jc_save_fromStation=%u6606%u660E%2CKMM; _jc_save_toStation=%u695A%u96C4%2CCUM; _jc_save_fromDate=2024-05-20',
    'Host': 'kyfw.12306.cn',
    'If-Modified-Since': '0',
    'Referer': 'https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}


def homepage():
    url = "http://www.99118.com/huoche/zhan/"
    try:
        response = requests.get(url=url, headers=headers, timeout=10)
    except Exception as e:
        res = ""
        print("Exception homepage:", end=" ")
        print(e)
    else:
        res = response.text
        # print(res)
    hlist = []
    str1 = "<a href='"
    index = 0
    while True:
        index = res.find(str1, index)
        if index == -1:
            break
        index2 = res.find("'>", index)
        tmp_str = res[index + len(str1): index2]
        # print(tmp_str)
        hlist.append(tmp_str)
        index = index2
    print(len(hlist))
    return hlist


def shai_cha():
    #找出所有站点的url
    list2 = []
    hlist = homepage()
    # for hstr in hlist:
    i = 0
    while i < len(hlist):
        url = 'http://www.99118.com' + hlist[i]
        try:
            response = requests.get(url=url, headers=headers, timeout=10)
        except Exception as e:
            print("Exception shai_cha:", end=" ")
            print(e)
            continue
        else:
            res = response.text
            i += 1
        str1 = "13:14"
        index = res.find(str1, 0)
        if index != -1:
            list2.append(url)
            # print(i, end="  ")
            print(url)
    # 手动复制导出到shai_cha_huoche.txt
    print(len(list2))


def read_txt(filepath):
    alist = []
    with open(filepath, 'r', encoding='UTF-8') as file:
        for line in file:
            str1 = line.strip()
            if 'Exception' in str1:
                continue
            alist.append(str1)
            # print(str1)
    return alist


def chai_cha_1314():
    #找出1314站点的车次
    alist = read_txt('./txt/shai_cha_huoche.txt')
    i = 0
    blist = []
    while i < len(alist):
        url = alist[i]
        try:
            response = requests.get(url=url, headers=headers, timeout=4)
            # print(response.apparent_encoding)
            response.encoding = 'gb2312'
        except Exception as e:
            print("Exception cha_status:", end=" ")
            print(e)
            continue
        else:
            res = response.text
            i += 1
        str1 = "13:14"
        index = 0
        while True:
            index1314 = res.find(str1, index + 1)
            if index1314 == -1:
                break
            tmp_list = []
            td_index = res.rfind('<td height=', index, index1314)
            if td_index == -1:
                index = index1314
                continue

            # 车次
            a1_index = res.find("htm'>", td_index, index1314) + len("htm'>")
            a2_index = res.find('</a>', a1_index, index1314)
            che_ci = res[a1_index:a2_index]
            tmp_list.append(che_ci)

            # 始发
            a1_index = res.find("htm'>", a2_index) + len("htm'>")
            a2_index = res.find('</a>', a1_index, index1314)
            shi_fa = res[a1_index:a2_index]
            tmp_list.append(shi_fa)

            # 经过，查询站
            jg1_index = res.find("<td>", res.find("<td>", a1_index) + 1) + len("<td>")
            jg2_index = res.find("</td>", jg1_index)
            jg_zhan = res[jg1_index:jg2_index]
            tmp_list.append(jg_zhan)

            # 终点
            tr2_index = res.find('</tr>', index1314)
            a1_index = res.rfind("htm'>", a2_index, tr2_index) + len("htm'>")
            a2_index = res.find('</a>', a1_index, tr2_index)
            zhong_dian = res[a1_index:a2_index]

            # 剔除离站时间为1314的
            leave_time1_index = res.find('<td>', jg2_index)
            leave_time2_index = res.find('</td>', leave_time1_index)
            leave_time3_index = res.rfind('<td>', jg2_index, tr2_index)
            if index1314 > leave_time3_index or (leave_time1_index < index1314 < leave_time2_index):
                index = index1314
                continue

            tmp_list.append(zhong_dian)
            blist.append(tmp_list)
            for tmp_str in tmp_list:
                print(tmp_str, end=" ")
            print(url)
            index = index1314

    # 手动复制导出到checi.txt
    print(len(blist))


def cha_status():
    alist = read_txt('./txt/checi.txt')
    blist = []
    for str1 in alist:
        tmp_list = str1.split(" ")
        blist.append(tmp_list)
    i = 0
    right_list = []
    wrong_list = []
    while i < len(blist):
        station1_index = station_str.find("|" + blist[i][1] + "|") + len("|" + blist[i][1] + "|")
        station2_index = station_str.find("|" + blist[i][3] + "|") + len("|" + blist[i][3] + "|")
        url = 'https://www.12306.cn/index/view/infos/train-query-status.html'
        post_data = 'trainDate=2022' + datetime[0:2] + datetime[3:5] + '&from=' + station_str[
                                                                                  station1_index: station_str.find("|",
                                                                                                                   station1_index)] + '&to=' \
                    + station_str[station2_index:station_str.find("|", station2_index)] + '&station_train_code=' + \
                    blist[i][0]
        # try:
        #     response = requests.post(url=url, data=post_data, headers=headers_status_12306, timeout=10)
        # except Exception as e:
        #     if 'timed out' not in str(e):
        #         print("Exception cha_status:", end=" ")
        #         print(e)
        #     continue
        # else:
        #     res = response.text
        # res = res.replace('true', "True")
        # res = res.replace('false', 'False')
        # res = eval(res)
        # data = str(blist[i]) + " " + res['data']
        # print(data)
        # if res['data'] == '列车正常开行。':
        #     right_list.append(blist[i])
        #     with open('./txt/right_list.txt', "a+") as f:
        #         f.write(str(blist[i]) + '\n')
        # else:
        #     wrong_list.append(blist[i])
        #     with open('./txt/wrong_list.txt', "a+") as f:
        #         f.write(data + '\n')

        right_list.append(blist[i])
        with open('./txt/right_list.txt', "a+", encoding="UTF-8") as f:
            f.write(str(blist[i]) + '\n')
        i += 1

def qu_chong():
    # 给list去重
    alist = read_txt('./txt/right_list.txt')
    blist = []
    for str1 in alist:
        blist.append(eval(str1))
    right_set = set()
    nd_right_list = []
    for tlist in blist:
        a = len(right_set)
        right_set.add(tlist[0])
        if a == len(right_set):
            continue
        else:
            nd_right_list.append(tlist)
            print(tlist)
            # with open('./txt/right_list.txt', "a+") as f:
            #     f.write(str(tlist) + '\n')


def next_station():
    alist = read_txt('./txt/right_list.txt')
    blist = []
    for str1 in alist:
        blist.append(eval(str1))
    i = 0
    clist = []
    while i < len(blist):
        url = 'http://www.99118.com/huoche/checi/' + blist[i][0] + '.htm'

        try:
            response = requests.get(url=url, headers=headers, timeout=4)
            response.encoding = 'gb2312'
        except Exception as e:
            print("Exception cha_status:", end=" ")
            print(e)
            continue
        else:
            res = response.text
        index0 = res.find("站次", 0)
        # 先找1314站点
        index1314 = res.find("13:14", index0)
        if index1314 == -1:
            i += 1
            continue
        a2_index = res.rfind("</a>", index0, index1314)
        a1_index = res.rfind(">", index0, a2_index) + len('>')
        a = res[a1_index:a2_index]

        # 再找下一个站点
        b1_index = res.find("htm'>", index1314) + len("htm'>")
        b2_index = res.find("</a>", b1_index)
        b = res[b1_index:b2_index]

        tmp_list = [blist[i][0], a, b]
        print(tmp_list)
        with open('./txt/next_station.txt', "a+", encoding="UTF-8") as f:
            f.write(str(tmp_list) + '\n')
        clist.append(tmp_list)
        i += 1
    return clist


def sub_fun_ticket_price(tmp_dic):
    url = 'https://kyfw.12306.cn/otn/leftTicket/queryTicketPrice?train_no=' + tmp_dic['id'] + '&from_station_no=' + \
          tmp_dic['from_num'] + '&to_station_no=' + tmp_dic['to_num'] + '&seat_types=' + tmp_dic[
              'seat_type'] + '&train_date=2024-' + datetime
    while True:
        try:
            response = requests.get(url=url, headers=headers_ticket_12306, timeout=4)
            res = response.json()
        except Exception as e:
            print("Exception sub_ticket_price:")
            print(e)
            # input()
            continue
        else:
            res = res['data']
            # print("hello")
        price_str = ""
        if res.get("O") is not None:
            price_str += ("|二等座：" + res['O'].ljust(6) + "，余票" + tmp_dic['ed_seat'] + "  ").ljust(12,chr(12288))
        if res.get("A1") is not None:
            price_str += ("|硬座："+chr(12288) + res['A1'].ljust(6) + "，余票" + tmp_dic['yz_seat'] + "  ").ljust(12,chr(12288))
        if res.get("WZ") is not None:
            price_str += ("|无座："+chr(12288) + res['WZ'].ljust(6) + "，余票" + tmp_dic['wz_seat'] + "  ").ljust(12,chr(12288))
        if res.get("M") is not None:
            price_str += ("|一等座：" + res['M'].ljust(6) + "，余票" + tmp_dic['yd_seat'] + "  ").ljust(12,chr(12288))
        if res.get("A9") is not None:
            price_str += ("|商务座：" + res['A9'].ljust(6) + "，余票" + tmp_dic['sw_seat'] + "  ").ljust(12,chr(12288))
        if res.get("A3") is not None:
            price_str += ("|硬卧："+chr(12288) + res['A3'].ljust(6) + "，余票" + tmp_dic['yw_seat'] + "  ").ljust(12,chr(12288))
        tmp_dic['price'] = price_str
        return tmp_dic


def ticket_price():
    # with open('./txt/5.20_list.txt', "a+", encoding="UTF-8") as f:
    #     f.write('\n')
    alist = read_txt('./txt/next_station.txt')
    blist = []
    for str1 in alist:
        blist.append(eval(str1))
    i = 0
    all_list = []
    while i < len(blist):
        try:
            # station1_index = station_str.find("|" + blist[i][1] + "|") + len("|" + blist[i][1] + "|")
            station1_index = re.search(r'@\w+\|' + re.escape(blist[i][1]) + r'\|', station_str).end()
            # station2_index = station_str.find("|" + blist[i][2] + "|") + len("|" + blist[i][2] + "|")
            station2_index = re.search(r'@\w+\|' + re.escape(blist[i][2]) + r'\|', station_str).end()
        except Exception as e:
            i = i + 1
            continue


        cha_url = 'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2024-' + datetime + '&leftTicketDTO.from_station=' + station_str[
                                                                                                                                            station1_index:station_str.find("|",station1_index)] + '&leftTicketDTO.to_station=' + station_str[station2_index:station_str.find("|",station2_index)] + '&purpose_codes=ADULT'
        try:
            response = requests.get(url=cha_url, headers=headers_ticket_12306, timeout=10)
            res = response.json()
        except Exception as e:
            # print("Exception ticket_price:")
            # print(e)
            # input()
            # print()
            # print(cha_url)
            continue
        else:
            res = res['data']['result']
        list1 = []
        for str1 in res:
            tmp_dic = dict()
            item = str1.split("|")
            tmp_dic['id'] = item[2]
            tmp_dic['checi'] = item[3]
            tmp_dic['from_name'] = blist[i][1]
            tmp_dic['to_name'] = blist[i][2]
            tmp_dic['from_num'] = item[16]
            tmp_dic['from_time'] = item[8]
            tmp_dic['to_num'] = item[17]
            tmp_dic["ed_seat"] = item[30] if item[30] != '' else '-'
            tmp_dic["yd_seat"] = item[31] if item[31] != '' else '-'
            tmp_dic["sw_seat"] = item[32] if item[32] != '' else '-'
            tmp_dic["wz_seat"] = item[26] if item[26] != '' else '-'
            tmp_dic["yw_seat"] = item[28] if item[28] != '' else '-'
            tmp_dic["yz_seat"] = item[29] if item[29] != '' else '-'
            tmp_dic['seat_type'] = item[35]
            tmp_dic['houbu'] = item[37]
            if tmp_dic['from_time'] == "13:14":
                tmp_dic = sub_fun_ticket_price(tmp_dic)
                list1.append(tmp_dic)
                all_list.append(tmp_dic)
        if len(list1) == 0:
            print(blist[i][0], end=" ")
            if (blist[i][0] == 'D388'):
                abc = 1
        # print(list1)
        i += 1
    # all_list.sort(key=lambda x: x['price'])
    for tdic in all_list:
        str2 = (tdic['checi']).ljust(6) + (tdic['from_name'] + " " + tdic['to_name']).ljust(12, chr(12288))
        str2 += tdic['price']
        with open('./txt/' + datetime + 'list.txt', "a+", encoding="UTF-8") as f:
            f.write(str(str2) + '\n')

if __name__ == '__main__':
    # shai_cha()
    # chai_cha_1314()
    # cha_status()
    # qu_chong()
    # next_station()
    ticket_price()
    print("end")