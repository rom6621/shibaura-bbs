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
import thread

class Entry:
    id: int #書込の順番
    auther: str
    content: str

    def __init__(self, entryId, entryAuther, entryContent):
        self.id = entryId
        self.auther = entryAuther
        self.content = entryContent

    def exchangeContent(self):
        self.content = '削除されました'
        return self

"""def d_addContents(entry, thread):
    print(entry.id, entry.auther, entry.content, thread.name)

def d_deleteContents(thread, entry):
    print(entry.id, entry.auther, entry.content, thread.name)   テスト用コード"""

#書込みを登録する関数
def writeEntry(thread, entryAuther, entryContent):
    new = thread.addEntry(entryAuther, entryContent)
    #addEntryで作成されたnewインスタンスを用いて関数を呼び出す
    addContents(new, thread) #本物のコード
    """d_addContents(new, thread)
    return new   テスト用コード"""

#書込みを削除する関数
def deleteEntry(thread, entry):
    #書き込み内容のみを置き換えたものをnewインスタンスに入れる
    new = entry.exchangeContent()
    deleteContents(thread, new) #本物のコード
    #d_deleteContents(thread, new)   テスト用コード
