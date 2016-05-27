using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using Google.ProtocolBuffers;
using com.gexin.rp.sdk.dto;
using com.igetui.api.openservice;
using com.igetui.api.openservice.igetui;
using com.igetui.api.openservice.igetui.template;
using com.igetui.api.openservice.payload;
using System.Net;



/**
 * 
 * 说明：
 *      此工程是一个测试工程，所用的相关.dll文件，都已经存在protobuffer文件里，需要加载到References里。
 *      工程中还有用到一个System.Web.Extensions文件，这个文件是用到Framework里V4.0版本的，
 *      一般路径如下：C:\Program Files\Reference Assemblies\Microsoft\Framework\.NETFramework\v4.0，
 *      或如下路径：C:\Program Files\Reference Assemblies\Microsoft\Framework\v3.5
 *      没有的也可以在protobuffer文件夹里找到。
 *      如再有问题，请直接联系技术客服，谢谢！
 *      GetuiServerApiSDK：此.dll文件为个推C#版本的SDK文件
 *      Google.ProtocolBuffers：此.dll文件为Google的数据交换格式文件
 *  注：
 *      新增一个连接超时时间设置，通过在环境变量--用户变量中增加名为：GETUI_TIMEOUT 的变量（修改环境变量，电脑重启后才能生效），值则是超时时间，如不设定，则默认为20秒。
 **/
namespace GetuiServerApiSDKDemo
{
    public class demo
    {
        //参数设置 <-----参数需要重新设置----->
        //http的域名
        private static String HOST = "http://sdk.open.api.igexin.com/apiex.htm";

        //https的域名
        //private static String HOST = "https://api.getui.com/apiex.htm";


        private static String APPID = "";                     //您应用的AppId
        private static String APPKEY = "";                    //您应用的AppKey
        private static String MASTERSECRET = "";              //您应用的MasterSecret 
        private static String CLIENTID = "";        //您获取的clientID
  
        private static String CLIENTID1 = "";
        private static String ALIAS = "请输入别名";
        private static String ALIAS1 = "别名1";
        private static String DeviceToken = "";  //填写IOS系统的DeviceToken

        static void Main(string[] args)
        {
            //toList接口每个用户状态返回是否开启，可选
            Console.OutputEncoding = Encoding.GetEncoding(936);
            Environment.SetEnvironmentVariable("needDetails", "true");

            //通过代理访问需要自行配置代理
            //System.Net.WebRequest.DefaultWebProxy = new WebProxy("192.168.1.108", 808);


            /*
             服务端推送接口，支持三个接口推送
             *      1.PushMessageToSingle接口：支持对单个用户进行推送
             *      2.PushMessageToList接口：支持对多个用户进行推送，建议为50个用户
             *      3.pushMessageToApp接口：对单个应用下的所有用户进行推送，可根据省份，标签，机型过滤推送
             */
            //1.1   PushMessageToSingle接口
           // PushMessageToSingle();
            //1.2 PushMessageToSingleBatch接口
            //PushMessageToSingleBatch();

            //2.PushMessageToList接口
            //PushMessageToList();

            //3.pushMessageToApp接口
            //pushMessageToApp();

            //4.任务停止功能
            //taskStop();
            //5.用户状态返回
            //getUserStatus();
				
		      	//6.APN简化推送
            apnPush();

            //7.ClientId设置标签
            //setTag();

            //8.ClientId自定义别名功能
                //a.单个Client自定义别名
            //bindAlias();
                //b.根据clientid查询别名
            //queryAlias();
                //c.根据别名查询ClientId
            //queryClientId();
                //d.单个ClientId解除绑定
                //aliasUnBind();
                //e.批量ClientId绑定相同别名
                //bindAliasAll();
                //f.根据别名解除所有ClientId绑定
                //aliasUnBindAll();

            //9.获取推送状态
            //getPushResult();
            //10.根据ClientID获取用户标签
            //getUserTags();
            //11.根据appid获取注册登录量信息
            //queryAppUserDataByDate();
            //12.根据appid获取某天下发信息
            //queryAppPushDataByDate();
        }

