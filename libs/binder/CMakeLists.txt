add_library(binder
        AppOpsManager.cpp
        Binder.cpp
        BpBinder.cpp
        BufferedTextOutput.cpp
        Debug.cpp
        IActivityManager.cpp
        IAppOpsCallback.cpp
        IAppOpsService.cpp
        IBatteryStats.cpp
        IInterface.cpp
        IMediaResourceMonitor.cpp
        IMemory.cpp
        IPCThreadState.cpp
        IPermissionController.cpp
        IProcessInfoService.cpp
        IResultReceiver.cpp
        IServiceManager.cpp
        IShellCallback.cpp
        MemoryBase.cpp
        MemoryDealer.cpp
        MemoryHeapBase.cpp
        Parcel.cpp
        PermissionCache.cpp
        PersistableBundle.cpp
        ProcessInfoService.cpp
        ProcessState.cpp
        Static.cpp
        Status.cpp
        TextOutput.cpp
        IpPrefix.cpp
        Value.cpp
        aidl/android/content/pm/IPackageManagerNative.aidl
        )

target_include_directories(binder PUBLIC include ../include ../../)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11 -stdlib=libc++")
set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -std=gnu11")

add_subdirectory(tests)
