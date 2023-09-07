def call(build_board_type, package_path) {
    if (build_board_type == "pcie") {
        // 复制文件到指定目录
        sh "cp -a driver/gpgpu/build/sdk/include/* ${package_path}/Firmware/include"
        sh "cp -a driver/gpgpu/build/sdk/drivers/* ${package_path}/Firmware/lib"
        sh "cp -a inc/soc/* ${package_path}/Firmware/include"
        sh "cp -a lib/soc/* ${package_path}/Firmware/lib"
        sh "cp -a aiframework/aiframework_sdk_soc.tar.gz ${package_path}/Firmware/"
        sh "cp -a aiframework/tools/common/deploy_inference_soc.sh ${package_path}/Firmware/"

        // 创建目录并复制文件
        sh "mkdir -p ${package_path}/SDK/inference/"
        sh "cp -a aiframework/aiframework_sdk/host/* ${package_path}/SDK/inference/"

        // 处理其他工具文件
        // sh "mkdir -p ${package_path}/Tool/ProfilingTool"
        // sh "mkdir -p ${package_path}/Tool/EyediagramTool"
        // sh "cp -rf solution/eyediagram/build/eye*.tgz ${package_path}/Tool/EyediagramTool"
        // sh "cp -rf solution/performancesolution/electron-admin/build/Profiling_Tool*.tgz ${package_path}/Tool/ProfilingTool"

        echo "end to organize content for debug package"
    }
}


//@Library('my-shared-library') _
//import my.shared.library.copyAndOrganizeFiles
//
//pipeline {
//    agent any
//    parameters {
//        string(name: 'BUILD_BOARD_TYPE', defaultValue: '', description: 'Specify the board type to build')
//        string(name: 'PACKAGE_PATH', defaultValue: '', description: 'Specify the package path')
//        // 其他参数...
//    }
//    stages {
//        stage('Copy and Organize Files') {
//            steps {
//                script {
//                    def build_board_type = params.BUILD_BOARD_TYPE
//                    def package_path = params.PACKAGE_PATH
//
//                    // 调用脚本中的函数来执行文件复制和组织操作
//                    copyAndOrganizeFiles(build_board_type, package_path)
//                }
//            }
//        }
//        // 其他阶段...
//    }
//    post {
//        success {
//            echo '构建成功'
//        }
//        failure {
//            echo '构建失败'
//        }
//    }
//}