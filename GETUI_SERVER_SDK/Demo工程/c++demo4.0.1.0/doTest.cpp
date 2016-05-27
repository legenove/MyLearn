#include "IGtPush.h"
#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <string>
#ifdef WIN32
#include <windows.h>
#endif

using namespace std;
static void printResult(IPushResult &result);
static void printQueryResult(IQueryResult &result);
//-----------------------------------------------------------------------------------------------------------------------------

//tosingle
void tosingletest();

//tolist
void tolisttest();

//toapp
void toapptest();

//查询用户
void getuserinfo();

//查询推送
void getappinfo();

//按taskid查询
void getresult();

//toapnsingle
void toapnsingletest();

//toapnlist
void toapnlisttest();

//单个别名绑定
void bindAliastest();

//别名绑定多个cid
void bindAliasListtest();

//通过cid查询别名
void queryAliastest();

//通过别名查询cid
void queryClientIdtest();

//解绑单个cid
void unBindAliastest();

//解绑别名所有cid
void unBindAliasAlltest();

//任务停止
void stopTaskTest(); 

// http的域名
//static char *host ="http://sdk.open.api.igexin.com/apiex.htm";

//https的域名
static char *host ="https://api.getui.com/apiex.htm";


static char *appId = "";
static char *appKey = "";
static char *masterSecret = "";
static char *cid = "";
static char *dt="";


/*	1.透传消息模板	*/
void TransmissionTemplateDemo(TransmissionTemplate* templ)
{
    templ->t.appId = appId;
    templ->t.appKey = appKey;
     //应用启动类型，1：强制应用启动 2：等待应用启动
    templ->transmissionType = 1;          
    //透传内容  
    templ->transmissionContent = "{\"sound\":\"test1.wav\",\"badge\":4}";
	templ->t.pushInfo.badge=4;
	templ->t.pushInfo.sound="text1.wav";
	templ->t.pushInfo.contentAvailable=1;
	templ->t.pushInfo.category="";
	Entry cmsg = {0};//
	strcpy(cmsg.key,"");
	strcpy(cmsg.value,"");
	templ->t.pushInfo.cmsg.size=2;
	templ->t.pushInfo.cmsg.map=&cmsg;
	templ->t.pushInfo.body="";
	templ->t.pushInfo.actionLocKey="";
	templ->t.pushInfo.locKey="";
	ListItem locargs[2]={"",""};//
	templ->t.pushInfo.locArgs.size=2;
	templ->t.pushInfo.locArgs.item=locargs;
	templ->t.pushInfo.launchImage="";
	//IOS8.2以上支持
	templ->t.pushInfo.title="";
	templ->t.pushInfo.titleLocKey="";
	ListItem titlelocargs[2]={"",""};//
	templ->t.pushInfo.titleLocArgs.size=2;
	templ->t.pushInfo.titleLocArgs.item=titlelocargs;

	//templ->t.duration_start="2015-07-10 18:00:00";
	//templ->t.duration_end="2015-07-10 19:00:00";
} 