        public static void getPushResult() {
            IGtPush push = new IGtPush(HOST, APPKEY, MASTERSECRET);
            //String ret = push.getPushResult("OSA-0312_oPv6vL62zgA3JU942ZO3S");
            //System.Console.WriteLine(ret);

            //System.Console.WriteLine(push.queryAppPushDataByDate(APPID, "20150612"));
            System.Console.WriteLine(push.queryAppUserDataByDate(APPID, "20150525"));

            
        }

        public static void getUserTags() {
            IGtPush push = new IGtPush(HOST, APPKEY, MASTERSECRET);
            String ret = push.getUserTags(APPID,CLIENTID);
            System.Console.WriteLine(ret);
        }

        public static void bindAlias() {
            IGtPush push = new IGtPush(HOST, APPKEY, MASTERSECRET);
            String ret = push.bindAlias(APPID, ALIAS, CLIENTID);
            System.Console.WriteLine(ret);
        }

        public static void queryAlias()
        {
            IGtPush push = new IGtPush(HOST, APPKEY, MASTERSECRET);
            String ret = push.queryAlias(APPID, CLIENTID);
            System.Console.WriteLine(ret);
        }

        public static void queryClientId()
        {
            IGtPush push = new IGtPush(HOST, APPKEY, MASTERSECRET);
            String ret = push.queryClientId(APPID, ALIAS);
            System.Console.WriteLine(ret);
        }

        public static void aliasUnBind()
        {
            IGtPush push = new IGtPush(HOST, APPKEY, MASTERSECRET);
            String ret = push.unBindAlias(APPID, ALIAS, CLIENTID);
            System.Console.WriteLine(ret);
        }

        public static void bindAliasAll()
        {
            IGtPush push = new IGtPush(HOST, APPKEY, MASTERSECRET);
            List<com.igetui.api.openservice.igetui.Target> Lcids = new List<com.igetui.api.openservice.igetui.Target>();
            com.igetui.api.openservice.igetui.Target target = new com.igetui.api.openservice.igetui.Target();
            target.clientId = CLIENTID;
            target.alias = ALIAS;

            com.igetui.api.openservice.igetui.Target target1 = new com.igetui.api.openservice.igetui.Target();
            target1.clientId = "7c6edf411568c5db12e565425e4a381633";
            target1.alias = ALIAS1;


            Lcids.Add(target);
            Lcids.Add(target1);

            String ret = push.bindAlias(APPID, Lcids);
            System.Console.WriteLine(ret);
        }

        public static void aliasUnBindAll()
        {
            IGtPush push = new IGtPush(HOST, APPKEY, MASTERSECRET);
            String ret = push.unBindAliasAll(APPID, ALIAS);
            System.Console.WriteLine(ret);
        }

        public static void setTag() {
            IGtPush push = new IGtPush(HOST, APPKEY, MASTERSECRET);

            List<String>  list=new List<String>();
            list.Add("");
            String ret =push.setClientTag(APPID, CLIENTID, list);
            System.Console.WriteLine(ret);
        }


        public static void taskStop()
        {
            IGtPush push = new IGtPush(HOST, APPKEY, MASTERSECRET);
            Boolean result = push.stop("OSA-1126_L8v85pqZfCApbivwfHwZk5");
            System.Console.WriteLine("-----------------------------------------------");
            System.Console.WriteLine(result);
        }

        public static void queryAppUserDataByDate()
        {
            IGtPush push = new IGtPush(HOST, APPKEY, MASTERSECRET);
            String ret = push.queryAppUserDataByDate(APPID, "20150910");
            System.Console.WriteLine(ret);
        }

        public static void queryAppPushDataByDate()
        {
            IGtPush push = new IGtPush(HOST, APPKEY, MASTERSECRET);
            String ret = push.queryAppPushDataByDate(APPID, "20150910");
            System.Console.WriteLine(ret);
        }

