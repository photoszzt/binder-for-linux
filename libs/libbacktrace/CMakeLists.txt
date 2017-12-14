add_library(backtrace
    Backtrace.cpp
    BacktraceCurrent.cpp
    BacktracePtrace.cpp
    thread_utils.c
    ThreadEntry.cpp
    UnwindCurrent.cpp
    UnwindMap.cpp
    UnwindPtrace.cpp)

target_include_directories(backtrace PRIVATE "../include")

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")
