class GitUtil {

    static initRepo(String manifestUrl, String branch, String manifestFile) {
        sh """
            /opt/tools/git-repo/repo init \\
            -u ${manifestUrl} \\
            -b ${branch} \\
            -m ${manifestFile} \\
            --current-branch --submodules
        """
    }
    staic syncRepo(){
        sh "/opt/tools/git-repo/repo sync -d -c -q"
    }

    static checkoutBranch(String branchName) {
        sh "git checkout ${branchName}"
    }

    static addFile(String filePath) {
        sh "git add ${filePath}"
    }

    static commitChanges(String commitMessage) {
        sh "git commit -m '${commitMessage}'"
    }

    static getCommitLogs() {
        return sh(script: 'git log --oneline', returnStatus: true).trim()
    }

    static cloneRepository(String remoteUrl) {
        sh "git clone ${remoteUrl} ."
    }
}

// 生成manifest文件
    static generateManifest(String repoTool, String outputDir, String manifestName){

    sh "${repoTool} manifest -o ${outputDir}/${manifestName} -r"

}
// 使用方式:

GitUtil.initRepo(
        "ssh://swsupport@10.2.24.143:29418/manifest",
        "master",
        "toolchain.xml"
)

GitUtil.checkoutBranch("feature-branch")

GitUtil.cloneRepository("https://github.com/yourusername/yourrepository.git") // 克隆另一个仓库到当前工作区

GitUtil.addFile("path/to/your/file.txt")

GitUtil.commitChanges("Add a new file")

def commitLogs = GitUtil.getCommitLogs()
echo "提交记录:\n${commitLogs}"


def repoTool = "/opt/tools/git-repo/repo"
def outputDir = "manifests"
def manifestName = "mymanifest.xml"

GitUtil.generateManifest(outputDir, manifestName)