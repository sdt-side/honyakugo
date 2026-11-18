#!/usr/bin/env python3
"""翻訳語コンバータ（軽量ルールベース版）

通常の日本語に、翻訳語ミームの「味付け」を施す簡易変換器。
文の意味を作り替える本格変換は LLM 用プロンプト (prompt.md) を使うこと。
これは間投詞の付与、語彙の置換、文末の調整、ㅋㅋㅋ の付与など、
機械的にできる部分だけを担当する。

使い方:
  python3 honyakugo.py "わかります、私もよくあります"
  python3 honyakugo.py --female "この男、いつも関わってますよね"
  python3 honyakugo.py --kkk "それは面白い"
"""
import argparse
import re
import sys

# 語彙の置換（やわらかい口語 -> 直訳っぽい硬さ・大げささへ）
SWAPS = [
    ("すごく", "マジで"),
    ("とても", "本当に"),
    ("よくある", "しばしば起こる"),
    ("よくあります", "しばしば起こります"),
    ("タダ", "無料"),
    ("みんな", "全員"),
    ("あの人たち", "あいつら"),
    ("あの人", "あいつ"),
]

# 感情キーワード -> 間投詞
INTERJECTIONS = [
    (("笑", "面白", "おもしろ", "ウケ"), "ハハ、"),
    (("ムカ", "最悪", "ふざけ", "太っ", "腹立"), "クソッ、"),
    (("見て", "聞いて", "ねえ"), "おい、"),
]

FEMALE_ENDINGS = [
    (r"だよ$", "だわ"),
    (r"ですよね$", "なのよね"),
    (r"ますよね$", "ますわよね"),
    (r"だよね$", "なのよね"),
]


def convert(text: str, female: bool = False, kkk: bool = False) -> str:
    out = text.strip()

    # 語彙置換
    for a, b in SWAPS:
        out = out.replace(a, b)

    # 女性版の文末調整
    if female:
        for pat, rep in FEMALE_ENDINGS:
            out = re.sub(pat, rep, out)

    # 「マジで」が無ければ、最後の文の文末に寄せる
    if "マジで" not in out:
        if out.endswith("。"):
            out = out[:-1] + "、マジで。"
        elif out.endswith("わ"):
            out = out + "マジで。"
        elif not out.endswith("。"):
            out = out + "。マジで。"

    # 間投詞を先頭に（既に付いていなければ）
    if not re.match(r"(クソ|ハハ|おい|もう|ねえ)", out):
        for keys, inter in INTERJECTIONS:
            if any(k in out for k in keys):
                if female and inter == "おい、":
                    inter = "ねえ、"
                out = inter + out
                break

    # ㅋㅋㅋ
    if kkk:
        out = out + "ㅋㅋㅋㅋㅋㅋ"

    return out


def main() -> None:
    ap = argparse.ArgumentParser(description="翻訳語コンバータ（軽量版）")
    ap.add_argument("text", help="変換する日本語")
    ap.add_argument("--female", action="store_true", help="女性版の語尾にする")
    ap.add_argument("--kkk", action="store_true", help="ㅋㅋㅋ を付ける")
    args = ap.parse_args()
    print(convert(args.text, female=args.female, kkk=args.kkk))


if __name__ == "__main__":
    main()
