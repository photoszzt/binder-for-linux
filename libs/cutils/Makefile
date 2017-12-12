cutils_sources := \
	ashmem-dev.c \
	ashmem-host.c \
    hashmap.c \
    iosched_policy.c \
    load_file.c \
	native_handle.c \
	properties.c \
	safe_iop.c \
	socket_inaddr_any_server_unix.c \
	socket_local_client_unix.c \
	socket_local_server_unix.c \
    socket_network_client_unix.c \
    str_parms.c \
    open_memstream.c \
    record_stream.c \
	sockets.c \
    strdup8to16.c \
    strdup16to8.c \
	strlcpy.c \
	threads.c

cutils_cpp_sources := \
	sockets_unix.cpp \
    sched_policy.cpp \

objects += $(patsubst %.c,cutils/%.o, $(cutils_sources))
objects += $(patsubst %.cpp,cutils/%.o, $(cutils_cpp_sources))
