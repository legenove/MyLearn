/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var AppAccountsSelf = function () {
    /*
        @params obj 'data params'
            title   'ref' 
            introduction   'ref' 
            price   'ref' 
            is_answer_free_in_30mins   'boolean' 
            avatar   'ref' 
            is_receive_inquiry   'boolean' 
            
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
            url: "/app/accounts/self",
            method: "PUT",
            data: {
                title: obj.title,
                introduction: obj.introduction,
                price: obj.price,
                is_answer_free_in_30mins: obj.is_answer_free_in_30mins,
                avatar: obj.avatar,
                is_receive_inquiry: obj.is_receive_inquiry
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
    AppAccountsSelf: new AppAccountsSelf
};