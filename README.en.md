# Translationese Converter

[日本語](README.md) | [English](README.en.md) | [한국어](README.ko.md)

A toolkit for converting plain Japanese into "translationese" — the meme style
that spread on X, written as if a foreign-language post (mostly casual Korean
posts) had been machine-translated into Japanese.

It is based on a post that went viral in November 2026
and its reply thread, where everyone replied in translationese.
Other people's posts are not quoted verbatim, out of respect for their rights.

## Contents

- `STYLE.md` — a corpus of real examples and an analysis of the style rules (the core document)
- `prompt.md` — prompts you can paste into an LLM to get translationese conversion (male / female / English-source style / polite / English output / Korean output)
- `honyakugo.py` — a light rule-based converter (adds interjections, swaps vocabulary, adjusts sentence endings, appends ㅋㅋㅋ)
- `examples.md` — conversion examples

## Usage

```bash
python3 honyakugo.py "わかります、私もよくあります"
# -> わかります、私もしばしば起こります、マジで。

python3 honyakugo.py --female --kkk "それは面白い"
```

For full conversion (literal metaphors, restoring dropped subjects, restructuring
sentences), paste the prompts in `prompt.md` into an LLM (ChatGPT / Codex / Claude, etc.).

## The style in brief

1. Start with an interjection (クソッ、 / ハハ、 / おい、)
2. Spell out subjects and objects that Japanese would normally drop
3. Make metaphors literal and exaggerated (a meat-dumpling body)
4. End sentences with 〜なんだよ / マジで〜わ / 〜だよな
5. Mix in one stiff literal word (しばしば, 実に)
6. ㅋㅋㅋ is optional
7. Do not polish it with natural Japanese idioms. No honorifics. Keep it short.

See `STYLE.md` for details.

## License

No license is set.

## Using it with ChatGPT / Codex / Claude

- ChatGPT: paste a prompt from `prompt.md`, then your text, and it replies in translationese
- Codex: connect this repository and it can read `STYLE.md` and `prompt.md` to do the same conversion
- Claude: paste a prompt from `prompt.md`, or have it read this repository
- If you use it often, put the prompt into a Custom GPT's instructions or a Claude project's instructions so you do not have to paste it each time
