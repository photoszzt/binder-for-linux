add_library(cutils
    config_utils.c
    fs_config.cpp
    canned_fs_config.c
    hashmap.c
    iosched_policy.c
    load_file.c
    native_handle.c
    open_memstream.c
    record_stream.c
    sched_policy.cpp
    sockets.cpp
    strdup16to8.c
    strdup8to16.c
    strlcpy.c
    threads.c
    android_get_control_file.cpp
    fs.c
    multiuser.c
    socket_inaddr_any_server_unix.c
    socket_local_client_unix.c
    socket_local_server_unix.c
    socket_network_client_unix.c
    sockets_unix.cpp
    str_parms.c
    ashmem-host.c
    trace-host.c
    )

target_include_directories(cutils PUBLIC include ../include)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")
set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -std=gnu11")
