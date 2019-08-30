#set(COMPONENT_SRCDIRS "esp32" "extmod" "py")
set(MICROPY_PY_USSL=0)
set(MICROPY_SSL_AXTLS=0)
if(CONFIG_MICROPY_PY_USE_BTREE)
    set(MICROPY_PY_BTREE=1)
else()
    set(MICROPY_PY_BTREE=0)
endif()
set(MICROPY_FATFS = 0)

include(${CMAKE_CURRENT_LIST_DIR}/py/CMakeLists.txt)
list(TRANSFORM PYTHON_SRCS PREPEND "py/")

set(COMPONENT_SRCS_ESP32
        main.c
        uart.c
        gccollect.c
        mphalport.c
        help.c
        modutime.c
        moduos.c
        machine_timer.c
        machine_i2c.c
        machine_pin.c
        machine_touchpad.c
        machine_adc.c
        machine_dac.c
        machine_pwm.c
        machine_uart.c
        modmachine.c
        modnetwork.c
        modsocket.c
        moduhashlib.c
        mpthreadport.c
        mpsleep.c
        machine_rtc.c
        modymodem.c
        machine_ulp.c
        machine_ow.c
        modesp.c
        modconsts.c
        modmpr121.c
        moderc12864.c
        modneopixel.c
        modssd1306.c
        modeink.c
        modespnow.c
        moddisobeysamd.c
        modframebuffer.c
        modsndmixer.c
        modmpu6050.c
)
list(TRANSFORM COMPONENT_SRCS_ESP32 PREPEND "esp32/")

set(COMPONENT_SRCS_EXTMOD
        modbtree.c
)
list(TRANSFORM COMPONENT_SRCS_EXTMOD PREPEND "extmod/")

set(COMPONENT_SRCS_LIB
        mp-readline/readline.c
        netutils/netutils.c
        timeutils/timeutils.c
        utils/pyexec.c
        utils/interrupt_char.c
        utils/sys_stdio_mphal.c
)
list(TRANSFORM COMPONENT_SRCS_LIB PREPEND "lib/")

set(COMPONENT_SRCS_LIBS
        espcurl.c
        neopixel.c
        esp_rmt.c
        telnet.c
        ftp.c
        websrv.c
        libGSM.c
        curl_mail.c
        ow/owb_rmt.c
        ow/owb.c
        ow/ds18b20.c
        littleflash.c
)
list(TRANSFORM COMPONENT_SRCS_LIBS PREPEND "esp32/libs/")

set(COMPONENT_SRCS ${COMPONENT_SRCS_ESP32} ${COMPONENT_SRCS_EXTMOD} ${COMPONENT_SRCS_LIB} ${COMPONENT_SRCS_LIBS} ${PYTHON_SRCS} frozen_mpy.c)
set(COMPONENT_ADD_INCLUDEDIRS
        .
        genhdr
        py
        esp32
        lib
        lib/utils lib/mp-readline
        extmod
        extmod/crypto-algorithms
        lib/netutils
#        drivers/dht
        lib/timeutils
        lib/berkeley-db-1.xx/include
        lib/berkeley-db-1.xx/btree
        lib/berkeley-db-1.xx/db
        lib/berkeley-db-1.xx/hash
        lib/berkeley-db-1.xx/man
        lib/berkeley-db-1.xx/mpool
        lib/berkeley-db-1.xx/recno
)
set(COMPONENT_REQUIRES "bt")
register_component()

# FROZEN_MPY
function(LIST_REPLACE LIST NEWLIST REGEX NEWVALUE)
    set(outlist)
    foreach(loop_var IN LISTS ${LIST})
        string(REGEX REPLACE "${REGEX}" "${NEWVALUE}" VALUE "${loop_var}")
        list(APPEND outlist "${VALUE}")
    endforeach()
    set(${NEWLIST} ${outlist} PARENT_SCOPE)
endfunction(LIST_REPLACE)

string(STRIP "${CONFIG_INFO_HARDWARE_FOLDER}" FROZEN_MPY_SUBDIR)
set(FROZEN_MPY_DIR "${CMAKE_SOURCE_DIR}/python_modules/${FROZEN_MPY_SUBDIR}")

