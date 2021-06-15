#################################################
### Designer : 鈴木一史
### Date : 2021/06/13
### Purpose : C1 UI処理部から渡された検索語句とタグをC6スレッド情報管理部に渡す
#################################################

#################################################
### Function Name : SearchProcessing
### Designer : 鈴木一史
### Date : 2021/06/13
### Function: C1 UI処理部から渡された検索語句とタグをC6スレッド情報管理部に渡す。
### Return : search_word,search_tag
#################################################
import entry

class Thread:
    id: int
    name: str
    details: str
    lastEntryId: int
    entries = []

    def __init__(self, threadId, threadName, threadDetails):
        self.id = threadId
        self.name = threadName
        self.details = threadDetails
        self.lastEntryId = 0

    def addEntry(self, entryAuther, entryContent):
        self.lastEntryId += 1
        new = entry.Entry(self.lastEntryId, entryAuther, entryContent)
        self.entries.append(new)

def analyzeKeyword(line):

    searchWords = []
    searchTags = []

    #スペース文字で文字列を分解
    keywords = line.split(" ")

    #検索語句かタグかを判別
    for keyword in keywords:
        if(keyword[0] == "#"):
            searchTags.append(keyword[1:])
        else:
            searchWords.append(keyword)

    #検索語句の配列とタグの配列をまとめる作業
    search_keys = []
    search_keys.append(searchWords)
    search_keys.append(searchTags)

    # search_key[ [検索語句1,検索語句2,...], [タグ1,タグ2,....]]
    return search_keys
    