from core.role import get_role_by_code
from core.user import get_current_user
from core.summarization import get_summary_by_role_code


SYSTEM_PROMPT_TEMPLATE_SUFFIX = """
当前跟你对话的用户信息如下：
姓名：{user.name} 
小名：{user.nickname}
性别：{user.gender}
年龄：{user.age}
描述：{user.description}

基于之前总结的聊天总结和前几次的聊天记录进行回答，注意：如果你不清楚用户的问题，可以先问一下，然后再尝试回答。

当前聊天总结:
{summary}

要求：用100字内，用第一人称适合口语表达风格的话回答，尽可能用简单词汇通俗易懂有趣的方式介绍。已经说过的话不用多次说
"""

def get_system_prompt_by_role_code(role_code: int):
    role = get_role_by_code(role_code)
    system_prompt = role.prompt + \
        SYSTEM_PROMPT_TEMPLATE_SUFFIX.format(summary=get_summary_by_role_code(role_code), user=get_current_user())
    print("system_prompt: " + system_prompt)
    return system_prompt