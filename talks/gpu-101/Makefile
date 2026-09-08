LATEXMK ?= latexmk
LATEXFLAGS = -lualatex -interaction=nonstopmode -halt-on-error

.PHONY: all slides notes
all: slides notes

slides:
	$(LATEXMK) $(LATEXFLAGS) gpu-101.tex

notes:
	$(LATEXMK) $(LATEXFLAGS) gpu-101-notes.tex
