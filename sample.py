import spacy

# 日本語モデルの読み込み
nlp = spacy.load("ja_ginza")

text = "私は昨日、美味しいラーメンを食べました。"
doc = nlp(text)

# 単語ごとにバラバラにして表示
for token in doc:
    print(token.text, token.pos_) # 単語と品詞を表示