class BuildType {
    static def buildSoc(selectedBoardTypes = ['pcie', 'evb', 'slt', 'fpga']) {
        echo "Building board types: ${selectedBoardTypes.join(', ')}"

        // 在这里使用 selectedBoardTypes 来执行构建操作
    }
}
class MySharedLibrary {
    static def buildBoardType(buildType='debug', boardType, product,bld_flow="driver") {
        def commands = []
        if boardType=="pcie":
        // 构建 host
            commands << "make BLD_TARGET=host BLD_TYPE=${buildType} BOARD_TYPE=${boardType} PRODUCT=${product}"

        // 构建 soc
            commands << "make BLD_TARGET=soc BLD_TYPE=${buildType} BOARD_TYPE=${boardType} PRODUCT=${product}"
        else:
            commands << "make BLD_TARGET=host BLD_TYPE=${buildType} BOARD_TYPE=${boardType} PRODUCT=${product} BLD_FLOW={bld_flow}"

        // 构建 soc
             commands << "make BLD_TARGET=soc BLD_TYPE=${buildType} BOARD_TYPE=${boardType} PRODUCT=${product} BLD_FLOW={bld_flow}"

        return commands
    }
}


//pipeline {
//    agent any
//    parameters {
//        choice(name: 'SELECTED_BOARD_TYPES', choices: 'pcie\nevb\tslt\tfpga', description: 'Select BOARD_TYPES to compile', multiSelect: true)
//    }
//    stages {
//        stage('Build SOC') {
//            steps {
//                script {
//                    def selectedBoardTypes = params.SELECTED_BOARD_TYPES ?: ['pcie', 'evb', 'slt', 'fpga']
//
//                    MySharedLibrary.buildSoc(selectedBoardTypes)
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