/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var AccountsMobile = function () {
    /*
        @params obj 'data params'
            username   'string' 
            code   'integer' 
            mobile   'ref' 
            auth_approach   'string' 
            avatar   'string' 
            password   'string' 
            nickname   'string' 
            
        @success
            status 201    type:object
            following_count   'integer' 
            mobile   'string' 
            frozen_time_remaining   'integer' 
            has_answer_probability   'boolean' 
            answer_probability   'string' 
            is_bound_weixin_app   'boolean' 
            is_bound_weixin   'boolean' 
            verify_category   'string' 
            
    */
    this.post = function (that, obj){
        http.request({
            baseUrl: "/v1",
            url: "/accounts/mobile",
            method: "POST",
            data: {
                username: obj.username,
                code: obj.code,
                mobile: obj.mobile,
                auth_approach: obj.auth_approach,
                avatar: obj.avatar,
                password: obj.password,
                nickname: obj.nickname
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
    AccountsMobile: new AccountsMobile
};