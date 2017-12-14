add_library(utils
        CallStack.cpp
        FileMap.cpp
        JenkinsHash.cpp
        NativeHandle.cpp
        Printer.cpp
        PropertyMap.cpp
        RefBase.cpp
        SharedBuffer.cpp
        Static.cpp
        StopWatch.cpp
        String8.cpp
        String16.cpp
        StrongPointer.cpp
        SystemClock.cpp
        Threads.cpp
        Timers.cpp
        Tokenizer.cpp
        Unicode.cpp
        VectorImpl.cpp
        misc.cpp
        )

target_include_directories(utils PUBLIC include ../include)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=gnu++11 -stdlib=libc++")
set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -std=gnu11")
target_link_libraries(utils log)
