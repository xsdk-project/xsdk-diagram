TARGETS=legend.pdf xsdk.pdf xsdk-onlypkgs.pdf

all: $(TARGETS)

%.pdf: %.dot
	dot -Tpdf < $< > $@

clean:
	rm -f $(TARGETS)
