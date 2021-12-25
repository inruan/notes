from __future__ import print_function

def get_cmd_ret(cmd):
    import os, subprocess
    sp = subprocess.Popen(cmd,
                          shell=True,
                          stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE,
                          bufsize=-1)
    r = sp.stdout.read().decode().strip()
    return r or ''

def trans_md(__filename):
    import io, re
    # commands.ge
    # __filename = 'python.md'
    alltext = io.open(__filename, encoding='utf8').read()
    # print(text)
    codes = re.findall('```python[^`]*```', alltext, re.MULTILINE)
    codefile = 'tmp.py'
    for rawcode in codes:
        code = rawcode.replace('```python', '').replace('```', '').strip()
        # print('---code---')
        # print(code)
        # print('---end----')
        with io.open(codefile, encoding='utf8', mode='w') as f:
            f.write(code)
        out = get_cmd_ret('python %s' % codefile)
        # print(out)
        alltext = alltext.replace(rawcode, rawcode + '\n\n 输出:\n\n```\n%s\n```\n' % out)
    import os
    if os.path.exists(codefile):
        os.remove(codefile)

    alltext = '<!-- 该文件由"%s"文件编译生成请勿直接编辑 -->\n' % __filename + alltext
    io.open(__filename.replace('.md', '-out.md'), encoding='utf8', mode='w').write(alltext)

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2:
        print('useage: python %s file' % sys.argv[0])
        exit(1)
    trans_md(sys.argv[1])