# -*- coding:utf-8 -*-

number = 19
tables = dict.fromkeys(range(20), 0)
fires = dict.fromkeys(range(8), 0)
peoples = dict.fromkeys(range(number), 0)
time_table = 0
time_fire = 0

p_table_img = 0

p_ready_to_table = 0
p_ready_to_fire = 0
p_fire_ing = 0
p_fire_done = 0

flag = 0 
def dis_table2():
    global p_table_img, p_ready_to_fire, peoples, flag
    if peoples.__len__():
        peoples_tmp = peoples.copy()
        for people_id, people_status in peoples_tmp.iteritems():
            if people_status == 0:
                p_table_img += 1
                peoples[people_id] += 1
            if people_status:
                peoples[people_id] += 1
                if people_status == 5:
                    p_ready_to_fire +=1
                    peoples.pop(people_id)
    else:
        flag = 1
    return p_ready_to_fire

def dis_fire():
    global p_fire_ing, p_fire_done, p_ready_to_fire, fires
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
def test(i,p_interval = 0,p_have = 0):
    global peoples, p_need_to_table
    if p_interval:
        print p_interval,'p_interval'
        peoples = {}
    else:
        peoples = dict.fromkeys(range(number), 0)
        #p_need_to_table = number
    for n in range(i):
        if p_interval:
            if not n % p_interval :
                p_have = n // p_interval
                if p_have < number:
                    #print p_have,'dfdfdf'
                    peoples[p_have] = 0
                    #p_need_to_table += 1
                    #print p_need_to_table,'fansfashfas'
        #else:
        if flag:
            print n
        dis_table2()
        dis_fire()

def result(p_interval = 0,p_have = 0):
    global peoples, p_need_to_table, flag
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
                    #print p_have,'dfdfdf'
                    peoples[p_have] = 0
                    #p_need_to_table += 1
                    #print p_need_to_table,'fansfashfas'
        #else:
        if not flag:
            dis_table2()
        dis_fire()
        n += 1
    return n


#test(5+18,6)
#n = result(1)
#print n
print p_ready_to_fire,'to fire'
print p_fire_ing, 'ing'
print p_fire_done, 'done'

print peoples
print fires