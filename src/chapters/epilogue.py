# -*- coding: utf-8 -*-
'''
Chapter "エピローグ"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from config import TITLES


## chapter
def main(w: World):
    return w.chapter(TITLES[-1],
            w.plot_setup("一連の事件の黒幕が$morianoではなく$wilsonだったと$sherlockは語る"),
            w.plot_turnpoint("本物の$wilsonがやってくる"),
            w.plot_develop("$wilsonは既に解決した事件の正式な書簡を見せ、$sherlockに仕事を依頼しようとする"),
            w.plot_develop("事情を全て聞かされた$wilson"),
            w.plot_turnpoint("そんな$wilsonに新しい書簡が届く"),
            w.plot_resolve("勇者直系の国王が暗殺されたという"),
            w.plot_resolve("その調査を依頼されるのだ"),
            w.plot_resolve("王室からの依頼は受けないといっていたが、それが自分の兄だと知り、仕方なく出向くことになった"),
            )

