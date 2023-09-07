class parmUtil {

    def mySharedParameters() {
        return [
                string(name: 'BUILD_BOARD_TYPE', defaultValue: '', description: 'Specify the board type to build'),
                string(name: 'PACKAGE_PATH', defaultValue: '', description: 'Specify the package path'),
                string(name: 'TEST_CASE_PATH', defaultValue: '', description: 'Specify the test case path'),
                string(name: 'BOOT_MODE', defaultValue: 'pcie', description: 'Specify the boot mode'),
                string(name: 'BUILD_NUMBER', defaultValue: '', description: 'Specify the build number'),
                string(name: 'YY', defaultValue: '', description: 'Specify the year'),
                string(name: 'WW', defaultValue: '', description: 'Specify the week'),
                string(name: 'DD', defaultValue: '', description: 'Specify the day')
                // 添加其他参数...
        ]
    }
}

@Library('my-shared-library') _
import my.shared.library.MySharedParameters

def parameters = mySharedParameters()

//pipeline {
//    agent any
//    parameters(parameters) // 引入参数
//
//    stages {
//        stage('Create Package') {
//            steps {
//                script {
//                    def build_board_type = params.BUILD_BOARD_TYPE
//                    def package_path = params.PACKAGE_PATH
//                    def test_case_path = params.TEST_CASE_PATH
//                    def boot_mode = params.BOOT_MODE
//                    def build_number = params.BUILD_NUMBER
//                    def yy = params.YY
//                    def ww = params.WW
//                    def dd = params.DD
//
//                    // 执行 Shell 命令，将参数传递给命令
//                    sh """
//                        echo "BD400_INFERENCE_DEV_W${yy}.${ww}.${dd}_${build_board_type}_P${build_number}" > ./output/host/dl_tool_${boot_mode}_${build_board_type}/BXBM/scatter/${boot_mode}_scatter/version
//
//                        mkdir -p ${package_path}/Driver/${build_board_type}
//                        cp -rf output/host/* ${package_path}/Driver/${build_board_type}
//                        mkdir -p ${package_path}/Firmware/{include,lib,bin}
//                        cd ${package_path}/Firmware
//                        ln -s ../../Driver/${build_board_type}/dl_tool_${boot_mode}_${build_board_type}/BXBM/scatter/${boot_mode}_scatter/ dl_tool_${boot_mode}_${build_board_type}
//                        cd ${CURRENT_DIR}
//                        cp -rf output/test_case/* ${test_case_path}
//                    """
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