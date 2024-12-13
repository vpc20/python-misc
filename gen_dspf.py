# dds = '''
#      A*****************************************************************
#      A*     FILE NAME:  CUSMST                                        *
#      A*  RELATED PGMS:  CUSMNT, SCHZIP, SCHNAM                        *
#      A* RELATED FILES:  CUSMSTL1, CUSMSTL2, CUSMSTL3 (LOGICAL FILES)  *
#      A*   DESCRIPTION:  THIS IS THE PHYSICAL FILE CUSMST. IT HAS      *
#      A*                 ONE RECORD FORMAT CALLED CUSREC.              *
#      A*****************************************************************
#      A* CUSTOMER MASTER FILE -- CUSMST
#      A          R CUSREC
#      A            CUST           5  0       TEXT('CUSTOMER NUMBER')
#      A            NAME          20          TEXT('CUSTOMER NAME')
#      A            ADDR1         20          TEXT('CUSTOMER ADDRESS')
#      A            ADDR2         20          TEXT('CUSTOMER ADDRESS')
#      A            CITY          20          TEXT('CUSTOMER CITY')
#      A            STATE          2          TEXT('CUSTOMER STATE')
#      A            ZIP            5  0       TEXT('CUSTOMER ZIP CODE')
#      A            ARBAL         10  2       TEXT('ACCOUNTS RECEIVABLE BALANCE')
# '''
#
# for e in dds.split('\n'):
#     print(e)

dspf_txt = '''
     A                                      DSPSIZ(24 80 *DS3)              
     A                                      MSGLOC(24)                      
     A                                      INDARA                          
     A                                      ERRSFL                          
     A          R DSPREC1                                                   
     A                                      CF03                            
     A                                      CF04                            
     A                                      CF12                            
     A                                  1  2'PGMNAME'                     
     A                                  1 28'Application System Name'       
     A                                      DSPATR(HI)                      
     A                                  1 71DATE                            
     A                                      EDTWRD('0  /  /  ')             
     A                                  2  2USER                            
     A                                  2 31'File Maintenance'  
     A                                      DSPATR(HI)                      
     A                                  2 71TIME                            
     A                                      EDTWRD('0  :  :  ')             
     A            MAINTMODE     15A  O  4  2COLOR(BLU)  
     A                                 23  2'F3=Exit  F4=List  F12=Cancel'   
     A                                      COLOR(BLU)                         
'''


def gen_display_file(pffilename):
    f = open('dspf.mbr', 'w')
    f.write(dspf_txt)
    f.close()
    f = open('dspf.mbr', 'a')

    row = 5
    pffile = open(pffilename)
    for line in pffile:
        if line[6:7] != '*' and line[16:17] == ' ':
            fldname = line[18:28]
            fldlen = line[29:37]
            print(fldlen)
            # flddec = line[35:37]
            print(line, end='')
            row += 1
            f.write(f"     A                                {str(row).rjust(3)}  2'{fldname.title().strip()}'\n")
            f.write(f"     A            {fldname} {fldlen}B{str(row).rjust(3)} 14\n")
            if row == 22:
                break
    pffile.close()
    f.close()


gen_display_file(r'C:\Users\vpc\As400Stuff\dds\cusmst.mbr')