		static void apnPush()
        {

            //APN简单推送
            //IGtPush push = new IGtPush(HOST, APPKEY, MASTERSECRET);
            //APNTemplate template = new APNTemplate();
            //APNPayload apnpayload = new APNPayload();
            //SimpleAlertMsg alertMsg = new SimpleAlertMsg("");
            //apnpayload.AlertMsg = alertMsg;
            //apnpayload.Badge = 11;
            //apnpayload.ContentAvailable = 1;
            //apnpayload.Category = "";
            //apnpayload.Sound = "com.gexin.ios.silence";
            //apnpayload.addCustomMsg("", "");
            //template.setAPNInfo(apnpayload);

            //APN高级推送
            IGtPush push = new IGtPush(HOST, APPKEY, MASTERSECRET);
            APNTemplate template = new APNTemplate();
            APNPayload apnpayload = new APNPayload();
            DictionaryAlertMsg alertMsg = new DictionaryAlertMsg();
            alertMsg.Body = "";
            alertMsg.ActionLocKey = "";
            alertMsg.LocKey = "";
            alertMsg.addLocArg("");
            alertMsg.LaunchImage = "";
            //IOS8.2支持字段
            alertMsg.Title = "";
            alertMsg.TitleLocKey="";
            alertMsg.addTitleLocArg("");

            apnpayload.AlertMsg = alertMsg;
            apnpayload.Badge = 10;
            apnpayload.ContentAvailable = 1;
            apnpayload.Category = "";
            apnpayload.Sound = "";
            apnpayload.addCustomMsg("", "");
            template.setAPNInfo(apnpayload);



            /*单个用户推送接口*/
            //SingleMessage Singlemessage = new SingleMessage();
            //Singlemessage.Data = template;
            //String pushResult = push.pushAPNMessageToSingle(APPID, DeviceToken, Singlemessage);
            //Console.Out.WriteLine(pushResult);
            
            /*多个用户推送接口*/
            ListMessage listmessage = new ListMessage();
            listmessage.Data = template;
            String contentId = push.getAPNContentId(APPID, listmessage);
            //Console.Out.WriteLine(contentId);
            List<String> devicetokenlist = new List<string>();
            devicetokenlist.Add(DeviceToken);
            String ret = push.pushAPNMessageToList(APPID, contentId, devicetokenlist);
            Console.Out.WriteLine(ret);
        }

        //PushMessageToSingle接口测试代码
        private static void PushMessageToSingle()
        {
            // 推送主类
            //根据HOST判断是http还是https
            IGtPush push = new IGtPush(HOST,APPKEY, MASTERSECRET);
            //http接口的访问模式
            //IGtPush push = new IGtPush(APPKEY, MASTERSECRET, false);
            //https接口的访问模式
            //IGtPush push = new IGtPush(APPKEY, MASTERSECRET, true);

            /*消息模版：
                1.TransmissionTemplate:透传模板
                2.LinkTemplate:通知链接模板
                3.NotificationTemplate：通知透传模板
                4.NotyPopLoadTemplate：通知弹框下载模板
             */
             
            TransmissionTemplate template =  TransmissionTemplateDemo();
            //NotificationTemplate template =  NotificationTemplateDemo();
            //LinkTemplate template = LinkTemplateDemo();
            //NotyPopLoadTemplate template = NotyPopLoadTemplateDemo();
            template.TransmissionContent = "测试";

            // 单推消息模型
            SingleMessage message = new SingleMessage();
            message.IsOffline = true;                         // 用户当前不在线时，是否离线存储,可选
            message.OfflineExpireTime = 1000 * 3600 * 12;            // 离线有效时间，单位为毫秒，可选
            message.Data = template;
            message.PushNetWorkType = 0;        //判断是否客户端是否wifi环境下推送，1为在WIFI环境下，0为非WIFI环境

            com.igetui.api.openservice.igetui.Target target = new com.igetui.api.openservice.igetui.Target();
            target.appId = APPID;
            //target.clientId = CLIENTID;
            target.alias = ALIAS;

            try
            {
                String pushResult = push.pushMessageToSingle(message, target);

                System.Console.WriteLine("-----------------------------------------------");
                System.Console.WriteLine("-----------------------------------------------");
                System.Console.WriteLine("----------------服务端返回结果：" + pushResult);
            }
            catch (RequestException e)
            {
                String requestId=e.RequestId;
                String pushResult = push.pushMessageToSingle(message, target, requestId);
                System.Console.WriteLine("-----------------------------------------------");
                System.Console.WriteLine("-----------------------------------------------");
                System.Console.WriteLine("----------------服务端返回结果：" + pushResult);
            }
        }

