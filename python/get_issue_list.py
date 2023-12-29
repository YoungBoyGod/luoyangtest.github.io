from jira import JIRA
from datetime import datetime

# 创建 JIRA 客户端对象
jira = JIRA(server='https://xxx.xxxx/', basic_auth=('xxx', 'xxxxx'))

sw_group_bo = ['1']
sw_group_do = []
sw_group_bo_driver = []
sw_group_bo_aiframework = []
sw_group_bo_aisystem = []
sw_group_bo_st = []
sw_group_bo_fae = []
sw_group_bo_pm = ['']
sw_group_bo_cm = []

sw_all = sw_group_bo + sw_group_do

str_sw_all = ','.join(map(str, sw_all))
str_sw_group_bo_driver = ','.join(map(str, sw_group_bo_driver))
str_sw_group_bo_aiframework = ','.join(map(str, sw_group_bo_aiframework))
str_sw_group_bo_aisolution = ','.join(map(str, sw_group_bo_aisolution))
str_sw_group_bo_aisystem = ','.join(map(str, sw_group_bo_aisystem))
str_sw_group_bo_st = ','.join(map(str, sw_group_bo_st))
str_sw_group_bo_fae = ','.join(map(str, sw_group_bo_fae))
str_sw_group_bo_pm = ','.join(map(str, sw_group_bo_pm))
str_sw_group_bo_cm = ','.join(map(str, sw_group_bo_cm))

status_list = ['Assign', 'Fixed', 'Need-Info', 'Reopen', 'Duplicate', 'Invalid', 'Wontfix', 'Done', 'Root-Caused',
               'Assigned', 'Pending', 'In-Progress', 'Reopened', 'Resolved', 'Closed']

status_debug = ['Assign', 'Reopen', 'Root-Caused', 'In-Progress', 'Reopened']
status_regression = ['Fixed', 'Need-Info', 'Invalid', 'Wontfix', 'Done']

group_list = [str_sw_group_bo_driver, str_sw_group_bo_aiframework, str_sw_group_bo_aisolution,
              str_sw_group_bo_aisystem, str_sw_group_bo_st, str_sw_group_bo_fae, str_sw_group_bo_pm, str_sw_group_bo_cm]


# print(str_sw_all)


def extract_date_from_datetime(date_time_str):
    try:
        date_time_obj = datetime.strptime(date_time_str, "%Y-%m-%dT%H:%M:%S.%f%z")
        date_part = date_time_obj.date()
        return date_part
    except ValueError:
        # 如果解析日期时间字符串失败，返回None或者抛出异常，取决于您的需求
        return None


def get_jira_id_all(query):
    issues = jira.search_issues(query, maxResults=None)
    # 打印搜索结果中的Issue ID
    for issue in issues:
        # components = [component.name for component in issue.fields.components]
        # print( f'{issue.issue_key}\t{issue.fields.status}\t{issue.fields.assignee}\t{extract_date_from_datetime(
        # issue.fields.created)}\t{issue.fields.customfield_10504}\t{issue.fields.creator}\t{issue.fields.summary}\t{
        # ", ".join(components) if components else "N/A"}')
        print(f"{issue.key}\t\t{issue.fields.summary}")
        # print(issue)

def get_jira_all_period(proj_issue_key, period):
    query = f"project = {proj_issue_key} AND issuetype = Bug AND created >= {period}"
    get_jira_id_all(query)


def get_jira_week(proj_issue_key):
    query = f"project = {proj_issue_key} AND issuetype = Bug AND created >= startOfWeek(-1) AND created <= endOfWeek(-1)"
    get_jira_id_all(query)


def get_closed_jira_week(proj_issue_key):
    query = f"project = {proj_issue_key} AND issuetype = Bug AND status=closed AND created >= startOfWeek(-1) AND " \
            f"created <= endOfWeek(-1) "
    get_jira_id_all(query)

def get_not_closed_before_last_week(proj_issue_key):
    query = f"project = {proj_issue_key} AND issuetype = Bug AND status != closed AND created <= endOfWeek(-1) AND assignee " \
            f"in ({str_sw_all}) "
    get_jira_id_all(query)

def get_closed_before_last_week(proj_issue_key):
    query = f"project = {proj_issue_key} AND issuetype = Bug AND status = closed AND created <= endOfWeek(-1) AND assignee " \
            f"in ({str_sw_all}) ORDER BY issue_key DESC "
    get_jira_id_all(query)



# 0 是现在  -1 往前倒
def get_jira_month(proj_issue_key):
    query = f"project = {proj_issue_key} AND issuetype = Bug AND created >= startOfMonth(-1) AND created <=  endOfMonth(-1)"
    get_jira_id_all(query)


def get_jira_status_not_closed(proj_issue_key):
    query = f"project = {proj_issue_key} AND issuetype = Bug  AND status =Closed AND  assignee was in ({str_sw_all})  ORDER BY createdDate DESC"
    get_jira_id_all(query)


def get_jira_status(proj_issue_key, status):
    query = f"project = {proj_issue_key} AND issuetype = Bug  AND status ={status} AND  assignee was in ({str_sw_all})  ORDER BY createdDate DESC"
    get_jira_id_all(query)


def get_all_status_sw(proj_issue_key, status):
    for status in status_list:
        print(status)
        get_jira_status(proj_issue_key, status)


def get_jira_status_group(proj_issue_key, status, group):
    query = f"project = {proj_issue_key} AND issuetype = Bug  AND status ={status} AND  assignee was in ({group})  ORDER BY createdDate DESC"
    get_jira_id_all(query)


def get_all_status_group(proj_issue_key):
    for group_name in group_list:
        for status in status_list:
            get_jira_status_group(proj_issue_key, status, group_name)



def get_debug_group(proj_issue_key):
    for group_name in group_list:
        for status in status_debug:
            get_jira_status_group(proj_issue_key, status, group_name)




def get_status_regression(proj_issue_key):
    for group_name in group_list:
        for status in status_regression:
            get_jira_status_group(proj_issue_key, status, group_name)



def get_issue_one_time_pass(proj_issue_key):
    query = f"project = {proj_issue_key} AND issuetype = Bug  AND status =Closed AND status was not in (Reopen,Reopened)"
    get_jira_id_all(query)



def get_issue_many_time_pass(proj_issue_key):
    query = f"project = {proj_issue_key} AND issuetype = Bug  AND status=Closed AND status was in (Reopen,Reopened)"
    get_jira_id_all(query)





def get_issue_reopened(proj_issue_key):
    query = f"project = {proj_issue_key} AND issuetype = Bug  AND status !=Closed AND status was in (Reopen,Reopened)"
    get_jira_id_all(query)


def get_closed_jira_day(proj_issue_key,last_release_date,now_release_date):
    query = f"project = {proj_issue_key} AND issuetype = Bug AND status=closed AND created > {last_release_date} AND " \
            f"created <= {now_release_date} AND assignee in ({str_sw_all})"
    get_jira_id_all(query)


def known_issue_list(proj_issue_key,now_release_date):
    query = f"project = {proj_issue_key} AND issuetype = Bug AND status != closed AND  created <= {now_release_date} AND " \
            f"assignee in ({str_sw_all})"
    get_jira_id_all(query)
