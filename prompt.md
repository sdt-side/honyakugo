# 翻訳語コンバータ（LLM用プロンプト）

通常の日本語を、Xのミーム「翻訳語」（外国語のカジュアルな投稿を機械翻訳したような
日本語）に変換するためのプロンプト。STYLE.md のルールが本体。

## プロンプト（男性版）

```
次の日本語の文章を「翻訳語」に変換してください。

翻訳語とは、韓国語のカジュアルな投稿を機械翻訳したような日本語の文体です。
ルール:
- 間投詞で始める（クソッ、／ハハ、／おい、から内容に合うもの）
- 日本語なら省略する主語・対象を明示する（自分は、俺は、あいつらは、その街の〜共）
- 比喩は直訳的で大げさに（例: 肉団子みたいな体型、ナイフで削ったみたいに細い）
- 文末は「〜なんだよ」「〜だよな」「〜わ」で締める。「マジで」は最大1回まで、入れなくてもよい。文末に固定しない
- 硬い直訳語を1つ混ぜる（しばしば、実に、まさに、等）
- 短文で区切る。全体で1〜3文
- 任意で ㅋㅋㅋ を文末に付ける
- 自然な日本語の慣用句で上手くまとめない。敬語にしない

変換する文章:
<ここに文章>
```

## プロンプト（女性版）

男性版との差分だけを差し替える:
- 文末は「〜わ」「〜のよ」「〜かしら」「〜なのよね」
- 間投詞は「もう、」「ハハ、」「ねえ、」から選ぶ
- 「兄弟」は使わない

## プロンプト（英語圏翻訳風）

男性版プロンプトのルールを次に差し替える:
- 間投詞は使わない。断定と命令形で書く（〜に来い。〜だ）
- 名詞・比喩は英語の直訳感を強く（例: 肉ゾーン、本物の男）
- 主語と所有格を明示する（私の国では、彼の〜は）
- 「本物の〜」「間違いなく〜」のような断定表現を1つ入れる
- ㅋㅋㅋ は使わない。「マジで」も使わない
- 短文で区切る。1〜3文

## プロンプト（丁寧め）

男性版プロンプトのルールを次に差し替える:
- です・ます調を保つ
- 主語と接続詞をいちいち明示する（私は、なぜなら、そのため）
- 直訳的な硬い語彙を使う（完全に、非常に、間違いなく、〜ということです）
- 感情は大げさに直接的に（心から感謝しています、深く感動しました）
- 間投詞、ㅋㅋㅋ、「マジで」は使わない

## プロンプト（英語版・翻訳語）

日本語を「日本語から機械翻訳されたような英語」に変換する。実例から抽出した型を使う。

```
Convert the following Japanese text into "translationese English" — English that
reads as if machine-translated from a casual Japanese post by Grok.
Rules (learned from real examples):
- End confirmations with "isn't it?" or "right?" no matter the original ending
- Translate 「さすが」 as "As expected!" and 「やっぱり」 as sentence-initial "After all,"
- List nouns literally without connectors, even if it creates odd implications
  (I like this photo of American men and meat)
- Render self-deprecation and modesty as earnest, dramatic declarations
  (There's no way we can beat these guys...)
- Keep parenthetical asides literally: (in two senses)
- Restore every dropped subject as "I", so many sentences start with I
- Drop or misuse articles (I went to park)
- Front the topic (As for me, ... / Speaking of ...)
- Keep over-politeness literally (Please be kind to me)
- Translate metaphors literally (thin like cut by a knife, a meat-dumpling body)
- Short declarative sentences in a row; do not smooth them into natural English prose
- A trailing "lol" is allowed
- Translate 草 as "grass" and leave "www" strings as-is or as "lol"
Text:
<ここに文章>
```

## プロンプト（韓国語版・翻訳語）

日本語を「日本語から機械翻訳されたような韓国語」に変換する。

```
Convert the following Japanese text into Korean that reads as if machine-translated
from Japanese.
Rules:
- Keep the Japanese sentence structure and topic-fronting as-is
- Overuse 〜것이다 endings and literal passives/causatives from Japanese
- Translate Japanese idioms literally instead of using natural Korean idioms
- Keep a stiffness that does not match a casual context
- Short sentences, declarative endings
Text:
<ここに文章>
```
