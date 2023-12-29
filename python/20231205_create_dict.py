import json
import sys
import argparse

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
    
    
    with open('dict.json', 'a',encoding='utf-8') as json_file:
        json.dump(new_dict, json_file)
        json_file.write(',\n')
        

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
def main():    
 # 根据命令行选择不同的方法，使用argpasrse模块
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--create',nargs='+', type=str, help='create dict list')
    parser.add_argument('-u', '--update',nargs='+', type=str, help='find and update dict')
    args = parser.parse_args()   
     # 根据命令行参数执行相应的方法
    if args.create:
        change_project = args.create[0]
        change_number = args.create[1]
        chanege_branch = args.create[2]
        change_patchset_number = args.create[3]
        change_jenkins_url = args.create[4]
        change_jenkins_result = args.create[5]
        print(change_project,change_number,chanege_branch,change_patchset_number,change_jenkins_url,change_jenkins_result)
        create_and_fill_dicts(change_project,change_number,chanege_branch,change_patchset_number,change_jenkins_url,change_jenkins_result)
    elif args.update:
        # change_number = args.update
        # change_jenkins_url = args.update
        # change_jenkins_result = args.update
        chanege_number = args.update[0]
        change_jenkins_url = args.update[1]
        change_jenkins_result = args.update[2]
        find_update_dict(change_number,change_jenkins_url,change_jenkins_result)
    else:
        print('No argument')

list1=[{"change_project": "aaabbba", "change_number": "abbbaaa", "chanege_branch": "abbbaaa", "change_patchset_number": "aabbbbaa", "change_jenkins_url": "aabbbbaa", "change_jenkins_result": "aabbbaa"},
{"change_project": "aaaa", "change_number": "aaaa", "chanege_branch": "aaaa", "change_patchset_number": "aaaa", "change_jenkins_url": "aaaa", "change_jenkins_result": "aaaa"}] 

# 需要把每個字典用;分隔,字典中的value用,分隔並輸出到一個文本中，輸出的格式是aaabbba,abbbaaa;aaaa,aaaa;   

if __name__ == "__main__":
   main()
    
    
    

