#################################################
### Designer : 鈴木一史
# Date : 2021/06/13
# Purpose : C1 UI処理部から渡された検索語句とタグをC6スレッド情報管理部に渡す
#################################################

#################################################
# Function Name : SearchProcessing
### Designer : 鈴木一史
# Date : 2021/06/13
# Function: C1 UI処理部から渡された検索語句とタグをC6スレッド情報管理部に渡す。
# Return : search_word,search_tag
#################################################
import classes
import manageThread

def analyzeKeyword(line):

    searchWords = []
    searchTags = []

    #全角スペースを削除
    table = str.maketrans({'\u3000':' '})
    line = line.translate(table)

    # スペース文字で文字列を分解
    keywords = line.split(" ")

    if keywords[0] != "":
        # 検索語句かタグかを判別
        for keyword in keywords:
            if(keyword[0] == "#"):
                searchTags.append(keyword[1:])
            else:
                searchWords.append(keyword)
    
    # 検索語句の配列とタグの配列をまとめる作業
    searchKeys = []
    searchKeys.append(searchWords)
    searchKeys.append(searchTags)

    # search_key[ [検索語句1,検索語句2,...], [タグ1,タグ2,....]]
    return manageThread.search(searchKeys)
