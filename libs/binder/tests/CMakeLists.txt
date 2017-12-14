add_executable(binderLibTest binderLibTest.cpp)

target_include_directories(binderLibTest PRIVATE /usr/include/libcxxabi)
target_link_libraries(binderLibTest binder utils cutils gtest pthread)
