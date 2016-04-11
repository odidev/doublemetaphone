# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import unittest

from doublemetaphone import doublemetaphone


class MetaphoneTestCase(unittest.TestCase):
    """
    """
    def test_single_result(self):
        result = doublemetaphone(u"aubrey")
        self.assertEquals(result, ('APR', 'APR'))

    def test_double_result(self):
        result = doublemetaphone(u"richard")
        self.assertEquals(result, ('RXRT', 'RKRT'))

    def test_general_word_list(self):
        result = doublemetaphone('Jose')
        self.assertEquals(result, ('HS', 'HS'))
        result = doublemetaphone('cambrillo')
        self.assertEquals(result, ('KMPRL', 'KMPR'))
        result = doublemetaphone('otto')
        self.assertEquals(result, ('AT', 'AT'))
        result = doublemetaphone('aubrey')
        self.assertEquals(result, ('APR', 'APR'))
        result = doublemetaphone('maurice')
        self.assertEquals(result, ('MRS', 'MRS'))
        result = doublemetaphone('auto')
        self.assertEquals(result, ('AT', 'AT'))
        result = doublemetaphone('maisey')
        self.assertEquals(result, ('MS', 'MS'))
        result = doublemetaphone('catherine')
        self.assertEquals(result, ('K0RN', 'KTRN'))
        result = doublemetaphone('geoff')
        self.assertEquals(result, ('JF', 'KF'))
        result = doublemetaphone('Chile')
        self.assertEquals(result, ('XL', 'XL'))
        result = doublemetaphone('katherine')
        self.assertEquals(result, ('K0RN', 'KTRN'))
        result = doublemetaphone('steven')
        self.assertEquals(result, ('STFN', 'STFN'))
        result = doublemetaphone('zhang')
        self.assertEquals(result, ('JNK', 'JNK'))
        result = doublemetaphone('bob')
        self.assertEquals(result, ('PP', 'PP'))
        result = doublemetaphone('ray')
        self.assertEquals(result, ('R', 'R'))
        result = doublemetaphone('Tux')
        self.assertEquals(result, ('TKS', 'TKS'))
        result = doublemetaphone('bryan')
        self.assertEquals(result, ('PRN', 'PRN'))
        result = doublemetaphone('bryce')
        self.assertEquals(result, ('PRS', 'PRS'))
        result = doublemetaphone('Rapelje')
        self.assertEquals(result, ('RPL', 'RPL'))
        result = doublemetaphone('richard')
        self.assertEquals(result, ('RXRT', 'RKRT'))
        result = doublemetaphone('solilijs')
        self.assertEquals(result, ('SLLS', 'SLLS'))
        result = doublemetaphone('Dallas')
        self.assertEquals(result, ('TLS', 'TLS'))
        result = doublemetaphone('Schwein')
        self.assertEquals(result, ('XN', 'XFN'))
        result = doublemetaphone('dave')
        self.assertEquals(result, ('TF', 'TF'))
        result = doublemetaphone('eric')
        self.assertEquals(result, ('ARK', 'ARK'))
        result = doublemetaphone('Parachute')
        self.assertEquals(result, ('PRKT', 'PRKT'))
        result = doublemetaphone('brian')
        self.assertEquals(result, ('PRN', 'PRN'))
        result = doublemetaphone('randy')
        self.assertEquals(result, ('RNT', 'RNT'))
        result = doublemetaphone('Through')
        self.assertEquals(result, ('0R', 'TR'))
        result = doublemetaphone('Nowhere')
        self.assertEquals(result, ('NR', 'NR'))
        result = doublemetaphone('heidi')
        self.assertEquals(result, ('HT', 'HT'))
        result = doublemetaphone('Arnow')
        self.assertEquals(result, ('ARN', 'ARNF'))
        result = doublemetaphone('Thumbail')
        self.assertEquals(result, ('0MPL', 'TMPL'))

    def test_homophones(self):
        self.assertEqual(
            doublemetaphone(u"tolled"),
            doublemetaphone(u"told"))
        self.assertEqual(
            doublemetaphone(u"katherine"),
            doublemetaphone(u"catherine"))
        self.assertEqual(
            doublemetaphone(u"brian"),
            doublemetaphone(u"bryan"))

    def test_similar_names(self):
        #result = doublemetaphone("Bartoš")
        #self.assertEquals(result, ('PRTS', 'PRTS'))
        result = doublemetaphone(u"Bartosz")
        self.assertEquals(result, ('PRTS', 'PRTX'))
        result = doublemetaphone(u"Bartosch")
        self.assertEquals(result, ('PRTX', 'PRTX'))
        result = doublemetaphone(u"Bartos")
        self.assertEquals(result, ('PRTS', 'PRTS'))

        result = set(doublemetaphone(u"Jablonski")).intersection(
            doublemetaphone(u"Yablonsky"))
        self.assertEquals(list(result), ['APLNSK'])
        result = set(doublemetaphone(u"Smith")).intersection(
            doublemetaphone(u"Schmidt"))
        self.assertEquals(list(result), ['XMT'])

    def test_non_english_unicode(self):
        result = doublemetaphone("andestādītu")
        self.assertEquals(result, ('ANTSTTT', 'ANTSTTT'))

    #def test_c_cedilla(self):
    #    result = doublemetaphone("français")
    #    self.assertEquals(result, ('FRNS', 'FRNSS'))
    #    result = doublemetaphone("garçon")
    #    self.assertEquals(result, ('KRSN', ''))
    #    result = doublemetaphone("leçon")
    #    self.assertEquals(result, ('LSN', ''))

    def test_various_german(self):
        result = doublemetaphone("ach")
        self.assertEquals(result, ("AK", "AK"))
        result = doublemetaphone("bacher")
        self.assertEquals(result, ("PKR", "PKR"))
        result = doublemetaphone("macher")
        self.assertEquals(result, ("MKR", "MKR"))

    def test_various_italian(self):
        result = doublemetaphone("bacci")
        self.assertEquals(result, ("PX", "PX"))
        result = doublemetaphone("bertucci")
        self.assertEquals(result, ("PRTX", "PRTX"))
        result = doublemetaphone("bellocchio")
        self.assertEquals(result, ("PLX", "PLX"))
        result = doublemetaphone("bacchus")
        self.assertEquals(result, ("PKS", "PKS"))
        result = doublemetaphone("focaccia")
        self.assertEquals(result, ("FKX", "FKX"))
        result = doublemetaphone("chianti")
        self.assertEquals(result, ("KNT", "KNT"))
        result = doublemetaphone("tagliaro")
        self.assertEquals(result, ("TKLR", "TLR"))
        result = doublemetaphone("biaggi")
        self.assertEquals(result, ("PJ", "PK"))

    def test_various_spanish(self):
        result = doublemetaphone("bajador")
        self.assertEquals(result, ("PJTR", "PHTR"))
        result = doublemetaphone("cabrillo")
        self.assertEquals(result, ("KPRL", "KPR"))
        result = doublemetaphone("gallegos")
        self.assertEquals(result, ("KLKS", "KKS"))
        result = doublemetaphone("San Jacinto")
        self.assertEquals(result, ("SNHSNT", "SNHSNT"))

    def test_various_french(self):
        result = doublemetaphone("rogier")
        self.assertEquals(result, ("RJ", "RJR"))
        result = doublemetaphone("breaux")
        self.assertEquals(result, ("PR", "PR"))

    def test_various_slavic(self):
        result = doublemetaphone("Wewski")
        self.assertEquals(result, ("ASK", "FFSK"))

    def test_various_chinese(self):
        result = doublemetaphone("zhao")
        self.assertEquals(result, ("J", "J"))

    def test_dutch_origin(self):
        result = doublemetaphone("school")
        self.assertEquals(result, ("SKL", "SKL"))
        result = doublemetaphone("schooner")
        self.assertEquals(result, ("SKNR", "SKNR"))
        result = doublemetaphone("schermerhorn")
        self.assertEquals(result, ("XRMRRN", "SKRMRRN"))
        result = doublemetaphone("schenker")
        self.assertEquals(result, ("XNKR", "SKNKR"))

    def test_ch_words(self):
        result = doublemetaphone("Charac")
        self.assertEquals(result, ("KRK", "KRK"))
        result = doublemetaphone("Charis")
        self.assertEquals(result, ("KRS", "KRS"))
        result = doublemetaphone("chord")
        self.assertEquals(result, ("KRT", "KRT"))
        result = doublemetaphone("Chym")
        self.assertEquals(result, ("KM", "KM"))
        result = doublemetaphone("Chia")
        self.assertEquals(result, ("K", "K"))
        result = doublemetaphone("chem")
        self.assertEquals(result, ("KM", "KM"))
        result = doublemetaphone("chore")
        self.assertEquals(result, ("XR", "XR"))
        result = doublemetaphone("orchestra")
        self.assertEquals(result, ("ARKSTR", "ARKSTR"))
        result = doublemetaphone("architect")
        self.assertEquals(result, ("ARKTKT", "ARKTKT"))
        result = doublemetaphone("orchid")
        self.assertEquals(result, ("ARKT", "ARKT"))

    def test_cc_words(self):
        result = doublemetaphone("accident")
        self.assertEquals(result, ("AKSTNT", "AKSTNT"))
        result = doublemetaphone("accede")
        self.assertEquals(result, ("AKST", "AKST"))
        result = doublemetaphone("succeed")
        self.assertEquals(result, ("SKST", "SKST"))

    def test_mc_words(self):
        result = doublemetaphone("mac caffrey")
        self.assertEquals(result, ("MKFR", "MKFR"))
        result = doublemetaphone("mac gregor")
        self.assertEquals(result, ("MKRKR", "MKRKR"))
        result = doublemetaphone("mc crae")
        self.assertEquals(result, ("MKR", "MKR"))
        result = doublemetaphone("mcclain")
        self.assertEquals(result, ("MKLN", "MKLN"))

    def test_gh_words(self):
        result = doublemetaphone("laugh")
        self.assertEquals(result, ("LF", "LF"))
        result = doublemetaphone("cough")
        self.assertEquals(result, ("KF", "KF"))
        result = doublemetaphone("rough")
        self.assertEquals(result, ("RF", "RF"))

    def test_g3_words(self):
        result = doublemetaphone("gya")
        self.assertEquals(result, ("K", "J"))
        result = doublemetaphone("ges")
        self.assertEquals(result, ("KS", "JS"))
        result = doublemetaphone("gep")
        self.assertEquals(result, ("KP", "JP"))
        result = doublemetaphone("geb")
        self.assertEquals(result, ("KP", "JP"))
        result = doublemetaphone("gel")
        self.assertEquals(result, ("KL", "JL"))
        result = doublemetaphone("gey")
        self.assertEquals(result, ("K", "J"))
        result = doublemetaphone("gib")
        self.assertEquals(result, ("KP", "JP"))
        result = doublemetaphone("gil")
        self.assertEquals(result, ("KL", "JL"))
        result = doublemetaphone("gin")
        self.assertEquals(result, ("KN", "JN"))
        result = doublemetaphone("gie")
        self.assertEquals(result, ("K", "J"))
        result = doublemetaphone("gei")
        self.assertEquals(result, ("K", "J"))
        result = doublemetaphone("ger")
        self.assertEquals(result, ("KR", "JR"))
        result = doublemetaphone("danger")
        self.assertEquals(result, ("TNJR", "TNKR"))
        result = doublemetaphone("manager")
        self.assertEquals(result, ("MNKR", "MNJR"))
        result = doublemetaphone("dowager")
        self.assertEquals(result, ("TKR", "TJR"))

    def test_pb_words(self):
        result = doublemetaphone("Campbell")
        self.assertEquals(result, ("KMPL", "KMPL"))
        result = doublemetaphone("raspberry")
        self.assertEquals(result, ("RSPR", "RSPR"))

    def test_th_words(self):
        result = doublemetaphone("Thomas")
        self.assertEquals(result, ("TMS", "TMS"))
        result = doublemetaphone("Thames")
        self.assertEquals(result, ("TMS", "TMS"))
