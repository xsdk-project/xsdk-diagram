TARGETS=legend.pdf xsdk.pdf xsdk_pkgsonly.pdf

all: $(TARGETS)

%.pdf: %.dot
	dot -Tpdf < $< > $@

clean:
	rm -f $(TARGETS)