/*	2.通知弹框下载消息模板	*/
void NotyPopLoadTemplateDemo(NotyPopLoadTemplate* templ)
{
    templ->t.appId = appId;
    templ->t.appKey = appKey;
    //通知栏标题
    templ->notyTitle = "请填写通知标题";     
    //通知栏内容
    templ->notyContent = "请填写通知内容";   
    //通知栏显示本地图片
    templ->notyIcon = "icon.png";           
    //通知栏显示网络图标
    templ->logoUrl = "http://www-igexin.qiniudn.com/wp-content/uploads/2013/08/logo_getui1.png";                    
    //弹框显示标题
    templ->popTitle = "弹框标题";    
    //弹框显示内容    
    templ->popContent = "弹框内容";   
    //弹框显示图片    
    templ->popImage = "";        
    //弹框左边按钮显示文本    
    templ->popButton1 = "下载";     
    //弹框右边按钮显示文本    
    templ->popButton2 = "取消";               
    //通知栏显示下载标题
    templ->loadTitle = "下载标题";           
    //通知栏显示下载图标,可为空 
    templ->loadIcon = "file://push.png";      
    //下载地址，不可为空
    templ->loadUrl = "http://www.appchina.com/market/d/425201/cop.baidu_0/com.gexin.im.apk";
    //应用安装完成后，是否自动启动
    templ->isActived = true;  
    //下载应用完成后，是否弹出安装界面，true：弹出安装界面，false：手动点击弹出安装界面 
    templ->isAutoInstall = true; 

	//templ->t.duration_start="2015-07-10 18:00:00";
	//templ->t.duration_end="2015-07-10 19:00:00";
    //接收到消息是否响铃，GT_ON：响铃 GT_OFF：不响铃
    //templ->isBelled = GT_OFF;            
    ////接收到消息是否震动，GT_ON：震动 GT_OFF：不震动   
    //templ->isVibrationed = GT_OFF;              
    ////接收到消息是否可清除，GT_ON：可清除 GT_OFF：不可清除    
    //templ->isCleared = GT_OFF;            
} 


/*	3.通知透传消息模板	*/
void NotificationTemplateDemo(NotificationTemplate* templ)
{
    templ->t.appId = appId;
    templ->t.appKey = appKey;
    //通知栏标题
    templ->title = "请填写通知标题";
    //通知栏内容
    templ->text = "请填写通知内容";
    //通知栏显示本地图片
    templ->logo = "";
    //通知栏显示网络图标
    templ->logoUrl = "";
    //应用启动类型，1：强制应用启动 2：等待应用启动
    templ->transmissionType = 1;
    //透传内容
    templ->transmissionContent = "请填写透传内容";
	//templ->t.duration_start="2015-07-10 18:00:00";
	//templ->t.duration_end="2015-07-10 19:00:00";
    ////接收到消息是否响铃，GT_ON：响铃 GT_OFF：不响铃
    //templ->isRing = GT_ON;
    ////接收到消息是否震动，GT_ON：震动 GT_OFF：不震动
    //templ->isVibrate = GT_ON;
    ////接收到消息是否可清除，GT_ON：可清除 GT_OFF：不可清除
    //templ->isClearable = GT_ON;
}
/*	4.通知打开网页消息模板	*/
void LinkTemplateDemo(LinkTemplate* templ)
{
    templ->t.appId = appId;
    templ->t.appKey = appKey;
    //通知栏标题
    templ->title = "请填写通知标题";       
    //通知栏内容 
    templ->text = "请填写通知内容";       
    //通知栏显示本地图片 
    templ->logo = "";               
    //通知栏显示网络图标，如无法读取，则显示本地默认图标，可为空
    templ->logoUrl = "";  
    //打开的链接地址    
    templ->url="http://www.baidu.com";
	//templ->t.duration_start="2015-07-10 18:00:00";
	//templ->t.duration_end="2015-07-10 19:00:00";
    ////接收到消息是否响铃，GT_ON：响铃 GT_OFF：不响铃   
    //templ->isRing = GT_OFF;
    ////接收到消息是否震动，GT_ON：震动 GT_OFF：不震动   
    //templ->isVibrate = GT_OFF;              
    ////接收到消息是否可清除，GT_ON：可清除 GT_OFF：不可清除
    //templ->isClearable = GT_OFF;             
} 


int main(){
	// 注意：接口传入字符必须为UTF-8编码，因ASCII字符UTF－8编码后与原先一样，所以可以不编码，但中文等非ASCII字符必须编码
	// 如果返回的类似错误"post http data failed, code=6"，错误码可百度CURL返回的错误码是什么意思，如http://www.cnblogs.com/wainiwann/p/3492939.html
	Result r = pushInit(host, appKey, masterSecret, "编码");//"编码"两个字为固定写法，不需要做转换
	if(r!=SUCCESS){
		printf("pushInit for app failed: ret=%d\n", r);
		return -1;
	}
        tosingletest();
        //tolisttest();
        //toapptest();
	//getuserinfo();
	//getappinfo();
	//getresult();
	//toapnsingletest();
        //toapnlisttest();
	//bindAliastest();
	//bindAliasListtest();
	//queryAliastest();
	//queryClientIdtest();
	//unBindAliastest();
	//unBindAliasAlltest();
        //stopTaskTest();
	return 0;
}

