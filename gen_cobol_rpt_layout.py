# Generate report layout for COBOL programs
def gen_report_layout(s, recctr):
    recname = f'REC{recctr}'
    fldname = ''
    fldctr = 0
    pictype = ''
    piclen = 0

    # count the number of spaces in between fields
    ctr = 0
    spc_ctrs = []
    for e in s.split(' '):
        if e == '':
            ctr += 1
        else:
            if ctr > 0:
                spc_ctrs.append(ctr + 1)
                ctr = 0
    if s[0] == ' ':
        spc_ctrs[0] -= 1

    # print the record name
    print(f'01 REC{str(recctr).zfill(4)}.')

    # for cases where there are leading spaces
    spc_idx = -1
    if s[0] == ' ':
        spc_idx += 1
        piclen = spc_ctrs[spc_idx]
        if piclen == 1:
            print(f'   05 FILLER                 PIC X     VALUE SPACES.')
        else:
            print(f'   05 FILLER                 PIC X({piclen})  VALUE SPACES.')

    for e in [item for item in s.split('  ') if item != '']:
        e = e.strip()
        # alphanumeric data
        if e.lower().startswith('x'):
            fldctr += 1
            fldname = f'FLD{str(fldctr).zfill(4)}'
            piclen = len(e)
            if piclen == 1:
                print(f'   05 {fldname}                PIC X.')
            else:
                print(f'   05 {fldname}                PIC X({piclen}).')
        # numeric data
        elif e.startswith('9'):
            fldctr += 1
            fldname = f'FLD{str(fldctr).zfill(4)}'
            if len(set(e)) == 1:  # all 9's
                piclen = len(e)
                if piclen == 1:
                    print(f'   05 {fldname}                PIC 9.')
                else:
                    print(f'   05 {fldname}                PIC 9({piclen}).')
            else:
                print(f'   05 {fldname}                PIC {e}.')
        # text literals
        else:
            fldctr += 1
            fldname = 'FILLER'
            pictype = 'X'
            piclen = len(e)
            print(f'   05 {fldname}                 PIC {pictype}({piclen})')
            print(f'      VALUE "{e}".')

        spc_idx += 1
        if spc_idx < len(spc_ctrs):
            print(f'   05 FILLER                 PIC X({spc_ctrs[spc_idx]})  VALUE SPACES.')


txt_ctr = 0
infile = open('cobol_report_layout')

for txt in infile:
    if not txt.isspace():
        txt_ctr += 1
        gen_report_layout(txt, txt_ctr)
infile.close()
