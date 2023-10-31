import requests
import uuid
import re
import time
def aiBytitle(title):
    url='https://api.binjie.fun/api/generateStream?refer__1360=n4RxBDyD9iiQ3DKDsuyrxAhADcjt4D'

    random_uid = uuid.uuid4()
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Access-Control-Request-Headers': 'content-type',
        'Access-Control-Request-Method': 'POST',
        'Origin': 'https://chat6.aichatos.top',
        'Referer': 'https://chat6.aichatos.top/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
    }

    payload = {
        "prompt": f"""
        我准备上传一个视频到哔哩哔哩，希望能够获得更多的关注和播放量，假设你是一个有经验的标题润色师，请你从我的视角帮我润色打磨一个引人注目的视频标题，视频标题可以采用夸张、比喻、排比、反问、反讽、讽刺、反问等艺术手法，以强调其影响力和吸引力，同时吸引观众的眼球，并根据此标题给出一个简短的视频介绍。最后严格按照如下格式给出回答结果,例如：视频标题：XXX  换行 视频简介：XXX 注意不要给出与问题无关的内容，请务必确保输出格式符合要求。
        我原本的标题是：{title} 。
        可以参考以下资料：激发观众好奇。好奇心是人的天性，所以在标题中设置悬念就尤为重要。比如《胆小的千万不要在百度上搜这几个字，后果很严重！》这个标题就容易引起观众的好奇心，观众们会好奇到底是哪几个字，也好奇搜索之后到底会出现什么结果，所以观众点开视频的可能性就很大。再比如《【未成年慎入】女生洗澡和男生洗澡有什么区别？》这个标题就有一种比较明显的暗示，也在观众的心理埋下了心矛，看见标题而划走的观众心里总会痒痒的。虽然观众们知道这个视频可能在欺骗我们，但观众们对这种具有色情意味的暗示还是欲罢不能，最终只好乖乖被骗进去。
引发观众共鸣、戳中观众痛点。所谓引发共鸣，就是替用户说出他的心里话，表达观众最想表达的观点，展示观众最想展示的态度。在大众们对于公益捐款产生信任危机的时候，这样一个《现在捐款我们更信韩红》的标题就替观众们表达了他们想要表达的观点，因此这个视频能给观众带来强烈的共鸣感。痛点就是观众们不愿提及的伤痛之处，比如钉钉的鬼畜曲《午夜凶钉》就戳中了疫情期间学生党、上班族被钉钉支配的恐惧。
制造强烈的预期。UP主们为了展现视频内容的实用性，就会为你植入非常强的预期。比如《一分钟学会两种小白也能做出来的流心蛋包饭！》这个标题就为你植入了快速学会蛋包饭的预期，对于厨房小白来说是非常具有诱惑力的。同理，《【PS小技巧】两分钟学会如何让模糊的照片变清晰》，在观众检索让照片变清晰的方法时，观众们会对比标题，他们觉得同样是PS教程，反正都能达到相同的结果，我不如去看一个更省时间的视频。这就是为观众植入内容实用性强的预期，为观众提供选择你的理由。
学会蹭知名度。蹭他人知名度的原理就是吸引与其垂类相同的粉丝的注意力。比如《我算出了这颗老番茄的尺寸，b站第一人》虽然这不是老番茄的视频，但也吸引了与老番茄垂类相同粉丝的注意力。再比如《【何同学】用何同学的方式打开2G》这部视频，用何同学的方式去制作内容，并非何同学的本人作品，却完美地蹭了一波何同学5G视频的热度，构思相当巧妙。
标题中可以多用数字。数字不仅可以提高标题的辨识度，而且UP主可以用数字表示时间、表示金钱、表示程度，实现更好强调效果。数字表示时间可以强调UP主做某件事所花的时间太多或太少，都可被视为稀奇的行为而成为一种看点。比如《受虐3天！我把史上最难的“自闭”游戏通关了！》这部视频就是用“3”这个数字来强调制作视频花费时间之多，以吸引观众的点击。再比如《73分钟看完柯南所有剧情！》这个标题就为观众植入了很强的预期，73分钟就能看完柯南所有剧情，对于想要了解柯南的观众来说非常有吸引力。除了时间之外，观众们还比较关心金钱。而用数字表示金钱会比汉字更为直观，也更容易形成多与少的对比。比如《2元和20元的泡面，有什么区别？》这种便宜与贵的对比视频要比单一的内容测评具有更多的信息量，UP主也更容易在视频的结尾做出一番总结，让观众收获感更强。因此这种不同价位的产品对比视频就成为了B站相对比较容易制作成功的视频类型。数字还可以代替形容词，表程度的多与少。小米手环4在广告词中写出：“有1600多万种颜色”其实翻译成行话就是，支持全彩RGB。RGB，每种颜色用2的8次方量化，共有2的24次方，约为1670w种颜色。小米手环4利用1600万这个数字作为宣传语，而不采用一些常规的说法去描述其色彩丰富的程度，更直观地强调了3代与4代最大的升级就是彩色表盘。既实现了较好的宣传效果，又不会增加观众的理解负担。再比如《【1周瘦腿计划表】全腿型，最少能瘦2CM》这个标题就表述出了见效之快，仅一周！瘦腿效果之好，瘦2CM！非常适合健身UP主模仿使用。
视频内容只为部分观众服务时，需要在标题中写清楚视频的受众范围。学生党、鬼畜区这些都可以成为视频受众的标签。当我们的内容只适合一部分人观看时，不妨在视频标题中添加受众标签。比如《我们，鬼畜区，向冠状病毒宣战！》这个标题非鬼畜区观众不会点开，而作为鬼畜区的观众就很可能会点开。点进视频的观众不一定是越多越好，某些观众不是你本视频的受众，对于你的内容肯定不感兴趣，从而拉低你的完播率和三连数据，导致视频被平台放弃推荐。所以，当我们的视频只为部分观众服务时，不妨在标题处打上预期的观众标签，只吸引符合视频定位的观众。
很多技巧需要你自己积累。少用晦涩的标题，让观众更快地了解你的含义。多用第一人称和第二人称，拉近彼此之间的距离。字数最好在12字以内，不超过24个字，避免标题冗长和手机端的显示折叠。重心前置，把核心卖点放在标题的最前面，第一时间吸引住观众的眼球。标题要保留神秘感、设置悬念，激起观众点击视频的兴趣，等等。
可以以偏概全，采用以偏概全的方法去拟定标题，能轻松地寻找到更吸引观众的视频卖点，这种卖点不需要我们亲力亲为，只需要引用一个案例、播放一段画面、编一个故事便可以到达相同的效果。如此简单高效，何乐而不为呢。
        最后我再次提醒你，请务必按照如下格式给出回答结果,例如：视频标题：XXX  换行 视频简介：XXX  
        """,
        
        
        "userId": f"#/{random_uid}",
        "network": True,
        "system": "",
        "withoutContext": False
    }

    response = requests.post(url, headers=headers, json=payload)
    #time.sleep(1)
    if response.status_code == 200:
        text=response.text
        # 使用正则表达式提取视频标题和视频简介的关键字及其内容
        pattern = r"(视频标题|视频简介)：(.+)"
        matches = re.findall(pattern, text)

        # 提取到的关键字及内容
        data = dict(matches)
        new_title=data.get('视频标题')
        new_content=data.get('视频简介')

        return new_title,new_content
    else:
        print("AI 润色失败")
        return title,None


a=aiBytitle("一张白纸，考出千万年薪？美国高分悬疑电影 最神秘的面试挑战！")
print(a)