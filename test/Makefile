all: binderAddInts

binderAddInts: binderAddInts.cpp
	g++ -std=gnu++11 -o $@ -I../libs/include -I.. -L../libs -DHAVE_PTHREADS -DHAVE_SYS_UIO_H -DHAVE_ENDIAN_H -DHAVE_ANDROID_OS=1 $< testUtil.c -lpthread -lbinder

clean:
	rm -f binderAddInts
