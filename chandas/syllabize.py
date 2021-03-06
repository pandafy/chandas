# -*- coding: utf-8 -*-
import logging
import string

import PyICU
import regex
from indic_transliteration import sanscript
from .sanskrit_numbers import get_cardinal_number
def get_graphemes(in_string):
  """ Split a devanAgarI and possibly other strings into graphemes.

  Example: assert syllabize.get_graphemes(u"बिक्रममेरोनामहो") == "बि क् र म मे रो ना म हो".split(" ")
  :param in_string:
  :return:
  """
  break_iterator = PyICU.BreakIterator.createCharacterInstance(PyICU.Locale())
  break_iterator.setText(in_string)
  i = 0
  graphemes = []
  for j in break_iterator:
    s = in_string[i:j]
    graphemes.append(s)
    i = j
  return graphemes


def is_vyanjanaanta(in_string):
  return in_string.endswith("्") or in_string.endswith("य्ँ") or in_string.endswith("व्ँ") or in_string.endswith("ल्ँ")


def has_vowel(in_string):
  return bool(regex.fullmatch(".*[ऄ-औ ऺ-ऻ ा-ौ ॎ-ॏ ॲ-ॷ].*".replace(" ", ""), in_string, flags=regex.UNICODE) or regex.fullmatch(".*[क-हक़-य़ॸ-ॿ](?!्).*", in_string, flags=regex.UNICODE))


def begins_with_vowel(in_string):
  return bool(regex.fullmatch(r"[ऄ-औॲ-ॷ].*", in_string, flags=regex.UNICODE))


def get_syllables(in_string):
  """ Split devanAgarI string into syllables. Ignores spaces and punctuation.

  syllabize.get_syllables(u"बिक्रममेरोनामहो") == "बिक् र म मे रो ना म हो".split(" ")
  :param in_string:
  :return:
  """
  # Normalize
  cleaned_phrase = in_string.replace(u"\u0966", "0", ).replace( u"\u0967", "1").replace(u"\u0968","2").replace(u"\u0969", "3",).replace(u"\u096A", "4",).replace(u"\u096B", "5",).replace(u"\u096C", "6",).replace(u"\u096D", "7",).replace(u"\u096E", "8",).replace(u"\u096F", "9",)

  cleaned_phrase = regex.sub(r"([^ऀ-़ ा-ॣ ॲ-ॿ  ꣠-ꣽ  ᳐-᳹])", "", cleaned_phrase, flags=regex.UNICODE)
  cleaned_phrase = cleaned_phrase.replace("ॐ", "ओम्")

  final_phrases = []
  for phrase in cleaned_phrase.split(' '):
    try:
      number = int(phrase)
    except Exception as e:
      final_phrases.append(phrase)
    else:
      final_phrases.append(get_cardinal_number(number))
  graphemes = get_graphemes(' '.join(final_phrases))
  syllables = []
  while len(graphemes) > 0:
    current_syllable = graphemes.pop(0)
    if len(graphemes) > 0 and regex.fullmatch(r" ꣠-ꣽ  ᳐-᳹]", graphemes[0], flags=regex.UNICODE):
      current_syllable = current_syllable  + graphemes.pop(0)

    if current_syllable == ' ':
      syllables.append(' ')
      continue
    while len(graphemes) > 0 and not has_vowel(graphemes[0]) and graphemes[0] != ' ':
      current_syllable = current_syllable  + graphemes.pop(0)
    if is_vyanjanaanta(current_syllable) and len(graphemes) > 0 and begins_with_vowel(graphemes[0]):
      vyanjana = current_syllable[-2:]
      graphemes[0] = sanscript.SCHEMES[sanscript.DEVANAGARI].do_vyanjana_svara_join(vyanjana, graphemes[0])
      current_syllable = current_syllable[:-2]

    while len(graphemes) > 0 and len(current_syllable) > 0 and not has_vowel(current_syllable):
      current_syllable = current_syllable  + graphemes.pop(0)
      # Deal with grapheme list like 'सा', 'म्', 'अ', 'प', 'ह', 'त्', 'यै'] - we'll need to merge म् and अ to get म.

    if len(current_syllable) > 0:
      syllables.append(current_syllable)
  return syllables


def get_syllable_weight(syllable):
  if regex.search("[् आ ई ऊ ॠ ए ऐ ॠ ॡ औ ओ औ ॐ ऻ ा ी ू ॄ ॗॣ ॎ े ै ो ौ ॕ ं ः  ᳢-ᳬ ᳮ ᳯ ᳰ ᳱ ᳲ ᳳ ᳵ ᳶ]".replace(" ", ""), syllable, flags=regex.UNICODE):
    return "G"
  else:
    return "L"


def to_weight_list(line_in):
  syllables = get_syllables(line_in)
  return [get_syllable_weight(syllable) for syllable in syllables]
