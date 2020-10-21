# -*- coding: utf-8 -*-
'''
About: "プロット（トリック面）"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


# world settings
def mystery_note(w: World):
    return w.writer_note('トリック設定',
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

