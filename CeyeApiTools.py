#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   ceyeApiTools.py
@Time    :   2022/03/07 11:02:56
@Author  :   Binarytree200 
@Version :   1.1
@Desc    :   None
@Github  :   https://github.com/Binarytree200/CeyeApiTools
'''


import requests
import json
import argparse



def start():
    print("""

                          _____               ___        _   ______          __  
                         / ___/__ __ _____   / _ | ___  (_) /_  __/__  ___  / /__
                        / /__/ -_) // / -_) / __ |/ _ \/ /   / / / _ \/ _ \/ (_-<
                        \___/\__/\_, /\__/ /_/ |_/ .__/_/   /_/  \___/\___/_/___/
                                /___/           /_/                              
                                        Author:Binarytree200
                                Github:https://github.com/Binarytree200
          """)
    print ("""
使用方法:python CeyeApiTools.py -t ”你的ceye api token” -m ”你要查询的类型 DNS or HTTP” -f ”url匹配规则”
           
           """)

def cecy_id(url1):
    try:
        r = requests.get(url=url1)
        datadict = json.loads(r.text)
        str1 = datadict['data'][0]
        str3= str1['id']
        return str3,str1
    except:
        return None,None

def run_dns(str3):
    str1=str3
    id = str1['id']
    name = str1['name']
    remote_addr = str1['remote_addr']
    created_at = str1['created_at']
    return id,name,remote_addr,created_at

def run_http(str3):
    str1=str3
    id = str1['id']
    name = str1['name']
    remote_addr = str1['remote_addr']
    method = str1['method']
    user_agent = str1['user_agent']
    data = str1['data']
    content_type = str1['content_type']
    created_at = str1['created_at']
    return id,name,remote_addr,method,user_agent,data,content_type,created_at

def main():
    parser = argparse.ArgumentParser(description="ceyeApi")
    parser.add_argument("--token","-t",type=str,required=True,help='请输入token')
    parser.add_argument("--mold","-m",type=str,default='dns',help='请输入要是查询的类型 DNS or HTTP')
    parser.add_argument("--filter","-f",type=str,default='ceye.io',help='url匹配规则')
    args = parser.parse_args()
    url="http://api.ceye.io/v1/records?token=%s&type=%s&filter=%s"%(args.token,args.mold,args.filter)
    data3,str123=cecy_id(url)

    while True:
        while True:
            data,str1=cecy_id(url)
            if  data != None:
                break
        if data3!=data:
            data3=data
            if args.mold=='dns':
                id,name,remote_addr,created_at = run_dns(str1)
                print ("ID:%s\n触发地址:%s\n触发IP:%s\n触发时间:%s"%(id,name,remote_addr,created_at))
                print ("\n######################################################################################\n")
            else:
                id,name,remote_addr,method,user_agent,data,content_type,created_at = run_http(str1)
                print ("ID:%s\n触发地址:%s\n触发IP:%s\n触发方式:%s\nUA:%s,Data:%s\nContent_Type:%s\n触发时间:%s"%(id,name,remote_addr,method,user_agent,data,content_type,created_at ))
                print ("\n######################################################################################\n")
            fo = open("log.txt", "a+")
            fo.write(str(str1))
            fo.write('\n')
            fo.close()

if __name__=="__main__":
    start()
    main()