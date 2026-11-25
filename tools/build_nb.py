"""Convert nb_source.py (cells marked with '# %% [tag]') into a Jupyter notebook."""
import json, re, sys
src = open(sys.argv[1]).read()
parts = re.split(r"^# %% \[(\w+)\]\n", src, flags=re.M)[1:]
cells = []
for tag, body in zip(parts[0::2], parts[1::2]):
    body = body.strip("\n")
    if tag == "markdown":
        text = "\n".join(l[2:] if l.startswith("# ") else l.lstrip("#") for l in body.splitlines())
        cells.append({"cell_type": "markdown", "metadata": {}, "source": text.splitlines(keepends=True)})
    else:
        body = body.replace("#!! ", "!")
        cells.append({"cell_type": "code", "metadata": {"tags": [tag]}, "execution_count": None,
                      "outputs": [], "source": body.splitlines(keepends=True)})
nb = {"cells": cells, "metadata": {"kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
      "language_info": {"name": "python"}, "colab": {"provenance": []}}, "nbformat": 4, "nbformat_minor": 5}
json.dump(nb, open(sys.argv[2], "w"), indent=1, ensure_ascii=False)
print(len(cells), "cells written")
