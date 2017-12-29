/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var WeixinAccessToken = function () {
    /*
        @params obj 'data params'
            code   'string' weixin code in query
            
        @success
            status 200    type:object
            openid   'string' 
            access_token   'string' 
            unionid   'string' 
            expires_in   'integer' 
            scope   'string' 
            refresh_token   'string' 
            
    */
    this.get = function (that, obj){
        http.request({
            baseUrl: "/v1",
            url: "/weixin/access_token",
            method: "GET",
            data: {
                code: obj.code
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
    WeixinAccessToken: new WeixinAccessToken
};