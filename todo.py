# -*- coding:utf-8 -*-
'''
使用有限元的思想，对时间进行细分
把时间每10s作为一个单元进行分配
=======================
分配分为两部分：
A：      dis_table2      分配吧台
B：      dis_fire        分配烧烤架
'''
#就餐人数
number = 2
#20个吧台，不使用时状态位为 0
tables = dict.fromkeys(range(20), 0)
#烧烤架可同时烧烤8个人，使用时状态位为 0
fires = dict.fromkeys(range(8), 0)
#选取食材的人，状态位为已经选取的食材个数
peoples = dict.fromkeys(range(number), 0)
#正在进行选取食材的人数
p_table_img = 0
#已经选取好5中食材，可以进行烧烤的人数
p_ready_to_fire = 0
#正在进行烧烤的人数
p_fire_ing = 0
#烧烤结束的人数
p_fire_done = 0
#吧台使用结束的标志位
flag_end_table = 0
#吧台使用的时间
time_total_table = 0
#在烧烤架等待的时间
time_wait_fire = 0

def dis_table2():
    '''
    根据需要选取食材的人(peoples)来随机分配吧台选取5中食材
    '''
    global p_table_img, p_ready_to_fire, peoples, flag_end_table
    if peoples.__len__():
        peoples_tmp = peoples.copy()
        for people_id, people_status in peoples_tmp.iteritems():
            if people_status == 0 and p_table_img < 20:
                p_table_img += 1
                peoples[people_id] += 1
            if people_status:
                peoples[people_id] += 1
                if people_status == 5:
                    p_ready_to_fire +=1
                    peoples.pop(people_id)
    else:
        #
        flag_end_table = 1
    return p_ready_to_fire

def dis_fire():
    global p_fire_ing, p_fire_done, p_ready_to_fire, fires, time_wait_fire
    if p_ready_to_fire > 8 - p_fire_ing:
        time_wait_fire += p_ready_to_fire - (8 - p_fire_ing)
    for fire_id, fire_status in fires.iteritems():
        if fire_status == 0:
            if p_ready_to_fire > 0 :
                p_fire_ing += 1
                p_ready_to_fire -= 1
                fires[fire_id] += 1
        if fire_status:
            fires[fire_id] +=1
            if fires[fire_id] == 3* 6:
                fires[fire_id] = 0
                p_fire_done += 1
                p_fire_ing -= 1
                
def time_form(n):
    return n//6, (n%6) * 10
        
#每10s分配一次
def test(i,p_interval = 0):
    global peoples, p_need_to_table
    if p_interval:
        print p_interval,'p_interval'
        peoples = {}
    else:
        peoples = dict.fromkeys(range(number), 0)
    for n in range(i):
        if p_interval:
            if not n % p_interval :
                p_have = n // p_interval
                if p_have < number:
                    peoples[p_have] = 0
        if flag:
            print n
        dis_table2()
        dis_fire()

def result(p_interval = 0,p_have = 0):
    global peoples, p_need_to_table, flag_end_table, time_total_table
    if p_interval:
        print p_interval,'p_interval'
        peoples = {}
    else:
        peoples = dict.fromkeys(range(number), 0)
        p_need_to_table = number
    n = 0
    while p_fire_done < number:
        if p_interval:
            if not n % p_interval :
                p_have = n // p_interval
                if p_have < number:
                    peoples[p_have] = 0
        if not flag_end_table:
            dis_table2()
            time_total_table = n
        dis_fire()
        n += 1
    return n


#test(5+18,6)
number = 9
n = result()
print n
print time_total_table, 'time_total_table'
print time_wait_fire, 'time_wait_fire '
print p_ready_to_fire,'to fire'
print p_fire_ing, 'ing'
print p_fire_done, 'done'

print peoples
print fires