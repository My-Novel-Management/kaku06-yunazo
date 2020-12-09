# -*- coding: utf-8 -*-
'''
About: "プロット"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


def main_notes(w: World):
    return (
            base_plot(w),
            chapter_plot(w),
            story_lines(w),
            plot_note(w),
            *mystery_note(w),
            fantasy_note(w),
            )


# world settings
def base_plot(w: World):
    return w.writer_note("基本プロット",
            "かつて$bossや$heroが存在した世界",
            "しかし$bossや$monsterの脅威は去り、世界は平和に暮らしていた",
            "ただその世界で幅を利かせていたのが「$hero利権」と呼ばれるもので、現在国を収める「女王」とその一族は$heroの末裔やその仲間の末裔たちである",
            "またかつては存在していた魔法・魔術は姿を消し、その力の源であった$enagyを動力源とする機械が誕生していた",
            "そんな世界で物語は進行する",
            "作品は記述者である「$wilson」の語りによって始まる",
            "彼がある事情で元勇者の血筋を引くらしい若者を探すのを依頼にやってくる",
            "それがどうも偏屈な若者で、奇妙な事件に首を突っ込んではあれこれと忠告していくという",
            "王立警察からひどくうとまれている存在だが腕は確かというので紹介してもらった",
            "そこに向かうと中に勝手に入れと言われて、その通りに奥に進むと、応接間でいきなり「帰れ」と言われて落とし穴に落とされそうになった",
            "依頼をしようと口を開くと、何を言う前から$wilsonの素性までぴたりと当てて、その上で「王室からの依頼は受けない」と断られる",
            "何とか依頼を受けてもらおうとしていると、そこに別の依頼人が飛び込んできて「助けてくれ」と",
            "そこから$wilsonは$sherlockという探偵と奇妙な事件に出くわすことになる",
            )


def story_lines(w: World):
    return w.writer_note("ストーリーライン",
            w.tag.title("基本のライン"),
            "ざっと見つかったものを挙げる",
            "勇者殺人事件",
            "$hero関係者失踪事件",
            "$boss復活儀式",
            "第二王女失踪事件（半年前から）",
            "謎の赤鎧クラブ",
            "宝剣盗難事件",
            "皇太子からの宝剣奪取依頼",
            "魔獣の伝説",
            "$morianoが黒幕",
            "謎の空き家の人影",
            w.tag.title("裏側で進行する全体に共通のもの"),
            "$hero関係者失踪事件",
            "$boss復活の兆候",
            "謎の宗教団体",
            "↓$moriano黒幕説",
            "↓偽物の$wilson",
            w.tag.title("$hero関係者殺人事件"),
            )


def chapter_plot(w: World):
    return w.writer_note("章構成",
            "プロローグ＋８章＋エピローグかな",
            "もしくは７章",
            w.tag.title("プロローグ"),
            "$wilson（記述者）の語り＋三人称で後から装飾して叙述されていると",
            "その記録された本を読んでいるというメタになっている",
            "更に$wilsonの知識は何故か現代人にねざしている（これは実は$wilsonが転生人だというオチ）",
            w.tag.title("１章"),
            "$wilsonが$sherlockを訪問し、依頼をしようとする",
            "そこで$sherlockの能力を見せつけられる",
            "依頼をしようとしたところに、殺人事件の容疑者になってしまった少女の疑いを晴らしてほしいと幼馴染から依頼がある",
            "現場にいってみると顔なじみの警官がいた",
            "事件概要は口論から父親を娘が殺してしまったというもので、少し前に口論しているのを目撃した人間がいた",
            "しかし実際はハメられただけで、$maryは無実だった",
            "$maryの無実を晴らしたものの、彼女は家族を失い、その身柄を$sherlockたちが引き取ることになった",
            w.tag.title("２章"),
            "改めて$wilsonは$sherlockに依頼内容を話す",
            "$wilsonは巷で密かに続いている謎の失踪事件を騙る",
            "彼が調べたところによると「勇者」の関係者ばかりが失踪しているという",
            "実は$sherlockも興味をもって調べていたがまだ謎が多くて情報が足りない",
            "そこにある依頼が持ち込まれる",
            "赤い鎧の人間だけがつける不思議な仕事があるというのだ",
            "そこに雇っている野良の騎士が通っているのだが、本当にこのまま続けてもいいものかと",
            "現場を確認し、すぐに理屈を見抜いた$sherlock",
            "それはある宗教団体が穴を掘るために護衛の片方を遠ざけていたのだと分かる",
            "しかし既にその何かの発掘を終えたために赤鎧クラブは解散してしまい、もう一人の護衛の兵士も行方不明になった（その後殺されて発見された）",
            w.tag.title("３章"),
            "仕事がなくなった赤鎧の無言騎士を引き取った$sherlockたち",
            "そこに王室から使者がやってくる",
            "どうやら皇太子の結婚相手が決まり、近々結婚するが、その皇太子がかつて懇意にしていた女性に宝剣を渡してしまい、それを取り戻してもらいたいというのだ",
            "巷で噂の怪盗にでも頼めばいいと突き返す$sherlock",
            "しかし同じ日に同じ人物がやってきて同じ依頼をしていく",
            "どうやら最初は何者かが変装して依頼をしていったらしい",
            "興味をもった$sherlockはとりあえずその女性$ailyに出会う",
            "実は$ailyのもとに宝剣はなく、それは既に噂の怪盗に盗まれてしまったという",
            "$sherlockたちは謎の怪盗を調べ始める",
            "調べていくうちに$ailyという女性が本当は存在していない事実にぶち当たる",
            "出会っていた$ailyこそが本物の怪盗$jackだった",
            w.tag.title("４章"),
            "青いガーネット",
            "ある日、市場の男が駆け込んでくる",
            "仕入れたニワトリから宝石が出てきたというのだ",
            "それもただの宝石ではなく、先日消えた宝剣についていた王国のガーネットだった",
            "怪盗$jackの仕業だと思い、調査を開始する",
            "しかし調べていくうちに",
            w.tag.title("５章"),
            "バスカヴィル家の犬",
            "ある田舎町。そこで魔犬による犠牲者が出た",
            "最近$monsterが凶暴化しているという話があったが、魔犬が出たとなれば$bossが本当に復活したのではないかという話も出てくる",
            "$sherlockは乗り気じゃなく、別の用事があるとでかけてしまい、$wilsonたちで調査を開始する",
            "そのとき目の前に巨大な魔犬が現れたのだった",
            w.tag.title("６章"),
            "魔犬に襲われた$maryたちを助けた謎の男は$sherlockだった",
            "ただしそれは本物ではなく幻術だという",
            "魔犬による猟奇殺人ではないと言い切る$sherlockは、件の屋敷に向かう",
            "そこに現在ただ一人残る主は自分が失った娘を生き返らせようと降霊術にはまっていた",
            "それが怪異を呼び出した、と主は言う",
            "しかし魔犬による無差別殺人はどうも主をこの屋敷から追い払いたい人物が仕組んだことらしかった",
            "",
            w.tag.title("７章"),
            "最後の事件",
            "$morianoの存在がついに浮かび上がる",
            "しかしその名にたどり着いたところでしょぼくれた老人が突然現れた",
            "$sherlockは$morianoと対峙するが、その圧倒的な存在と知性に置いていかれる",
            "$morianoが残した痕跡をたどり、彼の隠れ家を探し出す",
            "みんなが止めるのもきかずに$sherlockは単身、その湖畔の屋敷に乗り込む",
            "$morianoが全ての黒幕だと推理を突きつけ、これ以上は何もやらせないと宣言する",
            "$sherlockは彼の護衛をやりすごし、$morianoを闇の穴まで追い詰めた",
            "だが$morianoは$sherlockを道連れにしてその穴へと落ちてしまった",
            w.tag.title("８章"),
            "空き家の冒険",
            "失踪した$sherlockを探す$maryたち",
            "$sherlockなき事務所に妙な事件が持ち込まれる",
            "$wilsonたちはその空き家へと向かう",
            w.tag.title("エピローグ"),
            "偽物の$wilsonは自ら消滅した",
            "全ての事件の黒幕が消えたことで目的を推測するしかなくなった",
            "$sherlockは勇者の正当な血筋である自分を殺そうとしたと推測する",
            "本物の$wilsonが訪れ、$sherlockたちに正式に依頼するという形になる",
            )

def plot_note(w: World):
    return w.writer_note("プロットメモ",
            "基本路線は「長編１本」で、細かい事件や仲間集めを挟みつつ、冒険嫌いな勇者に冒険させるような展開",
            "１０万字の予定は以下のようにする",
            "短編（１万から２万字）を３本で５万字",
            "中編（５万字）を１本",
            "これで１冊分になるように調整する",
            "今回はホームズシリーズから色々と引っ張ってきて、そのタイトルをかぶせる",
            "冒険に出たくない勇者を大好きな「謎」を餌になんとか冒険させようとする、という形に",
            "ホームズ（初期型）とワトソン（クラデス）に、途中参加メンバーを加えてパーティにする",
            "勇者ということは隠しつつ、探偵です、の代わりに「勇者です」と言う",
            "「ただの謎解き好きな勇者です」",
            "全体を通して「緋色の研究」を。内容として細かく「踊る人形」とか入れていく",
            "ボヘミアの醜聞と赤毛組合、",
            "短編は基本的に「冒険」から引く",
            "１話は「緋色の研究の冒頭」＋「冒険」",
            "５話以降は「緋色の研究」のラストを使う。ワトソン役の$cradesが記述して残して研究していくことを決める",
            "勇者は「なぜ突然魔王が消えたのか」を知っていると$cradesと読者に思わせる",
            "１話で「$heroと$crades」コンビ結成かつ$heroの能力披露",
            "２話が$pan参加の話", "以前は「白馬に乗った王子伝説」",
            "３話が$emilの話", "大食い仮面騎士",
            "４話くらいで$ailの話ひっかけ",
            "５話からちょっと大型事件、連続殺人とか、密室殺人とか",
            "基本方針は「冒険の旅に出るまで」この街で事件解決をしつつ仲間や情報を揃える、が１巻",
            "全体の流れ：",
            "謎の殺人事件が裏で起こっている。関係者はかつて勇者に協力したとされる人間（事実ではなく噂であっても）",
            "最初は「簡単な依頼」を$cradesが持ってくる",
            "でもその事件を解決すると殺人事件に遭遇",
            "その容疑者に$pannaが選ばれる",
            "容疑を晴らすためにがんばる",
            "途中で謎の赤鎧組合が関わっているのを知る",
            "そこに潜んでいたのは「失踪中の第二王女」だった",
            "鎧の呪いを解いたが彼女は無口でしゃべらない",
            "四人の仲間と同居することになる",
            "ここまでが四話",
            "残りで怪盗と勇者連続殺人事件の真犯人を追い詰める",
            "実は$cradesが真犯人で、$cradesを名乗る別の人物だった",
            "$k_shalを$heroと確認し、滝壺に落とす",
            "しかし廃墟の冒険で生きていたことが分かり、$cradesを追い詰める",
            w.plot_note("１話（安楽椅子・ダイイングメッセージ）：$cradesが$heroを見つけて、魔王退治を依頼する。現場に行かずに事件解決（しかし情報間違っていたので後で推理し直す）"),
            w.plot_note("２話（アリバイ・人物偽装）：ボヘミアの醜聞。$ail登場"),
            w.plot_note("３話（事実誤認）：$pan仲間回。ボスコム警告の惨劇"),
            w.plot_note("４話（奇妙な設定）：$emil仲間回。赤毛組合。鎧騎士だけを集めた謎の組合"),
            w.plot_note("５話（密室）：くちびるのねじれた男"),
            w.plot_note("６話（クローズド）：犬の仕業みたいな謎の殺人事件発生"),
            w.plot_note("７話（奇妙な凶器）：魔獣の討伐依頼"),
            w.plot_note("８話（不可能犯罪）：$ail再登場し、警告"),
            w.plot_note("９話（見立て）：冒険嫌いの理由。"),
            w.plot_note("１０話（心理トリック）：$heroが滝に落ちる。ライヘンバッハの滝（最後の事件）"),
            w.plot_note("１１話（人物誤認）：実は謎の男の正体は$heroだった。空き家の冒険"),
            w.plot_note("１２話（叙述トリック）：戻ってきた$hero。実は$gradesは偽物で、連続殺人の真犯人だった"),
            w.plot_note("実は$cradesは魔王の使いで、勇者がまだ生きていることの確認とその殺害が目的だった"),
            w.plot_note("本物の$cradesは後になって登場する。ずっと謎の空間に閉じ込められていて、様々な時空を彷徨っていた"),
            )


def mystery_note(w: World):
    return (mystery_main(w),
            mystery_of_empty_house(w),
            )


def mystery_main(w: World):
    return w.writer_note('トリック設定',
            "できれば不可能犯罪っぽさを全体通して使いたい",
            w.tag.title("全体を通じて"),
            "叙述トリック",
            "記述者が犯人だった",
            w.tag.title("プロローグ"),
            "ここから叙述の始まり",
            w.tag.title("醜聞"),
            "密室殺人",
            "$ailyのことを調べにいったら、そこで謎の死体が発見される",
            "謎の死体、かつ、ずっと監視していた密室状態の家の中で殺されていた。誰も入っていないのに、という不可能犯罪",
            "実は$ailyという女は最初から存在しない",
            "見つかった死体はずっと失踪していた$heroの血縁の女性だった",
            "実は抜け穴があり、最初からこの屋敷は使っていなかった。$jackは家に入るなり抜け穴からすぐ外に出て、別の場所に向かった",
            "その抜け穴の存在を知っている誰かが、記憶も何も失っていた女を殺してここに放棄したのだった",
            w.tag.title("谷"),
            "アリバイトリック＆ダイイングメッセージ",
            "犯人は母親と繋がっていた使用人",
            "嘘の証言により犯人に仕立て上げた",
            "あと$animalなので、それがきっかけになっている",
            "ダイイングメッセージにより、犯人が$animalであるという偽装もしている",
            "ダイイングメッセージを何にするか。分かりづらいが推理できて、そうだと思える",
            w.tag.title("赤鎧"),
            "奇妙な仕事（偽装トリック）",
            "原作と同じトリックだが、そのままだとつまらない",
            "$limeが犯人に仕立て上げられるところから、の起死回生までやろう",
            "赤鎧の人間だけに仕事を与えるクラブがあった",
            "護衛仲間に頼まれてそこでこっそりバイトをする",
            "そうやって遠ざけておいて、もう一人が仲間を素通りさせる",
            "本当の目的は銀行の金庫内に補完されていた$stone",
            "そして仲間の護衛が殺されて発見される。その殺人犯人に$limeが仕立て上げられて、助けるところから",
            w.tag.title("ガーネット"),
            "奇妙な出来事（日常の謎）",
            "ガチョウから宝石を発見し、そこに$jackが隠していったことが分かるが、それとは別件で殺人事件が発生し、その凶器が一緒に見つかる",
            "$jackが殺人犯として疑われるものの、彼女は絶対にやっていない",
            "今回は彼女を助ける物語に",
            w.tag.title("魔犬"),
            "クローズド・サークル＆見立て殺人＆偽装トリック（犬による仕業に見せかける）",
            "陸の孤島と呼ばれる場所。そこで列車がとまり、行き来不能になり、数日閉じ込められる",
            "そこの屋敷の中で使用人や招待された人間が殺される",
            "連続殺人が起こり、本当に魔獣がいるのだと思わせる",
            "しかし実際はここの女主により、蘇らせた魔犬の食料になる人間を集めていただけだった",
            "報告さえしなければ殺人はなかったことになる",
            "そして伝説により寄り付かなくさせる",
            "殺害方法はいつも同じ。薬によって動かなくさせて、歯型の道具で千切る",
            "基本的には消失してしまうが、一部が見つかり、殺人事件発覚となる",
            w.tag.title("最後"),
            "暗号解読",
            "暗号をといていくとその先に「殺人事件」が転がっている",
            "それが$moriano関係者で、彼の残酷さと器用さを表すこと",
            "不可能犯罪で、容疑者は$sherlockになること",
            w.tag.title("空き家"),
            "すり替え",
            "叙述トリック明かす、がある",
            "殺人事件（不可能犯罪）が発生し、それと同じ手法で狙われる、みたいなのがいいかな",
            "その場に行かずに殺人を行う",
            "その装置を作った人間を探す",
            "その手法を$wilsonが思いつくが、実はそれは嘘の手法で、実際は普通に合鍵を使っただけだった",
            w.tag.title("エピローグ"),
            "叙述トリックを明かすのと、本物$wilson登場ですり替えマジック",
            "あと実はその$wilsonが「転生人」っぽいと伏線張る",
            w.tag.title("赤鎧組合"),
            "元ネタは「赤毛組合」",
            "赤鎧の人間を募集するという奇妙な内容だが、実はターゲットを守衛場所から遠ざけておくための手段",
            "その間にもぬけの殻となった場所で宝物を奪うための抜け穴を作ったりしていた",
            w.tag.title("$pannaが容疑者に"),
            "容疑者偽装トリック",
            "元ネタは「ボスコム谷の殺人」",
            "$cradesが持ってきた事件を解決したらそこに飛び込んできた新依頼がこれ",
            w.tag.title("元神官の男"),
            "$heroを訪れた時に何も聞かなくても「国王の差金」と見抜く",
            "元ネタは「緋色の研究」の冒頭部分",
            "ワトソンがアフガン帰りの軍医であることを見抜いたくだり",
            "文官ではなく現場である程度武道の心得があり、なおかつ$enagyの扱いにも長けている",
            w.tag.title("アクロイド殺し的な"),
            "記述者として「$crades」が登場しているが、実はその$cradesは偽物であり、本物は別のところにいた（療養という名目で温泉旅館を巡っていた）",
            "その間に$cradesに成り代わった闇のモノが$heroになる候補としての人間を殺すために調査に訪れていた",
            "空き家の事件なども$cradesが残った$pannaたちを事故に見せかけて殺害するために仕組んだ",
            "人知れぬ亡くなるのはほぼ$cradesか彼の指示、仕込みによるものだった",
            w.tag.title("ヴィルガスクの魔犬"),
            "元ネタは「バスカヴィル家の犬」",
            "魔犬の噂を流しておいて、実は普通に殺していただけだった",
            "一番の目的は人払い",
            "原作では伝説を作っておいて、あとで凶暴な猟犬を買い、それを手なづけて、心臓ショック死を狙っている",
            "狙いは遺産や財産になる",
            "今回は魔王復活の儀式から遠ざけるためである",
            "ある宗教団体のせいにしたが、実は$cradesが魔王復活を狙っていた",
            w.tag.title("最後の事件"),
            "元ネタは「最後の事件」",
            "これはホームズを処分するために作者が書いたもの",
            "ここで「教授」の存在がクローズアップされる",
            "しかしその教授の正体こそが$cradesだった",
            "彼が追っていたのはその影なのだ",
            "その影と同士討ちのようになり、闇の世界まで続くという滝に落ちてしまう",
            w.tag.title("空き家の事件"),
            "$heroを処分した$cradesは$pannaたちも処分しようと、廃墟の事件の調査をもちかける",
            "そこで事故に遭ったようにみせかけられ、睡眠薬で眠らされた彼女たちは絶体絶命の危機",
            "そこに最近街で見かけていた「鼻のひんまがった男」がちょうどやってきて彼女たちを助け出す",
            "自分のおんぼろホームに案内し、そこで正体を明かす",
            "この事件により彼は$cradesが殺人犯であることを確信するのだった",
            )


def mystery_of_empty_house(w: World):
    return w.writer_note("空き家事件のミステリ構成",
            w.tag.title("空き家殺人事件"),
            "空き家を監視していたら、夜に揉め事を目撃し、明けたら、人が死んでいた",
            "一連の謎の密室殺人事件の続き",
            "改造$gunによる殺人。センサーと監視カメラのように仕込みによって起動させる。あとで刑事の$patsonが回収する手はずになっている",
            "争っているのを装っていたのは$sherlockに似た殺人鬼",
            "実は$sherlockがおびき寄せるために使っていたが、それを$wilsonたちが利用した形",
            "目的は$sherlockを殺人犯に仕立て上げて、弁解のために表に出てこさせようとする",
            "しかし$sherlockはそれを理解していて、潜伏を続けていた",
            "一方、$maryが一人で勝手に$sherlockの容疑を晴らそうと立ち回り、その空き家から繋がっていた廃工場に行ってしまう",
            "その抜け穴は偽$sherlockが密室から消えた抜け道だった",
            "廃工場を発見した$maryをとりあえず拉致し、別の廃工場に監禁した",
            "$maryを囮にして$sherlockを誘い出そうとした",
            "$limeは$sherlockの家に手紙が送られたのを見る",
            "$maryを助けに向かう",
            "助けにやってきた$limeと、脱出を試みる$mary",
            "爆破準備されたところに救出に現れた$sherlock",
            "その$sherlockを偽$sherlockが殺そうと襲いかかるが、彼の準備（防具？）でなんとか助かり、逮捕できた",
            "空き家事件解決かに見えたが、$sherlockの家が燃やされる",
            "仕方なく$wilsonの家に移動し、",
            # TODO
            )


def fantasy_note(w: World):
    return w.writer_note("各話のファンタジィ要素",
            "$enagyと$magicが軸になる",
            "ただし$scienceとして体系化され、研究が進んでいる",
            "それに伴い、古来の$magicは廃れつつあり、忘れ去られた$missingになっている",
            "毎回装置や乗り物で何か出す（ワクワク感）",
            w.tag.title("プロローグ"),
            "最初の世界観提示ポイントとなり、$carを出す",
            "$carこそが$wilsonの存在価値になるので、ここが大事",
            "あとファンタジィ世界である、ということ、不思議な技術としての$magicが存在していることを想像させる（くらいでいい）",
            w.tag.title("1.醜聞"),
            "この世界の一般常識を示す。それでファンタジィの世界と認めてもらうように",
            "かつ、$heroも$bossも存在しなくなった、後の世界、という提示をしておく",
            "売買システム、お金の存在、交通や都市部の街の状況、市場の雰囲気などを",
            "また夜には電気の代わりに$enagyを使ったランプなどもあるが高額だと示す",
            "$magicが存在し、かつ、それが一般人には難しいが便利として利用されている現状を伝える",
            "王国があり、それが$heroの末裔によって支配、管理、権力を牛耳られていることを教える",
            w.tag.title("2.谷"),
            "駅の登場",
            "田舎町の雰囲気を見せる",
            "警察は地方警察で、そっちは全然$science捜査なんてないと見せる",
            "$trainはここで初登場にする",
            "$animalの存在を提示",
            "古代技術が生きていることの提示",
            w.tag.title("3.赤鎧"),
            "建築系の技術を中心にやること",
            "建設機械を何か",
            "銀行設備（金庫とか管理システムとか）",
            w.tag.title("4.ガーネット"),
            "",
            w.tag.title("5.魔犬"),
            "浄化槽（下水処理施設の都市部と地方の差）",
            w.tag.title("6.最後"),
            "",
            w.tag.title("7.空き家"),
            "$boss復活の祭壇",
            "発$enagy装置（発電機）的",
            w.tag.title("エピローグ"),
            "腕時計。これはこの時代には存在しないもので、$wilsonが現代人であることの証だが、そっと出しておく",
            )

