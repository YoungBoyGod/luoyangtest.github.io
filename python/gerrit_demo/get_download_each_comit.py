import re
import subprocess
import os

def get_revision_download(workspace,proj_path,branch_name,revision_to_be_download,change_num,patchset_number):
    output_path = os.path.join(os.getcwd(), "../repo_download.log")
    command=f"cd {workspace}/{proj_path} && git pull --no-edit origin {revision_to_be_download}  --no-rebase --no-verify"
    result=subprocess.run(command,shell=True,check=False,text=True,capture_output=True)
    if "Not possible to fast-forward" in str(result):
        command1=f"cd {workspace}/{proj_path} && git reset --hard origin {branch_name}"
        result1=subprocess.run(command1,shell=True,check=False,text=True,capture_output=True)
        print(f"{change_num},{patchset_number} need to merged manually"  )
    else:
        with open(output_path, "a") as f3:
           f3.write(f"{change_num},{patchset_number}\n")  

def read_xml(workspace,xml_path, project_name, change_num,branch_name,patchset_number,revision_to_be_download):
    pattern = re.compile(r'<project path="(.*?)" name="{}" revision="{}"'.format(re.escape(project_name), re.escape(branch_name)))
    matches = []
    with open(xml_path, "r") as f:
        for line in f:
            match = pattern.search(line)
            if match:
                proj_path=match.group(1)
                matches.append(proj_path)
                with open("need_download.log", "a") as f2:
                    print(f"{proj_path},{project_name},{change_num},{branch_name},{patchset_number},{revision_to_be_download};\n")
                    f2.write(f"{proj_path},{project_name},{change_num},{branch_name},{patchset_number},{revision_to_be_download}\n")
                    get_revision_download(workspace,proj_path,branch_name,revision_to_be_download,change_num,patchset_number)
                    
    if len(matches) > 0:
        return matches
    else:
        print("no match")
        return None


if __name__ == "__main__":
    read_xml("workspace","manifest.xml","driver/bluefin_build","1234","inference","1","12345")
    