//@test
void toapnlisttest(){

	//准备数据
	Message msg = {0};
	msg.isOffline = 1;//是否离线下发
	msg.offlineExpireTime = 1000*3600*2;//离线下发有效期 毫秒
	ListMessage listMsg = {0};
	listMsg.msg = msg;

	//模板
	//IOS自定义消息
	Entry cmsg = {0};
	strcpy(cmsg.key,"cmsg");
	strcpy(cmsg.value,"cmsg");

	//title-loc-args赋值
	ListItem titlelocargs[2]={"titlelocargs1","titlelocargs2"};

	//locargs赋值
	ListItem locargs[2]={"locargs1","locargs2"};


	APNTemplate templ = {0};
	templ.t.appId = appId;
    templ.t.appKey = appKey;

	templ.t.pushInfo.badge=4;
	templ.t.pushInfo.sound="";
	templ.t.pushInfo.contentAvailable=1;
	templ.t.pushInfo.category="";
	templ.t.pushInfo.cmsg.size=1;
	templ.t.pushInfo.cmsg.map = &cmsg;

	templ.t.pushInfo.body="body";
	templ.t.pushInfo.actionLocKey="";

	templ.t.pushInfo.locKey="lockey";
	templ.t.pushInfo.locArgs.size=2;
	templ.t.pushInfo.locArgs.item=locargs;

	templ.t.pushInfo.launchImage="launchimage";
	//IOS8.2以上版本支持
	templ.t.pushInfo.title="title";
	templ.t.pushInfo.titleLocKey="titlelockey";

	templ.t.pushInfo.titleLocArgs.size=2;
	templ.t.pushInfo.titleLocArgs.item=titlelocargs;

	//发送消息
	Result ret;
	char contentId[50] = "";
	ret = getAPNContentId(appKey, &templ, contentId, sizeof(contentId));
	if (ret == SUCCESS) {
		ListItem item;
		strcpy(item.item,dt);
		ListInfo target;
		target.size = 1;
		target.item = &item;
		 
        cout << "============pushApnMessageToList============" << endl;
		IPushResult result = {0};
        result = pushAPNMessageToList(appKey, appId, &target, contentId);
        printResult(result);
	}
}

//@test
void toapnsingletest(){
	//初始化
    Result r = pushInit(host, appKey, masterSecret, "编码");
	if(r!=SUCCESS){
		printf("pushInit for app failed: ret=%d\n", r);
		return;
	}

	//准备数据
	Message msg = {0};
	msg.isOffline = 1;//是否离线下发
	msg.offlineExpireTime = 1000*3600*2;//离线下发有效期 毫秒
	SingleMessage singleMsg = {0};
        singleMsg.msg = msg;

	//IOS自定义消息
	Entry cmsg = {0};
	strcpy(cmsg.key,"cmsg");
	strcpy(cmsg.value,"cmsg");

	//title-loc-args赋值
	ListItem titlelocargs[2]={"titlelocargs1","titlelocargs2"};

	//locargs赋值
	ListItem locargs[2]={"locargs1","locargs2"};


	APNTemplate templ = {0};
	templ.t.appId = appId;
    	templ.t.appKey = appKey;

	templ.t.pushInfo.badge=4;
	//templ.t.pushInfo.sound="test1.wav";
	//templ.t.pushInfo.contentAvailable=1;
	templ.t.pushInfo.category="";
	//templ.t.pushInfo.cmsg.size=1;
	//templ.t.pushInfo.cmsg.map = &cmsg;

	templ.t.pushInfo.body="body";
	templ.t.pushInfo.actionLocKey="";

	templ.t.pushInfo.locKey="";
	//templ.t.pushInfo.locArgs.size=2;
	//templ.t.pushInfo.locArgs.item=locargs;

	templ.t.pushInfo.launchImage="";
	//IOS8.2以上版本支持
	templ.t.pushInfo.title="";
	templ.t.pushInfo.titleLocKey="";

	//templ.t.pushInfo.titleLocArgs.size=2;
	//templ.t.pushInfo.titleLocArgs.item=titlelocargs;

	IPushResult result = {0};

	result = pushAPNMessageToSingle(appKey, &templ,appId, dt);
	//打印结果
	printResult(result);
}

