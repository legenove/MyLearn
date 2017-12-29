/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var Qrcode = function () {
    /*
        @params obj 'data params'
            scene_id   'integer' 
            expire_seconds   'integer' 
            action_name   'string' 
            scene_str   'string' 
            
        @success
            status 201    type:object
            url   'string' 二维码图片解析后的地址
            expire_seconds   'integer' 
            ticket   'string' 
            qrcode_url   'string' 二维码请求地址使用ticket换取
            
    */
    this.post = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/qrcode",
            method: "POST",
            data: {
                scene_id: obj.scene_id,
                expire_seconds: obj.expire_seconds,
                action_name: obj.action_name,
                scene_str: obj.scene_str
                },
            success: function (res) {
                typeof obj.success === 'function' && obj.success(res);
            },
            fail: function (res) {
                typeof obj.fail === 'function' && obj.fail(res);
            },
            complete: function (res) {
                typeof obj.complete === 'function' && obj.complete(res);
            }
        })
    };
    

};

module.exports = {
    Qrcode: new Qrcode
};