        private static void PushMessageToSingleBatch()
        {
            // 推送主类
            IGtPush push = new IGtPush(HOST, APPKEY, MASTERSECRET);
            IBatch Batch = push.getBatch();

            /*消息模版：
                1.TransmissionTemplate:透传模板
                2.LinkTemplate:通知链接模板
                3.NotificationTemplate：通知透传模板
                4.NotyPopLoadTemplate：通知弹框下载模板
             */

            TransmissionTemplate template = TransmissionTemplateDemo();
            //NotificationTemplate template =  NotificationTemplateDemo();
            //LinkTemplate template = LinkTemplateDemo();
            //NotyPopLoadTemplate template = NotyPopLoadTemplateDemo();
            template.TransmissionContent = "测试";


            // 单推消息模型
            SingleMessage message = new SingleMessage();
            message.IsOffline = true;                         // 用户当前不在线时，是否离线存储,可选
            message.OfflineExpireTime = 1000 * 3600 * 12;            // 离线有效时间，单位为毫秒，可选
            message.Data = template;
            //message.PushNetWorkType = 1;        //判断是否客户端是否wifi环境下推送，1为在WIFI环境下，0为非WIFI环境

            com.igetui.api.openservice.igetui.Target target = new com.igetui.api.openservice.igetui.Target();
            target.appId = APPID;
            target.clientId = CLIENTID;

            Batch.add(message, target);

            try
            {
                String pushResult = Batch.submit();

                System.Console.WriteLine("-----------------------------------------------");
                System.Console.WriteLine("-----------------------------------------------");
                System.Console.WriteLine("----------------服务端返回结果：" + pushResult);
            }
            catch (Exception e)
            {
                String pushResult = Batch.retry();
                System.Console.WriteLine("-----------------------------------------------");
                System.Console.WriteLine("-----------------------------------------------");
                System.Console.WriteLine("----------------服务端返回结果：" + pushResult);
            }
        }
        //PushMessageToList接口测试代码
        private static void PushMessageToList()
        {
            IGtPush push = new IGtPush(HOST, APPKEY, MASTERSECRET);

            ListMessage message = new ListMessage();
            /*消息模版：
                 1.TransmissionTemplate:透传功能模板
                 2.LinkTemplate:通知打开链接功能模板
                 3.NotificationTemplate：通知透传功能模板
                 4.NotyPopLoadTemplate：通知弹框下载功能模板
             */

            TransmissionTemplate template =  TransmissionTemplateDemo();
            //NotificationTemplate template =  NotificationTemplateDemo();
            //LinkTemplate template = LinkTemplateDemo();
            //NotyPopLoadTemplate template = NotyPopLoadTemplateDemo();
            template.TransmissionContent = "测试";

            message.IsOffline = true;                         // 用户当前不在线时，是否离线存储,可选
            message.OfflineExpireTime = 1000 * 3600 * 12;            // 离线有效时间，单位为毫秒，可选
            message.Data = template;
            //message.PushNetWorkType = 0;             //判断是否客户端是否wifi环境下推送，1为在WIFI环境下，0为非WIFI环境

            //设置接收者
            List<com.igetui.api.openservice.igetui.Target> targetList = new List<com.igetui.api.openservice.igetui.Target>();
            com.igetui.api.openservice.igetui.Target target1 = new com.igetui.api.openservice.igetui.Target();
            target1.appId = APPID;
            //target1.clientId = CLIENTID;
            target1.alias = ALIAS;

            // 如需要，可以设置多个接收者
            com.igetui.api.openservice.igetui.Target target2 = new com.igetui.api.openservice.igetui.Target();
            target2.appId = APPID;
            //target2.clientId = "f563cffaba68587e7ff2f23110f6defd";
            target2.alias = ALIAS1;

            targetList.Add(target1);
            targetList.Add(target2);

            String contentId = push.getContentId(message, "ToList_任务组名");
            String pushResult = push.pushMessageToList(contentId, targetList);
            System.Console.WriteLine("-----------------------------------------------");
            System.Console.WriteLine("服务端返回结果:" + pushResult);
        }