//@test
void getresult(){

	IPushResult result = {0};
	result = getPushResult(appKey,"OSA-1126_3iZaaoJ5TQ7Q6gOEQmVfe1");
	printResult(result);
}


//@test
void getappinfo(){
	IQueryResult result = {0};
	result = queryAppPushDataByDate(appKey,appId,"20150709");
	printQueryResult(result);
}
//@test
void getuserinfo(){
	//初始化
	IQueryResult result = {0};
	result = queryAppUserDataByDate(appKey,appId,"20150709");
	printQueryResult(result);
}
//@test
void toapptest(){

	//准备数据
	Message msg = {0};
	msg.isOffline = 0;//是否离线下发
	msg.offlineExpireTime = 1000*3600*2;//离线下发有效期 毫秒
	msg.pushNetWorkType = 0;//0不限 1wifi

	AppMessage appMsg = {0};
	appMsg.msg = msg;
        appMsg.speed = 10000;//定速
	char* appList[] = {appId};
	appMsg.appIdList = appList;
	appMsg.appIdListSize = 1;

	IPushResult result = {0};
	//模板
	TransmissionTemplate tmpl= {0};
        TransmissionTemplateDemo(& tmpl);
	//result = pushMessageToApp(appKey, &appMsg, &tmpl, Transmission);

	//NotyPopLoadTemplate tmpl= {0};
 //   NotyPopLoadTemplateDemo(& tmpl);
	//result = pushMessageToApp(appKey, &appMsg, &tmpl, NotyPopLoad);

	//NotificationTemplate tmpl= {0};
 //   NotificationTemplateDemo(& tmpl);
	//result = pushMessageToApp(appKey, &appMsg, &tmpl, Notification);
	
	//LinkTemplate tmpl= {0};
   // LinkTemplateDemo(& tmpl);
	//result = pushMessageToApp(appKey, &appMsg, &tmpl, Link);
	printf("push before\n");
	result =pushMessageToAppByGroupName(appKey, &appMsg, &tmpl, Transmission,"TO_APP群推");
	printf("push after\n");
	//打印结果
	printResult(result);
}


//@test
void tolisttest(){

	//准备数据
	Message msg = {0};
	msg.isOffline = true;//是否离线下发
	msg.offlineExpireTime = 1000*3600*2;//离线下发有效期 毫秒
	msg.pushNetWorkType = 0;//0不限 1wifi
	ListMessage listMsg = {0};
	listMsg.msg = msg;

	//NotificationTemplate tmpl= {0};
 //   NotificationTemplateDemo(& tmpl);
	////发送消息
	//Result ret;
	//char contentId[50] = "";
	//ret = getContentId(appKey, &listMsg, &tmpl, Notification, contentId, sizeof(contentId));

	//NotyPopLoadTemplate tmpl= {0};
 //   NotyPopLoadTemplateDemo(& tmpl);
	//Result ret;
	//char contentId[50] = "";
	//ret = getContentId(appKey, &listMsg, &tmpl, NotyPopLoad, contentId, sizeof(contentId));


	//LinkTemplate tmpl= {0};
  //  LinkTemplateDemo(& tmpl);
	//Result ret;
	//char contentId[50] = "";
	//ret = getContentId(appKey, &listMsg, &tmpl, Link, contentId, sizeof(contentId));

	TransmissionTemplate tmpl= {0};
  TransmissionTemplateDemo(& tmpl);
	Result ret;
	char contentId[50] = "";
	ret = getContentId(appKey, &listMsg, &tmpl, Transmission, contentId, sizeof(contentId));


	if (ret == SUCCESS) {
		Target* targetList = new Target[1];
		memset((void*)targetList, 0, sizeof(Target));
		for(int i=0;i<1;++i){
        targetList[i].appId = appId;
        //targetList[i].clientId = cid;
		targetList[i].alias = "test";
		}
		PushDetail details[1] = {0};

        //cout << "============pushMessageToList============" << endl;
		IPushResult result = {0};
        result = pushMessageToList(appKey, contentId, targetList,1, details);
		cout<<details->cid<<","<<details->ret<<endl;
        printResult(result);

        ret = cancelContentId(appKey, contentId);
        cout << "cancelContentId ret=" << ret << endl;
	}

}

