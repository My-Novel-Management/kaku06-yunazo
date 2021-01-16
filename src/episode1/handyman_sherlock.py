# -*- coding: utf-8 -*-
'''
Episode 1-0: "便利屋$sherlock"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from config import TITLES


# NOTE: outlines
ABSTRACT = """
$wilsonはある依頼をする為に便利屋$sherlockの許を訪れる。
しかし$sherlockは$wilsonが説明する前から、彼がどういう人物で何を依頼しようとしているのかまで言い当て、挙げ句に「王室からの依頼は受けない」と断ってしまう。
$wilsonは諦めて立ち去ろうとするが、自分の$carに子供たちが群がっているのを見て追い払おうとしてからまれる。そこを通りかかりの少年$ignesに助けられた。
だが$sherlockが出てきて$ignesにすった財布を返すように言われて、少年は返して立ち去った。
$wilsonはこうして$sherlockとまともに話すことに。
家の中に入ると$sherlockは自分が色々な難事件や面倒なことを解決してきたが、その大半が王室経由の厄介事だったと吐露する。
だからもう二度と受けないと決めたと。
と、そこに王子の書簡を持った秘書の$adelがやってくる。
"""


# Scenes


# Episode
def main(w: World):
    return w.episode("便利屋$sherlock",
            # NOTE
            w.plot_setup("$wilsonは便利屋$sherlockに仕事を依頼に訪れる"),
            w.plot_turnpoint("$sherlockは$wilsonが話す前から彼の素性までを全て推理して言い当てる"),
            w.plot_develop("だが$sherlockは$wilsonが話す前から全てを言い当て、挙げ句に「王室からの依頼は受けない」と言い出す。$wilsonは何とか$sherlockに仕事を受けてもらおうとするが"),
            w.plot_turnpoint("$ignesに財布をすられたお陰で、$sherlockは家の中に入れてくれた"),
            w.plot_resolve("そこに王室執務官秘書$adelがやってきて王子からの依頼の書簡を置いていった"),
            w.plot_turnpoint("書簡には王室の印がされていた"),
            w.plot_note("$wilsonは$carで$Baker街にやってくる"),
            w.plot_note("都心部から少し離れた場所"),
            w.plot_note("通りを歩く人、子供たちもいる"),
            w.plot_note("その中に$ignes（特徴的な外見。真っ赤な髪が立っている子供）"),
            w.plot_note("他にも$aruru、$rumis、$refiがいる（後の少年探偵団）"),
            w.plot_note("目つきが鋭いホームレスなども"),
            w.plot_note("やはり高級住宅街とは人種が違うな、と思う$wilson"),
            w.plot_note("$sherlockの家を確認し、呼び鈴を鳴らす"),
            w.plot_note("覗き窓が開いて、いきなり「役人が何の用だ？」と"),
            w.plot_note("どうして分かったのか、と尋ねると一部の高級取りしか買えない$carに乗って、その仕立てのいいコートを羽織っている等"),
            w.plot_note("更に喋り方になまりがなく、人と普段から応対する仕事をしていると"),
            w.plot_note("そういった役人でここに用事があるのは決まって厄介事を持ち込んでくる"),
            w.plot_note("ゆえに「王室からの依頼は断る」だった"),
            w.plot_note("$wilsonは「変わった男」と聞いていたが、こんな風になんでもいい当ててしまうことに驚かされる"),
            w.plot_note("$sherlockは観察と推測でしかないと言うが"),
            w.plot_note("どうしようかと逡巡する$wilson"),
            w.plot_note("$carにさっきの子供が群がっているのを見つける"),
            w.plot_note("追い払いにいく"),
            w.plot_note("子供が喧嘩をしはじめる"),
            w.plot_note("それを止めようとする$wilson"),
            w.plot_note(""),# TODO
            outline=ABSTRACT)

