class constants {
    enum BoardType {
        PCIE,
        EVB,
        FPGA,
        ALL
    }

    enum product {
        bf400_hpc,
        bf400_hpc_interconnect,
        bf400_training,
        bf400_securetraining,
        bf400_mslt,
        bf400_hpc_alivpx,
        bf400_hpc_kylinos,
        bf100_hpc,
        bf100cs_hpc,
        bd400_inference,
        bd400_mslt,
        bd100_inference,
        bf800_hpc,

    }

    enum Bld_target {
        soc,
        host
    }

    enum Bld_type {
        debug
    }

    enum Bld_flow {
        driver
    }

    enum Boot_mode {
        pcie,
        evb,
        fpga,
        slt
    }


}
//@Library('your-shared-library') _
//
//pipeline {
//    agent any
//
//    parameters {
//        choice(
//                name: 'BOARD_TYPE',
//                choices: constants.BoardType.values().collect { it.name() },
//                description: 'Select the board type'
//        )
//
//        choice(
//                name: 'PRODUCT',
//                choices: constants.product.values().collect { it.name() },
//                description: 'Select the product'
//        )
//
//        choice(
//                name: 'BLD_TARGET',
//                choices: constants.Bld_target.values().collect { it.name() },
//                description: 'Select the build target'
//        )
//
//        choice(
//                name: 'BLD_TYPE',
//                choices: constants.Bld_type.values().collect { it.name() },
//                description: 'Select the build type'
//        )
//
//        choice(
//                name: 'BLD_FLOW',
//                choices: constants.Bld_flow.values().collect { it.name() },
//                description: 'Select the build flow'
//        )
//
//        choice(
//                name: 'BOOT_MODE',
//                choices: constants.Boot_mode.values().collect { it.name() },
//                description: 'Select the boot mode'
//        )
//    }
//
//    stages {
//        stage('Build') {
//            steps {
//                // 在这里使用参数进行构建操作
//                sh "echo 'Selected BOARD_TYPE: \${BOARD_TYPE}'"
//                sh "echo 'Selected PRODUCT: \${PRODUCT}'"
//                sh "echo 'Selected BLD_TARGET: \${BLD_TARGET}'"
//                sh "echo 'Selected BLD_TYPE: \${BLD_TYPE}'"
//                sh "echo 'Selected BLD_FLOW: \${BLD_FLOW}'"
//                sh "echo 'Selected BOOT_MODE: \${BOOT_MODE}'"
//            }
//        }
//    }
//}