//@test
void tosingletest(){

	//准备数据
	Message msg = {0};
	msg.isOffline = true;//是否离线下发
	msg.offlineExpireTime = 1000*3600*2;//离线下发有效期 毫秒
	msg.pushNetWorkType = 0;//0不限 1wifi
	SingleMessage singleMsg = {0};
    singleMsg.msg = msg;

	//目标用户
    Target target = {0};
    target.appId = appId;
    //target.clientId = cid;
	target.alias = "test";
	IPushResult result = {0};


	TransmissionTemplate tmpl= {0};
  TransmissionTemplateDemo(& tmpl);
	result = pushMessageToSingle(appKey, &singleMsg, &tmpl, Transmission, &target);

	//NotyPopLoadTemplate tmpl= {0};
  //  NotyPopLoadTemplateDemo(& tmpl);
	//result = pushMessageToSingle(appKey, &singleMsg, &tmpl, NotyPopLoad, &target);

	//NotificationTemplate tmpl= {0};
 //   NotificationTemplateDemo(& tmpl);
	//result = pushMessageToSingle(appKey, &singleMsg, &tmpl, Notification, &target);
	
	//LinkTemplate tmpl= {0};
 //   LinkTemplateDemo(& tmpl);
	//result = pushMessageToSingle(appKey, &singleMsg, &tmpl, Link, &target);

	//打印结果
	printResult(result);
}

void bindAliasListtest(){
	Target* targetList = new Target[1];
	targetList->clientId = cid;
	targetList->alias = "test";
	IPushResult result = bindAliasList(appKey, appId, targetList, 1);
	printResult(result);
	delete []targetList;
}

void bindAliastest(){
	IPushResult result = bindAlias(appKey, appId, "test", cid);
	printResult(result);
}

void queryAliastest(){
	IPushResult result = queryAlias(appKey, appId, cid);
	printResult(result);
}

void queryClientIdtest() {
	char* list = NULL;
	IPushResult result = queryClientId(appKey, appId, "test", &list);
	
	printResult(result);

	if(list != NULL) {
		cout << "cidlist:" << list<<endl;

		//释放资源
		releaseMem(list);
	}
}

void unBindAliastest() {
	IPushResult result = unBindAlias(appKey, appId, "test", cid);
	printResult(result);
}

void unBindAliasAlltest() {
	IPushResult result = unBindAliasAll(appKey, appId, "test");
	printResult(result);
}

void stopTaskTest() {
        Result result = pushStop(appKey,"OSA-1126_lsJPsulDip7Pcd5JqWgUe8");
        printf("%d\n", result);
}
///-----------------------------------------------------------------------------------------------------------------------------





static void printResult(IPushResult &result) {
    cout << "print result:-------------" << endl;
    for (int i = 0; i < result.size; i++) {
        cout << result.entry[i].key << ": " << result.entry[i].value << endl;
    }
    cout << "print end:----------------" << endl;
}

static void printQueryResult(IQueryResult &result) {
    cout << "print result:-------------" << endl;
	cout <<"result:"<<result.result<<endl;
    for (int i = 0; i < result.size; i++) {
        cout << result.data[i].key << ": " << result.data[i].value << endl;
    }
    cout << "print end:----------------" << endl;
}
