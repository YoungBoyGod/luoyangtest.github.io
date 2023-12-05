import json

dicts_list = []
def create_and_fill_dicts(change_project,change_number,chanege_branch,change_patchset_number,change_jenkins_url,change_jenkins_result):
    # 初始化一个空字典模板，键 'A'、'B' 和 'C' 的值都为 None
    dict_template = {'change_project': None, 'change_number': None, 'chanege_branch': None,'change_patchset_number':None,'change_jenkins_url' :None,'change_jenkins_result':None}
    new_dict = dict_template.copy()  
    new_dict['change_project'] = change_project
    new_dict['change_number'] = change_number
    new_dict['chanege_branch'] = chanege_branch
    new_dict['change_patchset_number'] = change_patchset_number
    new_dict['change_jenkins_url'] = change_jenkins_url
    new_dict['change_jenkins_result'] = change_jenkins_result

    dicts_list.append(new_dict)
    print(dicts_list)
    return dicts_list

def find_update_dict(change_number,change_jenkins_url,change_jenkins_result):
    for dict in dicts_list:
        if dict['change_number'] == change_number:
            dict['change_jenkins_url'] = change_jenkins_url
            dict['change_jenkins_result'] = change_jenkins_result
            print(dict)
            return dict
    return None

# save list to json file
def save_list_to_json(filename):
    # 将字典列表写入 JSON 文件
    with open(filename, 'w',encoding='utf-8') as json_file:
        json.dump(dicts_list, json_file)
        

if __name__ == "__main__":

    create_and_fill_dicts("change_project","change_number","chanege_branch","change_patchset_number","change_jenkins_url","change_jenkins_result")
    create_and_fill_dicts("change_project1","change_number1","chanege_branch1","change_patchset_number1","change_jenkins_url1","change_jenkins_result")

    find_update_dict("change_number","http://10.2.10.10:8080/job/test/1/","9888")
    print(dicts_list)
    save_list_to_json("dict.json")
    