        //pushMessageToApp接口测试代码
        private static void pushMessageToApp()
        {
            IGtPush push = new IGtPush(HOST, APPKEY, MASTERSECRET);

            AppMessage message = new AppMessage();
            /*消息模版：
                1.TransmissionTemplate:透传模板
                2.LinkTemplate:通知链接模板
                3.NotificationTemplate：通知透传模板
                4.NotyPopLoadTemplate：通知弹框下载模板
             */

            TransmissionTemplate template =  TransmissionTemplateDemo();
            //NotificationTemplate template =  NotificationTemplateDemo();
            //LinkTemplate template = LinkTemplateDemo();
            //NotyPopLoadTemplate template = NotyPopLoadTemplateDemo();
            template.TransmissionContent = "测试";

            message.IsOffline = true;                         // 用户当前不在线时，是否离线存储,可选
            message.OfflineExpireTime = 1000 * 3600 * 12;            // 离线有效时间，单位为毫秒，可选
            message.Data = template;
            //message.PushNetWorkType = 0;            //判断是否客户端是否wifi环境下推送，1为在WIFI环境下，0为非WIFI环境
            //message.Speed = 1000;

            List<String> appIdList = new List<string>();
            appIdList.Add(APPID);

            List<String> phoneTypeList = new List<string>();    //通知接收者的手机操作系统类型
            //phoneTypeList.Add("ANDROID");
			//phoneTypeList.Add("IOS");

            List<String> provinceList = new List<string>();     //通知接收者所在省份
            //provinceList.Add("浙江");
            //provinceList.Add("上海");
            //provinceList.Add("北京");

            List<String> tagList = new List<string>();
            //tagList.Add("中文");

            message.AppIdList = appIdList;
            message.PhoneTypeList = phoneTypeList;
            message.ProvinceList = provinceList;
            message.TagList = tagList;


            String pushResult = push.pushMessageToApp(message, "toAPP任务别名");
            System.Console.WriteLine("-----------------------------------------------");
            System.Console.WriteLine("服务端返回结果：" + pushResult);
        }


        /*
         * 
         * 所有推送接口均支持四个消息模板，依次为透传模板，通知透传模板，通知链接模板，通知弹框下载模板
         * 注：IOS离线推送需通过APN进行转发，需填写pushInfo字段，目前仅不支持通知弹框下载功能
         *
         */
        //透传模板动作内容
        public  static TransmissionTemplate TransmissionTemplateDemo()
        {
            TransmissionTemplate template = new TransmissionTemplate();
            template.AppId = APPID;
            template.AppKey = APPKEY;
            template.TransmissionType = "1";            //应用启动类型，1：强制应用启动 2：等待应用启动
            template.TransmissionContent = "";  //透传内容

            //iOS简单推送
            //APNPayload apnpayload = new APNPayload();
            //SimpleAlertMsg alertMsg = new SimpleAlertMsg("alertMsg");
            //apnpayload.AlertMsg = alertMsg;
            //apnpayload.Badge = 11;
            //apnpayload.ContentAvailable = 1;
            //apnpayload.Category = "";
            //apnpayload.Sound = "";
            //apnpayload.addCustomMsg("", "");
            //template.setAPNInfo(apnpayload);

            //APN高级推送
            APNPayload apnpayload = new APNPayload();
            DictionaryAlertMsg alertMsg = new DictionaryAlertMsg();
            alertMsg.Body = "Body";
            alertMsg.ActionLocKey = "ActionLocKey";
            alertMsg.LocKey = "LocKey";
            alertMsg.addLocArg("LocArg");
            alertMsg.LaunchImage = "LaunchImage";
            //IOS8.2支持字段
            alertMsg.Title = "Title";
            alertMsg.TitleLocKey = "TitleLocKey";
            alertMsg.addTitleLocArg("TitleLocArg");

            apnpayload.AlertMsg = alertMsg;
            apnpayload.Badge = 10;
            apnpayload.ContentAvailable = 1;
            //apnpayload.Category = "";
            apnpayload.Sound = "test1.wav";
            apnpayload.addCustomMsg("payload", "payload");
            template.setAPNInfo(apnpayload);


            //设置客户端展示时间
            //String begin = "2015-03-06 14:28:10";
            //String end = "2015-03-06 14:38:20";
            //template.setDuration(begin, end);

            return template;
        }

