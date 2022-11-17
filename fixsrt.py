import pysrt
import glob

srt_files = glob.glob('en.srt')

for f in srt_files:
    subs = pysrt.open(f)
    print("Fixing ", f)
    for sub in subs:
        if sub.text == '':
            sub.text = ' '
    subs.save(f, encoding='utf-8')