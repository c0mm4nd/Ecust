# Ecust （Unofficial Api）
华理的小朋友看过来啦~做华理专属APP必备！——华理（本科生）模拟登陆源码<del>（PHP）</del> (Python)

<del>本人网站：cmd.ecustcic.com</del>

顺便安利：<del>ecustcic.com在我在学校这几年可以提供二级域名给大家方便华理学子实验学习</del> （已转交CIC）

<del>【最主要还是不用记ip不用买老外的不用备案省心省力。。。</del>

忘了说了本人<del>CIC会长</del>(现在已经退休2333)

##文件说明：

___old_version(PHP):___
    ___Ecust_login.php___
___已废弃___

__new_version__ (python):
在html处理方面，py的确非常方便。
    app.py:主程序
    JWC_login.py：教务处登录模块
    JWC_func.py：教务处相关功能模块
    URP_login.py：信息门户登录模块

    2016.1.30：增加changePW、curl_POST
    2016.1.31：修正curl的错误，增加选课信息查询XuanKeXinXi
    2016.2.2：改动：完善了XuanKeXinXi，开始准备接口部署，确认下一步目标为考试表
    2016.2.9: 增加个人信息，初步完善考试表，准备导入simple_html_dom库方便点，预期推出邮箱提醒课程服务
    2016.3.31: 于Viewstate原因无法实现登录，可能弃坑。。。毕竟实时维护做不到而且viewstate这个真不太懂。。。
    2016.5.5: 功能恢复，增加课程表查询
    2016.5.30: 决定用Python改写减小维护成本，PHP仅作接口用
    2016.8.11: 核心完成改写，逐步增加功能。新增信息门户的登录（坑
    2016.9.24: 


##接口使用：
~~接口还没写orz~~

~~如果不出意外的话应该只会有Get接口= =【个人不太喜欢Post太烦了~~

~~输出肯定是json~~

专心造轮子写手册，接口另做项目（看情况咯）

2016.8.11: 接口将托管于Ecust.Top
