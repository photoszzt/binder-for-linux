add_library(log
    config_read.c
    config_write.c
    local_logger.c
    log_event_list.c
    log_event_write.c
    log_ratelimit.cpp
    logger_lock.c
    logger_name.c
    logger_read.c
    logger_write.c
    logprint.c
    stderr_write.c
    fake_log_device.c
    fake_writer.c
    )

target_compile_definitions(log PRIVATE -DFAKE_LOG_DEVICE=1)

target_include_directories(log PUBLIC include ../include)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11 -stdlib=libc++")
set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -std=gnu11")
