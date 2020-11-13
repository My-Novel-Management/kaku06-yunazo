# -*- coding: utf-8 -*-
'''
Chapter "悲しみの谷"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from config import TITLES


## chapter
def main(w: World):
    return w.chapter(TITLES[2],
            w.plot_setup("田舎町で$gunを使った殺人事件が発生する"),
            w.plot_turnpoint("$sherlockのところにその容疑者になった女の子を助けてくれと電報が届く"),
            w.plot_develop("$sherlockと$wilsonはその田舎町に向かい、情報を集める"),
            w.plot_turnpoint("$maryが$animalだと$sherlockは言う"),
            w.plot_develop("$maryのことを調べていくと彼女が拾われた子供だと分かる"),
            w.plot_turnpoint("$maryが犯人に断定される"),
            w.plot_develop("$sherlockは真犯人を解明するために$maryの母親と使用人に再度話を聞く"),
            w.plot_turnpoint("$maryが獣化する"),
            w.plot_develop("母親を始末しようとした男から$maryが守るが、彼女の姿を見て殺人の自白をする母。逮捕された"),
            w.plot_turnpoint("$maryは財産贈与の全てを放棄した"),
            w.plot_resolve("保護者と住居を失った$maryが$sherlockの許にやってきて、居候させてとお願いした"),
            "$wilsonの依頼",
            w.plot_note("改めて$wilsonは$sherlockに依頼内容を語る"),
            w.plot_note("実はこの半年の間に謎の失踪事件が続いている"),
            w.plot_note("それは誰もが「$heroの血を引く者」だった"),
            w.plot_note("$heroとはかつて$bossを倒し、この世界に平和をもたらした存在とその仲間たちのことで、"),
            w.plot_note("現在この王国を始め、様々な重要部署を取り仕切っている"),
            w.plot_note("その中で血を濃く引くと言われているいくつかの家系がある"),
            w.plot_note("それぞれの家で直系の人間が失踪している"),
            w.plot_note("何か関連があるのか、あるとすればどんな力が働いているのか、それらを調べて報告してもらいたいと"),
            w.plot_note("$sherlockは新聞のスクラップを見せて「すでに興味がある事件だ」と答える"),
            w.plot_note("ただ情報が少ないので今すぐどうこうは言えないが、それでもある程度の推測は持っていると答えて、依頼を受けることにした"),
            "殺人事件",
            w.plot_note("そこに依頼の電報が舞い込む"),
            w.plot_note("内容はある殺人事件の容疑者となった女性を救って欲しいというものだった"),
            w.plot_note("$sherlockは$wilsonに車を出してもらい駅まで向かうことにした"),
            "谷の街",
            w.plot_note("駅まで迎えに来た少年$keanはある屋敷に務める使用人の家族の子だと自己紹介する"),
            w.plot_note("$sherlockはすぐにこの土地の大地主である$ln_royd家のものだと分かる"),
            w.plot_note("事件については現地についてから聞くことにして、まずこの街についての知識を確かめる$sherlock"),
            w.plot_note("街は大きな沼地で、昔は人家も少なく、作物もできず、その土地を購入した$ln_royd氏がここで育つ作物を見つけて財を成したらしい"),
            w.plot_note("谷の名前もそこからきている"),
            w.plot_note("屋敷は街の北側にあり、そこまで広大な湿原が広がっている"),
            w.plot_note("農場の手伝いもする$keanは事件が起こった場所で説明を始める"),
            "事件概要",
            w.plot_note("事件は呼び出された$royd氏とその娘である$maryが口論をしていて、翌朝、死体となって$royd氏が発見されたところから始まる"),
            w.plot_note("口論の現場を目撃したのは使用人の$kail（$keanの父）で、その証言と現場で発見されたナイフについていた$maryの指紋から容疑者が確定している"),
            w.plot_note("現場は湿原で、酷い雨により足跡は全て書き消えてしまっている"),
            w.plot_note("だが使用人である$keanは$maryを父親が溺愛していたことをよく知っていた"),
            w.plot_note("だから絶対に彼女は殺害していないと断言し、なんとか助けてくれないかと$sherlockの噂をきいて頼んだ"),
            "邸宅",
            w.plot_note("容疑者である$maryは警察に聴取で出向いて不在だった"),
            w.plot_note("残された奥さん$jeanは$sherlockたちを歓迎していない"),
            w.plot_note("対応は使用人の$kailがやってくれた"),
            w.plot_note("$roydに前妻を事故で失っていた"),
            w.plot_note("後妻である$jeanを迎えたのは五年前"),
            w.plot_note("遺書により莫大な遺産は全て家族に残すことになっている"),
            w.plot_note("殺害のあった日、$jeanは珍しく娘と夫が口をきかない朝食だったと証言する"),
            w.plot_note("もともと病気持ちで、そう身体の丈夫でなかった夫は最近食欲もなく、何かふさぎ込んでいたとも"),
            w.plot_note("何か悩んでいたようだ"),
            "$maryとの面会",
            w.plot_note("警察はよく世話をしている$restradeのツテを利用して、$maryと面会させてもらった"),
            w.plot_note("$maryは物静かな少女で、小柄。なぜか帽子や長いドレスで露出を少なくしている"),
            w.plot_note("彼女は小さな声で「やってない」とだけ答える"),
            w.plot_note("ただ口論していたことは認めるし、あんな時間に外出したことも証言した"),
            w.plot_note("ただその内容については語りたがらない。黙秘すると"),
            w.plot_note("$sherlockは一旦その場を離れる"),
            "$maryは実は$animal",
            w.plot_note("もう一度調べると$sherlockは現場に戻る"),
            w.plot_note("$wilsonに$maryに対して違和感がなかったか尋ねる"),
            w.plot_note("彼女は「$animal」だと教える"),
            w.plot_note("$animalとは昔存在した闇の世界の種族の一つで、人間に外見が似ているが一部や全部が動物の性質を持つ中間的な存在"),
            w.plot_note("他にも神官になっている$elfなど、古の種族と呼ばれているものがいくつかいる"),
            w.plot_note("どこかにその特徴が現れてきたのだろう"),
            w.plot_note("$wilsonは口論はそのことについてだろうと"),
            w.plot_note("現場を調べると動物の体毛が落ちている"),
            w.plot_note("彼女は$werewolfだと断言する"),
            w.plot_note("もし獣化して襲ったのだとしたら、なぜ現場にナイフが落ちていたのだろうか"),
            "$sherlockの解説",
            w.plot_note("翌日、$sherlockは邸宅に向かう"),
            w.plot_note("玄関先で$keanが口論していた。どうやら父親の方は完全に$maryが犯人と決めつけているようだ"),
            w.plot_note("$sherlockはその二人に声をかけ、部屋を用意してもらう"),
            w.plot_note("部屋に婦人も訪れ、そこで改めて推理した状況の説明を始める$sherlock"),
            w.plot_note("あの日の夜、$royd氏はある理由があり、娘の$maryを連れてあの場所にいった"),
            w.plot_note("あそこは氏が彼女を拾った場所だからだ"),
            w.plot_note("氏が建てたという小さなお堂があった"),
            w.plot_note("おそらくその時から氏は全てを知っていたのだ"),
            w.plot_note("そしてそのことを打ち明けるために呼び出した。それが口論の原因"),
            "母と子",
            w.plot_note("そこに警官が訪れて、$maryを連れてくる"),
            w.plot_note("$maryは全てを聞いていた"),
            w.plot_note("あそこでどんな話があったか告白する"),
            w.plot_note("$maryは父親から自分が養子ではなく、拾われた捨て子で、かつ、$werewolfであると聞かされた"),
            w.plot_note("最近身体の変化に気づいていた彼女は、自分が闇の一族と嫌悪されている"),
            w.plot_note("帽子を取ると小さな耳が見えた"),
            w.plot_note("それに母親は叫ぶ"),
            w.plot_note("そんな子供はほしくないと"),
            "事件の真相",
            w.plot_note("$sherlockは母親の$jeanも$maryが人間ではないことにうすうす気づいていて、この家から追い出したいと思っていたことを当てる"),
            w.plot_note("$keanが$jeanが本当の殺人犯か、と言うが"),
            w.plot_note("$sherlockは違うと言う"),
            w.plot_note("本当の犯人は目撃者である$keanの父親である$kailだった"),
            w.plot_note("ずっと片思いしていた$jeanの役に立ちたかった"),
            w.plot_note("そのために、少しずつ薬をいれて、身体を弱らせていた"),
            w.plot_note("死期が近いことを悟った$roydは娘に全財産を残そうとした"),
            w.plot_note("その遺言状を書き換え、そのうえで娘に罪をなすりつけることで全財産とこの家と土地の全てを手に入れようとした"),
            w.plot_note("そこであの偽装を考えた"),
            w.plot_note("実は最初から愛情はなく、$jeanはこの家の乗っ取りを考えていた"),
            w.plot_note("$jeanと$keanは幼馴染で、同じ施設に入っていた"),
            "居候",
            w.plot_note("事件は$jeanと$keanが逮捕され、解決を迎えた"),
            w.plot_note("邸宅や土地などの全てが$maryの持ち物となったが、彼女は未成年で、後見人はいない"),
            w.plot_note("だが$maryは全てを放棄し、地元に寄付をすると言い出した"),
            w.plot_note("父親のことを見守りながらも、息子の$keanはいつか帰ってこられるように邸宅の掃除とかをするらしい"),
            w.plot_note("事件を振り返っていた$sherlockと$wilsonのところに、訪問者がくる"),
            w.plot_note("$maryがやってきて、大きな荷物を持っている"),
            w.plot_note("「これからお世話になります」と押しかけてきた"),
            )


