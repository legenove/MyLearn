/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var OauthBind = function () {
    /*
        @params obj 'data params'
            password   'string' 微信token
            auth_approach   'string' 
            identity   'string' 微信openid
            
        @success
            status 201    type:object
            ok   'boolean' 
            
    */
    this.post = function (that, obj){
        http.request({
            baseUrl: "/v1",
            url: "/oauth/bind",
            method: "POST",
            data: {
                password: obj.password,
                auth_approach: obj.auth_approach || "weixin_mp",
                identity: obj.identity
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
    OauthBind: new OauthBind
};