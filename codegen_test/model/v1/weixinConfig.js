/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var WeixinConfig = function () {
    /*
        @params obj 'data params'
            url   'ref' 
            
        @success
            status 200    type:object
            timestamp   'string' 
            nonceStr   'string' 
            appId   'string' 
            signature   'string' 
            
    */
    this.post = function (that, obj){
        http.request({
            baseUrl: "/v1",
            url: "/weixin/config",
            method: "POST",
            data: {
                url: obj.url
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
    WeixinConfig: new WeixinConfig
};