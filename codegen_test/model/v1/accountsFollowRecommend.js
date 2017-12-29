/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var AccountsFollowRecommend = function () {
    /*
        @params obj 'data params'
            
        @success
            status 200    type:array
            listenings_count   'integer' 
            answers_count   'integer' 
            visitor_count   'integer' 
            
    */
    this.get = function (that, obj){
        http.request({
            baseUrl: "/v1",
            url: "/accounts/follow_recommend",
            method: "GET",
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
    AccountsFollowRecommend: new AccountsFollowRecommend
};