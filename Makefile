TARGETS=legend.pdf xsdk.pdf

all: $(TARGETS)

%.pdf: %.dot
	dot -Tpdf < $< > $@

clean:
	rm -f $(TARGETS)
