"""
SindhiNormalizer — Unicode normalization for Sindhi (Arabic script).
Handles NFC normalization, diacritic removal, and character standardization.
"""
import unicodedata
import re


class SindhiNormalizer:
    """
    Usage:
        norm = SindhiNormalizer()
        norm.normalize("ھوُ ھر روزَ")          # NFC + strip
        norm.normalize("ھوُ ھر روزَ", remove_diacritics=True)  # strip vowel marks too
    """

    # Arabic diacritics (harakat): zabar, zer, pesh, tanwin forms, shadda, sukun
    _DIACRITICS = re.compile(
        r"[\u064B-\u065F\u0670\u06D6-\u06DC\u06DF-\u06E4\u06E7\u06E8\u06EA-\u06ED]"
    )

    # Normalize common alternate forms used in Sindhi
    _CHAR_MAP = str.maketrans({
        "\u06BE": "\u06BE",   # ھ (do-chashmi he) — keep as-is, don't collapse to ه
        "\u0649": "\u06CC",   # ى → ي  (alef maqsura → Sindhi ye)
        "\u0643": "\u06A9",   # ك → ڪ  (Arabic kaf → Sindhi kaf)
    })

    def normalize(self, text: str, remove_diacritics: bool = False) -> str:
        """
        Normalize Sindhi text:
        - NFC Unicode normalization
        - Strip leading/trailing whitespace
        - Collapse multiple spaces
        - Optionally remove Arabic diacritics (vowel marks)
        """
        if not text:
            return text
        text = unicodedata.normalize("NFC", text)
        text = text.translate(self._CHAR_MAP)
        if remove_diacritics:
            text = self._DIACRITICS.sub("", text)
        text = re.sub(r"[ \t]+", " ", text).strip()
        return text
