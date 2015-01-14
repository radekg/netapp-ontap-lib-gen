class LanguageCode(basestring):
    """
    Language Code.
    <p>
    The following are the possible language codes along with their
    names:
    <ul>
    <li> 'C'            ... POSIX,
    <li> 'ar'           ... Arabic,
    <li> 'cs'           ... Czech,
    <li> 'da'           ... Danish,
    <li> 'de'           ... German,
    <li> 'en'           ... English,
    <li> 'en_US'        ... English (US),
    <li> 'es'           ... Spanish,
    <li> 'fi'           ... Finnish,
    <li> 'fr'           ... French,
    <li> 'he'           ... Hebrew,
    <li> 'hr'           ... Croatian,
    <li> 'hu'           ... Hungarian,
    <li> 'it'           ... Italian,
    <li> 'ja'           ... Japanese euc-j*,
    <li> 'ja_v1'        ... Japanese euc-j,
    <li> 'ja_JP.PCK'    ... Japanese PCK (sjis)*,
    <li> 'ja_JP.932'    ... Japanese cp932*,
    <li> 'ja_JP.PCK_v2' ... Japanese PCK (sjis),
    <li> 'ko'           ... Korean,
    <li> 'no'           ... Norwegian,
    <li> 'nl'           ... Dutch,
    <li> 'pl'           ... Polish,
    <li> 'pt'           ... Portuguese,
    <li> 'ro'           ... Romanian,
    <li> 'ru'           ... Russian,
    <li> 'sk'           ... Slovak,
    <li> 'sl'           ... Slovenian,
    <li> 'sv'           ... Swedish,
    <li> 'tr'           ... Turkish,
    <li> 'zh'           ... Simplified Chinese,
    <li> 'zh.GBK'       ... Simplified Chinese (GBK),
    <li> 'zh_TW'        ... Traditional Chinese euc-tw,
    <li> 'zh_TW.BIG5'   ... Traditional Chinese Big 5
    </ul>
    <p>
    To use UTF-8 as the NFS character set, append '.UTF-8' to the
    language code.
    """
    
    @staticmethod
    def get_api_name():
          return "language-code"
    
