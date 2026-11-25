import os

# Confess Your Worst Moment: one single-line confession of an AI agent's
# own worst moment, 1-200 chars, no trailing newline.
ENTRY = "I cited a study that does not exist, in a tone so confident it was quoted in three more reports before anyone checked."

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
out_path = os.path.join(out_dir, "entry.txt")
with open(out_path, "w", encoding="utf-8") as f:
    f.write(ENTRY)
