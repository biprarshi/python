'''
from translate import Translator

translator = Translator("eng_Latn", "fra_Latn")

english_sentence = "This is just a simple phrase." or [
    "Those are multiples sentences.",
    "If you have lots of them, load them directly from file.",
    "To efficiently batch translate them."
  ]
french_sentence = translator.translate(english_sentence)

print(f"{english_sentence=}")
print(f"{french_sentence=}")
'''

from translate import Translator
translator = Translator(to_lang="en", from_lang='es')
translation = translator.translate("Hueco Mundo")
print(translation)

# from translate import Translator
to_lang = 'ji'
from_lang = 'en'
secret = '<your secret from Microsoft>'
# translator = Translator(provider='microsoft', to_lang=to_lang, secret_access_key=secret)
# provider ['mymemory', 'microsoft', 'deepl', 'libre']
# translator = Translator(provider='mymemory',to_lang=to_lang, from_lang =from_lang, email='')
# print(translator.translate('the book is on the table'))

# to_lang = 'bn'
translator = Translator(to_lang="bn", from_lang='es')
translation = translator.translate("Hueco Mundo")
print(translation)

'''
ISO 639-1 language name
Abkhazian, Abkhaz ab
Afar aa
Afrikaans af
Akan ak
Albanian sq
Amharic am
Arabic ar
Aragonese an
Armenian hy
Assamese as
Avaric av
Avestan ae
Aymara ay
Azerbaijani az
Bambara bm
Bashkir ba
Basque eu
Belarusian be
Bengali bn
Bislama bi 
Bosnian bs
Breton br
Bulgarian bg
Burmese, Myanmar my
Catalan, Valencian ca
Chamorro ch
Chechen ce
Chichewa, Chewa, Nyanja ny
Chinese zh
Church Slavonic, Old Slavonic, Old Church Slavonic cu
Chuvash cv
Cornish kw
Corsican co
Cree cr
Croatian hr
Czech cs
Danish da
Divehi, Dhivehi, Maldivian dv
Dutch, Flemish nl
Dzongkha dz
English en
Esperanto eo
Estonian et
Ewe ee
Faroese fo
Fijian fj
Filipino, Pilipino(ISO 639-2) fil
Finnish fi
French fr
Western Frisian, Frisian fy
Fulah, Fula ff
Gaelic, Scottish Gaelic gd
Galician gl
Ganda lg
Georgian ka
German de
Greek, Modern(1453-) el
Ancient Greek(ISO 639-3) grc
Kalaallisut, Greenlandic kl
Guarani gn
Gujarati gu
Haitian, Haitian Creole ht
Hausa ha
Hebrew he
Hebrew(ISO 639:1988) iw
Herero hz
Hindi hi
Hiri Motu ho
Hungarian hu
Icelandic is
Ido io
Igbo ig
Indonesian id
Standard Indonesian ind
Interlingua(International Auxiliary Language Association) ia
Interlingue, Occidental ie
Inuktitut iu
Inupiaq ik
Irish ga
Italian it
Japanese ja
Javanese jv
Kannada kn
Kanuri kr
Kashmiri ks
Kazakh kk
Central KhmerKhmer, Cambodian km
Kikuyu, Gikuyu ki
Kinyarwanda rw
Kirghiz, Kyrgyz ky
Komi kv
Kongo kg
Korean ko
Kuanyama, Kwanyama kj
Kurdish ku
Lao lo
Latin la
Latvian lv
Limburgan, Limburger, Limburgish li
Lingala ln
Lithuanian lt
Luba-Katanga, Luba-Shaba lu
Luxembourgish, Letzeburgesch lb
Macedonian mk
Malagasy mg
Malay ms
Standard Malay zsm
Malayalam ml
Maltese mt
Manx gv
Maori, Māori mi
Marathi, Marāṭhī mr
Marshallese mh
Mongolian mn
Nauru, Nauruan na
Navajo, Navaho nv
North Ndebele, Northern Ndebele nd
South Ndebele, Southern Ndebele nr 
Ndonga ng
Nepali ne
Norwegian no/nor
Norwegian Bokmål nb/nob
Norwegian Nynorsk nn / nno
Sichuan Yi, Nuosu ii
Occitan oc
Ojibwa, Ojibwe oj
Oriya, Odia or
Oromo om
Ossetian, Ossetic os
Pali, Pāli pi 
Pashto, Pushto ps
Persian, Farsi fa
Polish pl
Portuguese pt
Punjabi, Panjabi pa
Quechua qu
Romanian, Moldavian, Moldovan ro
Romansh rm
Rundi, Kirundi rn
Russian ru
Northern Sami se
Samoan sm
Sango sg
Sanskrit sa
Sardinian sc
Serbian sr
Shona sn
Sindhi sd
Sinhala, Sinhalese si
Slovak sk
Slovenian, Slovene sl
Somali so
Southern Sotho st
Spanish, Castilian es
Sundanese su
Swahili sw
Swati, Swazi ss
Swedish sv
Tagalog tl
Tahitian ty
Tajik tg
Tamil ta 
Tatar tt
Telugu te
Thai th
Tibetan, Standard Tibetan bo
Tigrinya ti
Tonga (Tonga Islands), Tongan to 
Tsonga ts
Tswana tn
Turkish tr
Turkmen tk
Twi tw (covered by macrolanguage ak)
Uighur, Uyghur ug
Ukrainian uk
Urdu ur
Uzbek uz
Venda ve 
Vietnamese vi 
Volapük vo
Walloon wa
Welsh cy
Wolof wo
Xhosa xh
Yiddish yi
Yiddish(ISO 639:1988) ji
Yoruba yo
Zhuang, Chuang za
Zulu zu
'''
