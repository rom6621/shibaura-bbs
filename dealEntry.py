#################################################
### Designer :
### Date :2021/06/13
###
### Purpose :
#################################################

#################################################
### Function Name :
### Designer :
### Date :
### Function:
### Return :
#################################################

### Revision :
### V1.0 : 開米, 2021.06.13
### V1.1 : 修正者名, yyyy.mm.dd 改訂モジュール名を書く
### V1.2 : 修正者名, yyyy.mm.dd 改訂モジュール名を書く
### V1.3 : 修正者名, yyyy.mm.dd 改訂モジュール名を書く

from flask import Flask, request, render_template
import class

def writeEntry(thread, entryAuther, entryContent):
    thread.addEntry(entryAuther, entryContent)
    addContents(new, thread)

def deleteEntry(thread, entry):
    thread.deleteEntry()
    deleteContents(thread, entry)
