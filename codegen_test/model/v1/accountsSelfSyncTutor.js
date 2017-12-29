/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var AccountsSelfSyncTutor = function () {
    /*
        @params obj 'data params'
            
        @success
            status 200    type:object
            following_count   'integer' 
            mobile   'string' 
            frozen_time_remaining   'integer' 
            has_answer_probability   'boolean' 
            answer_probability   'string' 
            is_bound_weixin_app   'boolean' 
            is_bound_weixin   'boolean' 
            verify_category   'string' 
            
    */
    this.put = function (that, obj){
        http.request({
            baseUrl: "/v1",
            url: "/accounts/self/sync_tutor",
            method: "PUT",
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
    AccountsSelfSyncTutor: new AccountsSelfSyncTutor
};