# 112_python_learn_2023
_Python__大數據探勘

[GoogleMeeting上課網址](https://meet.google.com/bio-hmps-bpr)

[線上互動式編輯筆記 Google Colab](https://colab.research.google.com/?hl=zh-tw)

[徐國堂老師GitHub課程錄影連結](https://github.com/roberthsu2003/__112_python_chihlee__)

[解析jason格式 online jason viewer](https://jsoneditoronline.org/)

[pandas線上說明文件](https://pandas.pydata.org/docs/reference/index.html#api)

### GitHub Codespaces : Visual Studio Code Python環境設定
1) 畫面左下角「Codespaces:stunning succotash」-> "Add Dev Container Configuration files..." ->
"Create a new configuration..." -> "Python 3 Devcontainers..." -> "3.10-bullseye" ->
勾選4種選項:「A Remotes Shell ScriptsRunner wxw-matt」、「A Shell Command Runner wxw-matt」、「GitHub CLI devcontainers」、「Git(from souce)devcontainers」
-> "Keep Defaults"
畫面左下角「Codespaces:stunning succotash」-> "Rebuild Container" -> "Rebuild"

2) 延伸模組:在Marketplace中搜尋延伸模組 "jupyter"做安裝(延伸模組套件(4)) 。安裝後，第一次建立一支新的.ipynb檔案，在視窗右上邊「選取核心」-> 「Python Environments...」->「Python 3.10.13」

3) Codespace 將資料傳回Repo(Githu)設定 : 按「原始檔控制」圖示(VC畫面左側邊第3個圖示)，按「Commit」前要先輸入簡略的文字說明 -> 選「always」，總是上傳 -> 「Sync Change」，按＂ok＂，"Don't Show Show Again" -> "Yes"


### 檔案同時在repo和codespace修改要commit會出現錯誤，可在終端機執行命令
1) git push --force 強迫codespace的上傳，取消repo的任何修改下傳

2) git config pull.rebase false 下載repo和上傳codespace的檔案修改都保留

### Visual Studio Code連結GitHub
設定->命令選擇區->Configure Display Language->繁體
設定->AutoSave->afterDelay
最左下腳藍色(開啟遠端視窗)->GitHub Codespace->允許->Google Chrome->Codespace->Authorize Visual Studio Code(綠色按鈕)->Connect to Codespace...

Docker Desktop安裝(模擬Codespace在個人電腦):WSL:可以在Windows下創建Linux虛擬系統->新增開發者容器(Docker要先開啟才可新增)->新增開發人員容器

### 免費的Python模組 Pypi
PyInputPlus模組
pip 套件管理程式->pip install PyInputPlus   查詢:pip list

### 在Visual Studio Code專案中一次安裝所需要的外部模組
建立 requirements.txt，將要安裝的外部模組名稱列在檔案內容，透過執行命令 pip install -r requirements.txt 一次性安裝


### Python 資料結構
tuple() 唯讀，無法修改元素，暫時性
list []串列 可編輯元素
dict
set 對應資料

## 課程錄影檔

[20231014早上課程錄影](https://www.youtube.com/watch?v=YWTf5MMuTlY)

[20231014下午課程錄影](https://www.youtube.com/watch?v=ywgZoFSFy6o)

[20231021早上課程錄影-1](https://youtube.com/live/mTQnQarFk0c)

[20231021早上課程錄影-2](https://youtube.com/live/_D8jTDrcVkk)

[20231021下午課程錄影](https://youtube.com/live/xilBp4OW_S4)

[20231028早上課程錄影](https://youtube.com/live/OmaI3Lk14xs)

[20231028下午課程錄影](https://youtube.com/live/bPO4ogiVKmE)

[20231104早上課程錄影](https://youtube.com/live/FNED5Xou-HU)

[20231104下午課程錄影](https://youtube.com/live/6bIXI2lhDu0)

[20231111早上課程錄影](https://youtube.com/live/zcbPtg75KcE)

[20231111下午課程錄影](https://youtube.com/live/z5NiuQoStRc)

