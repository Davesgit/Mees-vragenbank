"""G8 batch 7 (VBN-E04 #6–#31): de b7-data (V-#944, V-#945, V-#946, Z-#943/Oef-#1004, Z-#945) en de bijbehorende guards (XSTER '(x 1000)', les 326 in
STAAF-BESLIS) gaan pas live als Oefeningen ronde 1b van patch_batch7 heeft geplaatst (steering 17:21: anders crasht b7/check op '×' en moet #21 tegelijk
met hun regelwijziging live). Aan sinds 17:27 (Oefeningen b7 ronde 1b, patch_batch7 17:26:20)."""
import os
ACTIEF = True or os.environ.get('G8_B7') == '1'
