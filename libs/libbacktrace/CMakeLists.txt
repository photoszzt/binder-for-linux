add_library(backtrace
    Backtrace.cpp
    BacktraceCurrent.cpp
    BacktracePtrace.cpp
    thread_utils.c
    ThreadEntry.cpp
    UnwindCurrent.cpp
    UnwindMap.cpp
    UnwindPtrace.cpp
    BacktraceMap.cpp
    )

target_include_directories(backtrace PRIVATE "../include" ../include/libunwind)
target_link_libraries(backtrace PUBLIC unwind_local demangle base)
