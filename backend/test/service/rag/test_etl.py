import pytest
import service.rag.etl as rag_etl
import service.rag.rag_story_wangwangdui as rag_story_wangwangdui

@pytest.mark.skip(reason="manual run test")
def test_build_index():
    rag_etl.build_index()
    
    collection = rag_story_wangwangdui.get_collection()

    count = collection.count()
    assert count == 4

    result = collection.get()
    print(f"result: {result}")
    """
    {'
    ids': ['a64f7a86-c5fc-4583-863b-e26179796ad6', 'c48acafd-37d5-4fc1-8af1-fe6c93727ca9', 'cc215487-3e86-4c09-81b1-ede0abfd49f3', 'ce044ff1-36fb-4d03-a8d9-b46675e3e385'], 
    'embeddings': None, 
    'metadatas': [{'source': './story/走失的小野雁.txt', 'story_name': '走失的小野雁'}, {'source': './story/走失的小野雁.txt', 'story_name': '走失的小野雁'}, {'source': './story/走失的小野雁.txt', 'story_name': '走失的小野雁'}, {'source': './story/走失的小野雁.txt', 'story_name': '走失的小野雁'}], 
    'documents': [
        '“毛绒不见了？没有困难的工作，只有勇敢的狗狗。汪汪队，总部集合。“\n“莱德在呼叫。“\n“早安，小砾。“\n“帮帮忙，拜托谁开个灯吧。“\n“莱德队长，已经可以出动了。“\n“狗狗们，我们的自家后院有紧急情况。我们的野雁朋友必须跟着雁群迁移，可是却少了一只小野雁。“\n“可怜的毛绒，都是我害的。“\n“要是不快点找到它，雁群会丢下它的。阿奇，我需要你用扩音机来呼叫毛绒。“\n“包在我身上。“\n“还有毛毛，毛绒会跟着你到处走，我也需要你帮忙找它。“\n“我，火力全开。“\n“好的，汪汪队要出动了。“\n“阿奇，用扩音机放野雁的叫声。毛绒，好像没有反应啊。“\n“这是毛绒的。“\n“我对羽毛有点过敏，它走得是这边，它走得是这边。“\n“你好啊，小野雁，你要吃这块面包吗？“\n“毛绒，经过这里。“\n“你听，好像是毛绒。“\n“快看上面。“\n“那些海鸥在抢毛绒的面包。“\n“不要欺负比你小的野雁了。“\n“毛绒，快飞下来。“', 
        '“快看上面。“\n“那些海鸥在抢毛绒的面包。“\n“不要欺负比你小的野雁了。“\n“毛绒，快飞下来。“\n“它不能飞，那个汽水灌的塑胶环套出它的翅膀。“\n“它会摔下来。“\n“毛毛，快，用你的梯子救毛绒下来。“\n“火力全开，我来了，毛绒。“\n“用你的头盔。“\n“太好了，接的好，毛毛。我帮你拿掉塑胶环。“\n“我没事。“\n“毛绒，这是你的雁群，快点追上那群野雁吧。“\n“别担心，毛绒，等你飞回北方，就能再见面了；等你往南迁移，也会再见的，然后，你又飞回北方。“\n“毛毛，毛绒要快点走了，快去吧。你只拍动翅膀，就能追上的。“\n“拜拜，毛绒。我觉得它不想走。“\n“它现在不走的话，就永远追不上了，小野雁应该跟家人在一起，毛毛。“\n“那怎么办？“\n“有办法了。“\n“拜托不要飞的太高，不可以高过我的鼻子。“\n“毛毛，你拥有惧高症，你都可以爬过火车站的屋顶了。“', 
        '“是野雁。“\n“看到了吗？毛毛。“\n“没有，但是他们已经就快到了。“\n“用附近的树叶做窝，可以让飞来的野雁在这里睡觉。“\n“他们也会饿，吃这个应该会吧。“\n“面包，太棒了。“\n“不是野雁，不是野雁，它绝对不是野雁。“\n“那么那些呢？“\n“没错，是野雁。“\n“野雁来了。“\n“野雁来了。” \n“听到了。“\n“他们喜欢你的窝，灰灰。“\n“你要去哪里？小野雁。“\n“我去救它，你没事吧，小小毛绒。嗨，你很适合叫毛绒。去找家人吧，毛绒。“\n“做的好，毛毛。“\n“毛毛，你交了永远的野雁朋友。“\n“交了什么？“\n“你交了一个好朋友了。“\n“抱歉，毛绒。好了，毛绒，该去睡到稻草里了，或是窝里。我是可以陪你们一起睡在这里了，好了，但是就这一次哦。再见，野雁们，你们该走了，我们会想念你们的。毛绒呢？毛绒，你在哪里？它去哪里了？莱德，毛绒，它不见了。我们一定要在雁群离开前，找到它。“', 
        '“拜托不要飞的太高，不可以高过我的鼻子。“\n“毛毛，你拥有惧高症，你都可以爬过火车站的屋顶了。“\n“好吧，就这么办，让我们飞上天空吧。这不算高嘛！好吧，这就有点高了。“\n“来吧，毛绒，该起飞了。这就对了。“\n“别忘了，毛绒，要是你遇到麻烦，就呱呱求救。“\n“拜，毛绒，一路顺风，你这只傻小雁。“\n“你们今天表现得真是太棒了，真是一群乖狗狗。“\n“我也会，怎么是只鸡呢？“\n“哇，鸟类都很喜欢你的，毛毛。”'], 
    'uris': None, 
    'data': None, 
    'included': ['metadatas', 'documents']}
    """