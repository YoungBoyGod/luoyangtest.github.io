from sshtunnel import SSHTunnelForwarder
import time, datetime, pymysql, json, requests
from decimal import Decimal

def split_and_quote(input_string):
    parts = input_string.split('-')

    if len(parts) == 2:
        project_issue_key, issue_number = parts
        project_issue_key = "'" + project_issue_key + "'"
        return project_issue_key, issue_number
    else:
        return None, None

def ssh_mysql(sql, method):
    # SSH 信息
    ssh_ip = '10.2.x.xx'
    ssh_port = 22  # type：int
    ssh_username = 'root'
    ssh_password = 'xxxx'
    # DB信息
    db_user = 'root'
    db_password = 'xxxx'
    db_host = '127.0.0.1'
    database = 'xxxx'

    with SSHTunnelForwarder(
            (ssh_ip, ssh_port),
            ssh_username=ssh_username,
            ssh_password=ssh_password,
            remote_bind_address=('127.0.0.1', 3306)) as server: 
                db = pymysql.connect(host=db_host,
                             port=server.local_bind_port,
                             user=db_user,
                             passwd=db_password,
                             database=database,
                             charset='utf8')
                cursor = db.cursor()

                if method == 'get':
                    cursor.execute(sql)
                    data = cursor.fetchall()
                    db.close()
                    return data

                if method == 'add':
                    cursor.execute(sql)
                    insert_id = cursor.lastrowid
                    db.commit()
                    db.close()
                    return '添加的id是:{}'.format(insert_id)

                if method == 'edit':
                    cursor.execute(sql)
                    edit_id = cursor.lastrowid
                    db.commit()
                    db.close()
                    return '更新的id是:{}'.format(edit_id)

                if method == 'del':
                    cursor.execute(sql)
                    del_id = cursor.lastrowid
                    db.commit()
                    db.close()
                    return '删除的id是{]'.format(del_id)


def get_need_info_time(issue_key):
    input_str = split_and_quote(issue_key)
    project_issue_key = input_str[0]
    issue_number = input_str[1]
    sql="xxx"
    # print(sql)
    data=ssh_mysql(sql, "get")
    # print(data)
    #json_data = json.dumps(result_as_dict)
    if len(data) == 0:
        print("no need info")
        return  None
    elif len(data) == 1:
        print("this issue may not closed")
        return  None
    else:
        sorted_data = sorted(data, key=lambda x: (x[0], x[1])) 
        # 计算两两相减的平均值和综合
        differences = [sorted_data[i + 1][1] - sorted_data[i][1] for i in range(0, len(sorted_data) - 1, 2)]
        # print(differences)

        # 计算平均值和综合
        average_difference = round(sum((diff.total_seconds() for diff in differences)) / len(differences) / (24 * 3600),1)
        total_difference = round(sum((diff.total_seconds() for diff in differences)) / (24 * 3600),1)
        # print("\n两两相减的结果:")
        # for diff in differences:
        #     print(diff)

        # print("\n平均值:", average_difference)
        # print("综合：", total_difference)
        result_dict={'issue_key':issue_key,'average_difference':average_difference,'total_difference':total_difference}
        return result_dict


def get_last_fixed_time(issue_key):
    input_str = split_and_quote(issue_key)
    project_issue_key = input_str[0]
    issue_number = input_str[1]
    # print(project_issue_key,issue_number)
    sql = f"xxxx"
    # print(sql)
    data=ssh_mysql(sql, "get")
    # print(data)
    if len(data) == 0:
        print("not fixed")
        return  None
    else:
        sorted_data = sorted(data, key=lambda x: (x[0], x[1])) 
        # print(sorted_data)
        last_fixed_duration = round((sorted_data[-1][-1]-sorted_data[1][-2]).total_seconds()/ (24 * 3600),1)
        result_dict={'issue_key':issue_key,'last_fixed_duration':last_fixed_duration}
        return result_dict

    

if __name__ == '__main__':
    x=get_last_fixed_time("xxxx")
    print(x)    