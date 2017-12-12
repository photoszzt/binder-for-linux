all: libbinder.a

include cutils/Makefile
include utils/Makefile
include binder/Makefile

CFLAGS := -I.. -Iinclude -DHAVE_PTHREADS -DHAVE_SYS_UIO_H -DHAVE_ENDIAN_H -DHAVE_ANDROID_OS=1
CXXFLAGS := -I.. -Iinclude -DHAVE_PTHREADS -DHAVE_SYS_UIO_H -DHAVE_ENDIAN_H -DHAVE_ANDROID_OS=1 -std=gnu++11

libbinder.a: $(objects)
	ar cr $@ $^

clean:
	rm -f  libbinder.a `find -name \*.o`

%.o : %.cpp
	g++ $(CXXFLAGS) -c -o $@ $<
%.o : %.c
	gcc $(CFLAGS) -c -o $@ $<
