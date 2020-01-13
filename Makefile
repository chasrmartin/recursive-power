# recursive power
all: rpow rpowOlg2
rpow: rpow.o main.o
	cc -o rpow main.o rpow.o
rpowOlg2: rpowOlg2.o main.o
	cc -o rpowOlg2 rpowOlg2.o main.o
rpow.o: rpow.c
	cc -c rpow.c
rpowOlg2.o: rpowOlg2.c
	cc -c rpowOlg2.c
clean:
	rm -f rpow rpowOlg2 *.o *.pdf *.tex
