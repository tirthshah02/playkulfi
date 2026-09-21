#!/usr/bin/env python3
"""Regenerate styles.min.css from styles.css. Run after every edit to
styles.css — every HTML page links the minified file, not the source."""
import re
import pathlib

root = pathlib.Path(__file__).resolve().parent.parent
src = root / "styles.css"
out = root / "styles.min.css"

s = src.read_text()
s = re.sub(r"/\x2A.*?\x2A/", "", s, flags=re.S)  # strip /* ... */ comments
s = re.sub(r"\s+", " ", s)                        # collapse whitespace
s = re.sub(r"\s*([{}:;,])\s*", r"\1", s)          # trim around punctuation
s = re.sub(r";}", "}", s)                         # drop trailing semicolons
out.write_text(s.strip())
print(f"{src.name}: {len(src.read_text())} bytes -> {out.name}: {len(s.strip())} bytes")
