all: binderAddInts

binderAddInts: binderAddInts.cpp
	clang++ -std=c++14 -stdlib=libc++ -o $@ -I../libs/include -I.. -L.. -DHAVE_PTHREADS -DHAVE_SYS_UIO_H -DHAVE_ENDIAN_H -DHAVE_ANDROID_OS=1 $< testUtil.c -lpthread -lbinder -lutils -lcutils -llog -lbacktrace -lunwind_local -lbase -lsafe_iop -llzma -ldemangle

clean:
	rm -f binderAddInts
