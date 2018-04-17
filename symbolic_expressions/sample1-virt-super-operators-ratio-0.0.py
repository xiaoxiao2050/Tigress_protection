#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])
ref_264 = SymVar_0
ref_279 = ref_264 # MOV operation
ref_6794 = ref_279 # MOV operation
ref_7078 = ref_6794 # MOV operation
ref_7086 = ((ref_7078 << (0x39 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_7093 = ref_7086 # MOV operation
ref_8190 = ref_279 # MOV operation
ref_8429 = ref_8190 # MOV operation
ref_8437 = (ref_8429 >> (0x7 & 0x3F)) # SHR operation
ref_8444 = ref_8437 # MOV operation
ref_8573 = ref_8444 # MOV operation
ref_8585 = ref_7093 # MOV operation
ref_8587 = (ref_8585 | ref_8573) # OR operation
ref_8738 = ref_8587 # MOV operation
ref_11131 = ref_8738 # MOV operation
ref_11374 = ref_11131 # MOV operation
ref_11376 = ((ref_11374 + 0x2D4AF89B) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_11532 = ref_11376 # MOV operation
ref_11534 = (ref_11532 & 0x1D5ABF66) # AND operation
ref_12636 = ref_279 # MOV operation
ref_12920 = ref_12636 # MOV operation
ref_12928 = ((ref_12920 << (0x35 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_12935 = ref_12928 # MOV operation
ref_14032 = ref_279 # MOV operation
ref_14271 = ref_14032 # MOV operation
ref_14279 = (ref_14271 >> (0xB & 0x3F)) # SHR operation
ref_14286 = ref_14279 # MOV operation
ref_14415 = ref_14286 # MOV operation
ref_14427 = ref_12935 # MOV operation
ref_14429 = (ref_14427 | ref_14415) # OR operation
ref_14545 = ref_14429 # MOV operation
ref_14557 = ref_11534 # MOV operation
ref_14559 = ((ref_14545 - ref_14557) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_14567 = ref_14559 # MOV operation
ref_14713 = ref_14567 # MOV operation
ref_17021 = ref_279 # MOV operation
ref_17112 = ref_17021 # MOV operation
ref_17126 = ((ref_17112 - 0xE8D4346) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_17134 = ref_17126 # MOV operation
ref_17280 = ref_17134 # MOV operation
ref_19673 = ref_8738 # MOV operation
ref_19746 = ref_19673 # MOV operation
ref_19760 = ((0x20453EE3 + ref_19746) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_20863 = ref_279 # MOV operation
ref_20954 = ref_20863 # MOV operation
ref_20966 = ref_19760 # MOV operation
ref_20968 = ((ref_20954 - ref_20966) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_20976 = ref_20968 # MOV operation
ref_21122 = ref_20976 # MOV operation
ref_24917 = ref_8738 # MOV operation
ref_26471 = ref_17280 # MOV operation
ref_26580 = ref_26471 # MOV operation
ref_26592 = ref_24917 # MOV operation
ref_26594 = (ref_26592 | ref_26580) # OR operation
ref_26903 = ref_26594 # MOV operation
ref_26909 = (0x3F & ref_26903) # AND operation
ref_27218 = ref_26909 # MOV operation
ref_27226 = ((ref_27218 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_27233 = ref_27226 # MOV operation
ref_28536 = ref_8738 # MOV operation
ref_28645 = ref_28536 # MOV operation
ref_28657 = ref_27233 # MOV operation
ref_28659 = (ref_28657 | ref_28645) # OR operation
ref_28810 = ref_28659 # MOV operation
ref_31437 = ref_14713 # MOV operation
ref_32878 = ref_28810 # MOV operation
ref_33117 = ref_32878 # MOV operation
ref_33125 = (ref_33117 >> (0x1 & 0x3F)) # SHR operation
ref_33132 = ref_33125 # MOV operation
ref_33436 = ref_33132 # MOV operation
ref_33442 = (0xF & ref_33436) # AND operation
ref_33576 = ref_33442 # MOV operation
ref_33590 = (0x1 | ref_33576) # OR operation
ref_33876 = ref_33590 # MOV operation
ref_33878 = ((0x40 - ref_33876) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_33886 = ref_33878 # MOV operation
ref_34032 = ref_31437 # MOV operation
ref_34036 = ref_33886 # MOV operation
ref_34038 = (ref_34036 & 0xFFFFFFFF) # MOV operation
ref_34040 = ((ref_34032 << ((ref_34038 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_34047 = ref_34040 # MOV operation
ref_35229 = ref_14713 # MOV operation
ref_36670 = ref_28810 # MOV operation
ref_36909 = ref_36670 # MOV operation
ref_36917 = (ref_36909 >> (0x1 & 0x3F)) # SHR operation
ref_36924 = ref_36917 # MOV operation
ref_37228 = ref_36924 # MOV operation
ref_37234 = (0xF & ref_37228) # AND operation
ref_37368 = ref_37234 # MOV operation
ref_37382 = (0x1 | ref_37368) # OR operation
ref_37488 = ref_35229 # MOV operation
ref_37492 = ref_37382 # MOV operation
ref_37494 = (ref_37492 & 0xFFFFFFFF) # MOV operation
ref_37496 = (ref_37488 >> ((ref_37494 & 0xFF) & 0x3F)) # SHR operation
ref_37503 = ref_37496 # MOV operation
ref_37632 = ref_37503 # MOV operation
ref_37644 = ref_34047 # MOV operation
ref_37646 = (ref_37644 | ref_37632) # OR operation
ref_37797 = ref_37646 # MOV operation
ref_40032 = ref_21122 # MOV operation
ref_41586 = ref_37797 # MOV operation
ref_41677 = ref_41586 # MOV operation
ref_41689 = ref_40032 # MOV operation
ref_41691 = ((ref_41677 - ref_41689) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_41699 = ref_41691 # MOV operation
ref_41845 = ref_41699 # MOV operation
ref_45959 = ref_28810 # MOV operation
ref_47279 = ref_14713 # MOV operation
ref_47563 = ref_47279 # MOV operation
ref_47569 = (0xF & ref_47563) # AND operation
ref_47703 = ref_47569 # MOV operation
ref_47717 = (0x1 | ref_47703) # OR operation
ref_48003 = ref_47717 # MOV operation
ref_48005 = ((0x40 - ref_48003) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_48013 = ref_48005 # MOV operation
ref_48159 = ref_45959 # MOV operation
ref_48163 = ref_48013 # MOV operation
ref_48165 = (ref_48163 & 0xFFFFFFFF) # MOV operation
ref_48167 = ((ref_48159 << ((ref_48165 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_48174 = ref_48167 # MOV operation
ref_49356 = ref_28810 # MOV operation
ref_50676 = ref_14713 # MOV operation
ref_50960 = ref_50676 # MOV operation
ref_50966 = (0xF & ref_50960) # AND operation
ref_51100 = ref_50966 # MOV operation
ref_51114 = (0x1 | ref_51100) # OR operation
ref_51220 = ref_49356 # MOV operation
ref_51224 = ref_51114 # MOV operation
ref_51226 = (ref_51224 & 0xFFFFFFFF) # MOV operation
ref_51228 = (ref_51220 >> ((ref_51226 & 0xFF) & 0x3F)) # SHR operation
ref_51235 = ref_51228 # MOV operation
ref_51364 = ref_51235 # MOV operation
ref_51376 = ref_48174 # MOV operation
ref_51378 = (ref_51376 | ref_51364) # OR operation
ref_52723 = ref_21122 # MOV operation
ref_53885 = ref_41845 # MOV operation
ref_53994 = ref_53885 # MOV operation
ref_54006 = ref_52723 # MOV operation
ref_54008 = (ref_54006 | ref_53994) # OR operation
ref_54272 = ref_54008 # MOV operation
ref_54280 = (ref_54272 >> (0x1 & 0x3F)) # SHR operation
ref_54287 = ref_54280 # MOV operation
ref_54591 = ref_54287 # MOV operation
ref_54597 = (0x7 & ref_54591) # AND operation
ref_54731 = ref_54597 # MOV operation
ref_54745 = (0x1 | ref_54731) # OR operation
ref_54896 = ref_51378 # MOV operation
ref_54900 = ref_54745 # MOV operation
ref_54902 = (ref_54900 & 0xFFFFFFFF) # MOV operation
ref_54904 = ((ref_54896 << ((ref_54902 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_54911 = ref_54904 # MOV operation
ref_55057 = ref_54911 # MOV operation
ref_55352 = ref_55057 # MOV operation
ref_55354 = ref_55352 # MOV operation

print ref_55354 & 0xffffffffffffffff