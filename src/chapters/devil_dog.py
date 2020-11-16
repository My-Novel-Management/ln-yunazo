# -*- coding: utf-8 -*-
'''
Chapter "魔獣"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from config import TITLES


# Episodes
def legend_of_darkdog(w: World):
    return w.episode("魔獣伝説",
            w.plot_note("$sherlockは怪奇事件の特集記事を読みながら「こんなものは実在しない」と言う"),
            w.plot_note("そもそも奇妙な現象、霊的なもの、不思議なものは人間が理解することを放棄していると説明する"),
            w.plot_note("小さい頃、学校内で七不思議というものがあったが、それを全て解明したらみんなから怒られたと"),
            w.plot_note("そこに$wilsonがこんな話がある、と、ある孤島に伝わる魔獣伝説を話した"),
            w.plot_note("そこはこの三年の間に六名もの犠牲者が出ているという"),
            w.plot_note("最初は飼い犬や家畜が殺されているだけだった"),
            w.plot_note("しかし最初に人の犠牲者が出た"),
            w.plot_note("それはどう見ても人の手によるものではなく、何か獣による被害だった"),
            w.plot_note("最初の事件から次の事件まではかなり時間が開いたが、直近はこの三ヶ月の間に二件も殺人事件が起こっている"),
            w.plot_note("$sherlockはそれだけ続くなら必ず人の手が関わっていると断言する"),
            w.plot_note("そこに招待状が届く"),
            w.plot_note("$wilsonはそれを開封し、噂をしていれば、とその伝説の孤島に暮らす城主からの招待状だと言った"),
            )


def first_murder(w: World):
    return w.episode("最初の犠牲者",
            "その夜、最初の犠牲者が出た",
            # TODO
            )


def second_murder(w: World):
    return w.episode("第二の犠牲者",
            "明確に誰かに殺された遺体が発見された",
            )


def exist_darkdog(w: World):
    return w.episode("魔獣は存在する",
            "そこに本物の魔獣が出現する",
            )


def real_murder(w: World):
    return w.episode("犯人",
            "$sherlockに犯人と指摘された女主人が逃げ出した",
            )


def sad_end(w: World):
    return w.episode("悲しい結末",
            w.plot_note("$sherlockは彼女を助けないと危ないという"),
            w.plot_note("しかし彼女が出ていった出口は閉ざされ、別の出入り口を探すしかなくなった"),
            w.plot_note("そうこうしているうちに島に到着した警察が、助けに入ってくる"),
            w.plot_note("やってきた$restradeに事情を説明し、$cherryを捜索してもらう"),
            w.plot_note("$sherlockは事件の真実を全て語った"),
            w.plot_note("事件の発端となったのは$cherryの愛犬が彼女の夫によって殺されたことだった"),
            w.plot_note("その恨みを晴らすために夫は事故死させられた"),
            w.plot_note("それに関わった人間が後で殺されている"),
            w.plot_note("彼女は魔獣を手に入れ、それにより殺害を行おうとしたが、魔獣は人殺しをしなかった"),
            w.plot_note("愛犬の代用となった魔獣は人の血が必要で、そのために彼女は自分の手で殺人を侵さざるを得なかった"),
            w.plot_note("彼女に協力していたのが地元の観光協会の男だった"),
            w.plot_note("その男が彼女を愛してしまい、今回の悲劇が訪れた"),
            w.plot_note("やっと到着した地元警察により$cherryが島の一番北側で魔獣に食い殺されている姿で発見された"),
            w.plot_note("魔獣は警察により射殺された"),
            )


def rebirth_ritual(w: World):
    return w.episode("蘇りの技法",
            "蘇りの秘法により起こった悲劇だった",
            w.plot_note("女主人$cherryの死去により事件は全てに幕を下ろした"),
            w.plot_note("死後に見つかった手記により今までの大半の事件の陰に彼女の存在があったことが判明する"),
            w.plot_note("$sherlockは死後に秘密の地下室を発見し、そこで儀式の跡を見た"),
            w.plot_note("図書館にやってきて、古文書を調べる"),
            w.plot_note("太古の技法で失われた魂を呼び戻す、闇の技法だった"),
            w.plot_note("本当に蘇らせたのだとわかる"),
            w.plot_note("$sherlockは彼女に接触しその技法を教えた$cultXのことをマークした"),
            w.plot_note("そこに情報がもたらされる"),
            w.plot_note("彼女が最後の$stoneの所有者だったという。しかし技法のために売り払い、今手元にはなかった"),
            w.plot_note("$sherlockは何者かが$stoneを四つ手に入れたのだと理解した"),
            )


# Chapter
def main(w: World):
    return w.chapter(TITLES[5],
            w.plot_setup("魔獣伝説のある場所で猟奇殺人事件が起こる"),
            w.plot_turnpoint("$sherlockの許にその孤島のパーティの招待状が届く"),
            w.plot_develop("$restradeの弟から事件解明を頼まれる"),
            w.plot_turnpoint("最初の殺人事件が起こる"),
            w.plot_develop("海は荒れて脱出も不可能になり、招待客は島に閉じ込められる"),
            w.plot_turnpoint("第二の被害者が出る"),
            w.plot_develop("$sherlockは獣による犯行ではないとして調査を開始する"),
            w.plot_turnpoint("本物の魔獣が出現する"),
            w.plot_develop("魔獣を殺そうとするが女主人が体を張って守ろうとする"),
            w.plot_turnpoint("$sherlockは女主人が犯人だと説明する"),
            w.plot_develop("女主人は魔獣とともに脱出を試みる"),
            w.plot_turnpoint("魔獣は女主人を食べてしまった"),
            w.plot_resolve("蘇りの秘法を使って$boss復活を願う宗教団体だったと判明する"),
            legend_of_darkdog(w),
            first_murder(w),
            second_murder(w),
            exist_darkdog(w),
            real_murder(w),
            sad_end(w),
            rebirth_ritual(w),
            )


