# -*- coding: utf-8 -*-
'''
Story Config
============
'''

ASSET = {
        "PERSONS": (
            # (tag / name / full / age (birth) / job / call / info)
            ## main
            ("sherlock", "シャーロック", "ホーマー,シャーロック", 20,(1,1), "male", "勇者", "me:僕"),
            ("mary", "メアリー", "", 16,(1,1), "female", "武闘家", "me:ウチ"),
            ("wilson", "ウィルソン", "ハドル,ウィルソン", 40,(1,1), "元神官", "me:私"),
            ("lime", "ライム", "", 19,(1,1), "female", "騎士（王女）", "me:私"),
            ## sub
            ("mikel", "マイケル", "ホーマー,マイケル", 27,(1,1), "役人", "me:俺"),
            ("aily", "アイリー", "ルドラー,アイリー", 20,(1,1), "female", "王族", "me:私"),
            ("jack", "ジャック", "", 20,(1,1), "female", "盗賊", "me:私"),
            ("moriano", "モリアーノ", "ジェーンズ,モリアーノ", 50,(1,1), "教授", "me:私"),
            ## 少年探偵団
            ("ignes", "イグネス", "", 14,(1,1), "male", "市場の手伝い", "me:俺"),
            ## 市場
            ("nowlis", "ノーリス", "", 30,(1,1), "male", "市場の男性", "me:俺"),# NOTE: 本物のwilson
            ## kingdom
            ## police
            ("appolo", "アポロ", "リキュール,アポロ", 50,(1,1), "male", "警察（警視）", "me:私"),
            ("restrade", "レストラーデ", "グレイ,レストラーデ", 35,(1,1), "警察（警部）", "me:俺"),
            ## 谷の関連
            ("kean", "キーン", "クラウデン,キーン", 25,(1,1), "male", "使用人", "me:俺"),
            ("kail", "カイル", "クラウデン,カイル", 55,(1,1), "male", "使用人", "me:私"),
            ("jean", "ジェーン", "タイラー,ジェーン", 45,(1,1), "female", "婦人", "me:私"),
            ("royd", "ロイド", "タイラー,ロイド", 50,(1,1), "male", "不動産業", "me:私"),
            ## 赤鎧クラブ
            ("jakins", "ジェイキンス", "ジェイキンス,ルアン", 50,(1,1), "male", "質屋オーナー", "me:私"),
            ("bins", "ビンス", "ホールディング,ビンス", 25,(1,1), "male", "質屋バイト", "me:オレ"),
            ## ガーネット
            ## 魔獣
            ("cherry", "チェリー", "ヴィルヘルム,チェリー", 30,(1,1), "female", "婦人", "me:私"),
            ("moch", "モック", "ジリアン,モック", 35,(1,1), "male", "観光協会", "me:私"),
            ## プロローグ
            ("stanry", "スタンリー", "", 35,(1,1), "male", "不動産屋", "me:俺"),
            ## 最後の事件
            # モリアーノの後輩。殺される男
            ),
        "STAGES": (
            # (tag / name / parent / (geometry) / info)
            ("Office", "勇者探偵社", "London"),
            ("London", "ロムダス", "", (1000,1000)),# ロンドン
            ("Baker", "ベイリー", "London"),# ベイカー街
            ("Dartmour", "ダースモア", "London"),# ダートムア
            # ライヘンバッハ
            # ウェストミンスター駅
            # キングス・クロス駅
            # チャリング・クロス駅
            # ピカデリー・サーカス駅
            # ボンド街駅
            # グリニッジ駅
            # グリーンパーク駅
            # コヴェントガーデン駅
            # エンバクメント駅
            # オックスフォード・サーカス駅
            # オリンピア駅
            # オールドゲイト駅
            # オールドゲイト・イースト駅
            # カムデン・タウン駅
            # キャノン駅
            # キルバーン駅
            # グッジ街駅
            # クラパムコモン駅
            # クラパムサウス駅
            # クラパムノース駅
            # セント・ジェームズ・パーク駅
            # ヴィクトリア駅
            # アイランド・ガーデンズ駅
            # エッジウェア・ロード駅
            # エンジェル駅
            ),
        "DAYS": (
            # (tag / name / month / day / year)
            ("base_year", "基本年", 1,1, 1881),
            ),
        "TIMES": (
            # (tag / name / hour / minute)
            ),
        "ITEMS": (
            # (tag / name / cate / info)
            ("gun", "魔銃"),
            ("train", "魔導列車"),
            ("taxi", "魔導タクシー"),
            ("car", "魔導車"),
            ("stone", "魔石"),
            ),
        "WORDS": (
            # (tag / name / cate / info)
            ("G", "ポンド"),
            ("hero", "勇者"),
            ("boss", "魔王"),
            ("monster", "魔獣"),
            ("k_shal", "シャル"),
            ("enagy", "魔素"),
            ("magic", "魔導"),
            ("animal", "獣人"),
            ("elf", "エルフ"),
            ("werewolf", "人狼"),
            ("science", "魔学"),
            ("missing", "喪失知識"),
            ("cultX", "教団Ｘ"),
            ),
        "RUBIS": (
            # (origin / rubi / exclusions / always)
            ),
        }

# Title
TITLES = [
        "プロローグ",
        "第１章　皇太子の醜聞",
        "第２章　悲しみの谷",
        "第３章　謎の赤鎧クラブ",
        "第４章　ガチョウのガーネット",
        "第５章　魔獣伝説",
        "第６章　これが最後の事件",
        "第７章　空き家には気をつけろ",
        "エピローグ",
        ]

