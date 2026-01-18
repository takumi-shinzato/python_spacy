import spacy
import random
nlp = spacy.load("ja_ginza")

# サンプルテキスト
texts = [
    "私は昨日、美味しいラーメンを食べました。",
    "今日は天気が良いので、外に出かけた。",
    "友達と一緒に映画を見に行った。",
    "明日は学校に行く予定だ。",
    "プログラミングが好きです。",
    "私は毎朝、ジョギングをします。",
    "昨日は雨が降っていたので、家で本を読んだ。",
    "友達からプレゼントをもらって、とても嬉しかった。",
    "私は将来、エンジニアになりたいと思っています。",
    "週末は家族と一緒にピクニックに行きます。",
    "私はコーヒーが好きで、毎日飲んでいます。",
    "昨日、友達と買い物に行って、新しい服を買った。",
    "私は音楽を聴くのが趣味です。",
    "今日は仕事が忙しくて、疲れました。",
    "私は旅行が好きで、世界中を回りたいです。"
]

# 各文をトークンに分割
sentences_tokens = []
for text in texts:
    doc = nlp(text)
    for sent in doc.sents:  # 文ごとに分ける
        tokens = [token.text for token in sent]
        if tokens:
            tokens.append('<END>')  # 終了コードを追加
            sentences_tokens.append(tokens)

# 状態遷移データを作成
transitions = {}
start_tokens = []
for tokens in sentences_tokens:
    if len(tokens) > 1:
        start_tokens.append(tokens[0])
        for i in range(len(tokens) - 1):
            current = tokens[i]
            next_token = tokens[i + 1]
            if current not in transitions:
                transitions[current] = []
            transitions[current].append(next_token)

# ランダムな文章を生成
for i in range(5):
    start_token = random.choice(start_tokens)
    sentence = [start_token]
    current = start_token
    while True:
        if current not in transitions:
            break
        next_tokens = transitions[current]
        next_token = random.choice(next_tokens)
        if next_token == '<END>':
            break
        sentence.append(next_token)
        current = next_token

    print(''.join(sentence))