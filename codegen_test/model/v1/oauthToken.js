/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var OauthToken = function () {
    /*
        @params obj 'data params'
            username   'string' 手机号/微信openid
            password   'string' 密码/微信token
            auth_approach   'string' 通道
            grant_type   'string' 认证类型 默认密码认证
            
        @success
            status 201    type:object
            scopes   'string' token scopes
            account_id   'integer' 
            is_new_weixin_app   'boolean' 
            access_token   'string' 
            expires_in   'integer' 
            token_type   'string' 
            refresh_token   'string' 
            
    */
    this.post = function (that, obj){
        http.request({
            baseUrl: "/v1",
            url: "/oauth/token",
            method: "POST",
            data: {
                username: obj.username,
                password: obj.password,
                auth_approach: obj.auth_approach || "weixin_mp",
                grant_type: obj.grant_type || "password"
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
    OauthToken: new OauthToken
};