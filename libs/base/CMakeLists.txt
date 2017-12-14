add_library(base
    file.cpp
    logging.cpp
    parsenetaddress.cpp
    quick_exit.cpp
    stringprintf.cpp
    strings.cpp
    test_utils.cpp
    chrono_utils.cpp
    errors_unix.cpp
    )

target_include_directories(base PUBLIC include)
