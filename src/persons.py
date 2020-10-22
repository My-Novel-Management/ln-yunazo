# -*- coding: utf-8 -*-
'''
About: "人物"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


# world settings
def main_notes(w: World):
    return (
            characters_note(w),
            )


def characters_note(w: World):
    return w.writer_note('人物設定',
            w.tag.title("主人公（勇者で探偵）"),
            "シャーロックという名前は使いたい",
            "知的でどこか病的でもあり勇者の血筋も引いていて$enagyの能力も秘めている",
            "ただそういったものを彼は「呪い」と捉えていてあまり人に知られたくはない",
            "第一巻では「勇者」であることを彼が認める、つまり自認の物語である",
            w.tag.title("ワトソン役（かつモリアーティ）"),
            "叙述トリックの肝心",
            "かつて王国の大神官にまでなった男を騙る、闇の住人",
            "かなり頭が切れ、主人公を途中まで見事に騙す",
            "しかし勇者である確証を得てからの行動でミスり、彼に誘導されて事故死に見せかけて処分したように勘違いさせられた",
            "名前はできればワトソンから何かもじったものがいい",
            "同じ名前の本人が二巻目以降、記述者の役割を担うことになる",
            w.tag.title("元パンナ"),
            "ヒロイン枠",
            "口うるさいタイプで感情豊か",
            "体型は子どもっぽいのがいいかな",
            "感が鋭いところが知的長所",
            w.tag.title("鎧役（女騎士）"),
            "第二のヒロイン枠",
            "呪いの鎧のせいでしゃべれない（後に呪いを解除されるがそれでも無口）",
            "実は王国の第二王女",
            "誘拐されたが呪いの鎧により逃亡に成功するも、そのせいで放浪の旅に",
            "何とか拾われて食い扶持を与えてもらっていた",
            )