file(GLOB_RECURSE FROZEN_MPY_PY_FILES RELATIVE ${FROZEN_MPY_DIR} "${FROZEN_MPY_DIR}/*.py")

LIST_REPLACE(FROZEN_MPY_PY_FILES FROZEN_MPY_MPY_FILES "(.*)\\.py$" "micropython/\\1.mpy")

# TODO
set(CONFIG_PYTHON /usr/bin/python2)
set(MPY_CROSS ${COMPONENT_PATH}/mpy-cross/mpy-cross)
set(MPY_TOOL ${COMPONENT_PATH}/tools/mpy-tool.py)
set(QSTRDEFS_PRE ../../firmware/build/genhdr/qstrdefs.preprocessed.h)
set(QSTRDEFS_GEN qstrdefs.generated.h)

foreach(loop_var IN LISTS COMPONENT_ADD_INCLUDEDIRS)
    list(APPEND COMPONENT_ADD_INCLUDEDIRS_QSTRDEFS "-I ${COMPONENT_PATH}/${loop_var}")
endforeach()

add_custom_command(OUTPUT
#        qstrdefs.preprocessed.h
        ${QSTRDEFS_GEN}
##        COMMAND cat ${COMPONENT_PATH}/py/qstrdefs.h qstrdefs.collected.h | sed "s/^Q\(.*\)/\"&\"/" | ${CMAKE_C_COMPILER} -E -I$(MP_EXTRA_INC) ${CMAKE_C_FLAGS} - | sed "s/^\"\\(Q(.*)\\)\"/\\1/"
##        COMMAND cat ${COMPONENT_PATH}/py/qstrdefs.h qstrdefs.collected.h | sed "s/^Q\(.*\)/\"&\"/" | ${CMAKE_C_COMPILER} -E -I${COMPONENT_PRIV_INCLUDEDIRS} ${CMAKE_C_FLAGS} - | sed "s/^\"\\(Q(.*)\\)\"/\\1/"
#        COMMAND echo "cat ${COMPONENT_PATH}/py/qstrdefs.h | sed \"s/^Q\(.*\)/\"&\"/\" | ${CMAKE_C_COMPILER} -E ${COMPONENT_ADD_INCLUDEDIRS_QSTRDEFS} ${CMAKE_C_FLAGS} -"
        COMMAND "${CONFIG_PYTHON}" "${MPY_TOOL}" "-f" "-q" "${QSTRDEFS_PRE}" ${FROZEN_MPY_MPY_FILES} > ${QSTRDEFS_GEN}
        DEPENDS mpy_files
        VERBATIM)

add_custom_target(qstrdefs_generated DEPENDS ${QSTRDEFS_GEN})

foreach(loop_var IN LISTS FROZEN_MPY_PY_FILES)
    string(REGEX REPLACE "\\.py" ".mpy" MPY_NAME "${loop_var}")
    get_filename_component(dir "micropython/${MPY_NAME}" DIRECTORY)
    add_custom_command(OUTPUT "micropython/${MPY_NAME}"
            COMMAND mkdir -p ${dir} && "${MPY_CROSS}" "-o" "micropython/${MPY_NAME}" "${FROZEN_MPY_DIR}/${loop_var}"
            DEPENDS "${FROZEN_MPY_DIR}/${loop_var}"
            VERBATIM)
endforeach()

add_custom_target(mpy_files DEPENDS ${FROZEN_MPY_MPY_FILES})

add_custom_command(OUTPUT frozen_mpy.c
        COMMAND "${CONFIG_PYTHON}" "${MPY_TOOL}" "-f" "-q" "${QSTRDEFS_PRE}" ${FROZEN_MPY_MPY_FILES} > frozen_mpy.c
        DEPENDS mpy_files
        VERBATIM)

add_custom_target(frozen_mpy DEPENDS frozen_mpy.c)

add_dependencies(${COMPONENT_NAME} frozen_mpy)

set_property(DIRECTORY "${COMPONENT_PATH}" APPEND PROPERTY
        ADDITIONAL_MAKE_CLEAN_FILES logo.h)
