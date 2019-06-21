# HA-serverchan
Homeassistant custom component to push notify message to weixin. Please report bugs to dengleer#126.com

Server酱 introduction:   
http://sc.ftqq.com/3.version   

Serverchan.py is poorly coded but a working version.  
Copy serverchan.py under .homeassistant/custom_components/notify. 

example  in configuration.yaml:   
notify:   
  \- name: weixin    
  
       platform: serverchan　　　　
       sc_key: xxxxxxxxxxxxxxxxxxxxxx   

Warn:"title" should NOT be null.

# HA-Qiyeweichat
Copy qiyewechat.py under .homeassistant/custom_components/notify

然后写配置文件：
notify:
  - platform: Qiyeweichat
    name: weixin_quanjia       #用于生成服务实体ID  比如这个出来就是notify.weixin_quanjia
    corpid: ***********       #这个是企业微信的企业id，https://work.weixin.qq.com/wework_admin/frame#profile 复制下网页底部的企业信息中的企业ID备用。
    agentId: ***********    #这个是企业微信里面新建应用的应用id 点击这里创建 https://work.weixin.qq.com/wework_admin/frame#apps/createApiApp
上传一个应用logo和自定义应用名字，其他默认。
    secret: ***********       #这个是企业微信里面新建应用的应用secret，创建后打开：https://work.weixin.qq.com/wework_admin/frame#apps 可以看到在 "应用"中的"自建"里有个应用。点进去打开 记录下 AgentId和Secret备用。
    touser: '@all'    #这里是发送个企业应用里面的全部人  当然  也可以设置指定的人的id  具体再企业微信里面设置


然后是服务的调用：

      - service: notify.weixin_quanjia
        data:
          title: "标题"
          message: 
            "类型|内容1|内容2|内容3"



其中：类型可以是“text，news， textcard， video
当类型为text   只需要内容1  
当类型为news   需要内容1和内容2和内容3   其中  内容1为显示的文字   内容2为点开的连接，，内容3为推送图片的连接
当类型为textcard    需要内容1和内容2  其中   内容1为显示的文字   内容2为点开的连接，，
当类型为video      需要内容1和内容2  其中  内容1为显示的文字   内容2为MP4文件的路径  比如 ，，{"title":"Homeassistant","message":"video|内容|/home/test/.homeassistant/1.mp4"}

mp4文件 只能10m以内,不过推送个10秒的监控   绰绰有余了,,,,,


以上的连接  都是指能够公网访问的连接。。。。。