        //通知透传模板动作内容
        public static NotificationTemplate NotificationTemplateDemo()
        {
            NotificationTemplate template = new NotificationTemplate();
            template.AppId = APPID;
            template.AppKey = APPKEY;
            template.Title = "请填写通知标题";         //通知栏标题
            template.Text = "请填写通知内容";          //通知栏内容
            template.Logo = "";               //通知栏显示本地图片
            template.LogoURL = "";                    //通知栏显示网络图标

            template.TransmissionType = "1";          //应用启动类型，1：强制应用启动  2：等待应用启动
            template.TransmissionContent = "请填写透传内容";   //透传内容

            //设置客户端展示时间
            //String begin = "2015-03-06 14:36:10";
            //String end = "2015-03-06 14:46:20";
            //template.setDuration(begin, end);

            template.IsRing = true;                //接收到消息是否响铃，true：响铃 false：不响铃
            template.IsVibrate = true;               //接收到消息是否震动，true：震动 false：不震动
            template.IsClearable = true;             //接收到消息是否可清除，true：可清除 false：不可清除
            return template;
        }

        //通知链接动作内容
        public static LinkTemplate LinkTemplateDemo()
        {
            LinkTemplate template =new LinkTemplate();
            template.AppId = APPID;
            template.AppKey = APPKEY;
            template.Title = "请填写通知标题";         //通知栏标题
            template.Text = "请填写通知内容";          //通知栏内容
            template.Logo = "";               //通知栏显示本地图片
            template.LogoURL = "";  //通知栏显示网络图标，如无法读取，则显示本地默认图标，可为空
            template.Url="http://www.baidu.com";      //打开的链接地址

            template.IsRing = true;                 //接收到消息是否响铃，true：响铃 false：不响铃
            template.IsVibrate = true;               //接收到消息是否震动，true：震动 false：不震动
            template.IsClearable = true;             //接收到消息是否可清除，true：可清除 false：不可清除

            return template;
        }

        //通知弹框下载模板动作内容
        public static NotyPopLoadTemplate NotyPopLoadTemplateDemo()
        {
            NotyPopLoadTemplate template = new NotyPopLoadTemplate();
            template.AppId = APPID;
            template.AppKey = APPKEY;
            template.NotyTitle = "请填写通知标题";     //通知栏标题
            template.NotyContent = "请填写通知内容";   //通知栏内容
            template.NotyIcon = "icon.png";           //通知栏显示本地图片
            template.LogoURL = "http://www-igexin.qiniudn.com/wp-content/uploads/2013/08/logo_getui1.png";                    //通知栏显示网络图标
              
            template.PopTitle = "弹框标题";             //弹框显示标题
            template.PopContent = "弹框内容";           //弹框显示内容
            template.PopImage = "";                     //弹框显示图片
            template.PopButton1 = "下载";               //弹框左边按钮显示文本
            template.PopButton2 = "取消";               //弹框右边按钮显示文本

            template.LoadTitle = "下载标题";            //通知栏显示下载标题
            template.LoadIcon = "file://push.png";      //通知栏显示下载图标,可为空
            template.LoadUrl = "http://www.appchina.com/market/d/425201/cop.baidu_0/com.gexin.im.apk";//下载地址，不可为空

            template.IsActived = true;                  //应用安装完成后，是否自动启动
            template.IsAutoInstall = true;              //下载应用完成后，是否弹出安装界面，true：弹出安装界面，false：手动点击弹出安装界面

            template.IsBelled = true;                 //接收到消息是否响铃，true：响铃 false：不响铃
            template.IsVibrationed = true;               //接收到消息是否震动，true：震动 false：不震动
            template.IsCleared = true;             //接收到消息是否可清除，true：可清除 false：不可清除
            return template;
        }

        public static void getUserStatus()
        {
            IGtPush push = new IGtPush(HOST, APPKEY, MASTERSECRET);
            String ret = push.getClientIdStatus(APPID, CLIENTID);
            System.Console.WriteLine("-----------------------------------------------");
            Console.WriteLine("用户状态:" + ret);
        }
    }
}
