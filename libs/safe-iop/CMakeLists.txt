add_library(safe_iop
    src/safe_iop.c
    )

target_include_directories(safe_iop PUBLIC include)
set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -std=c11")
