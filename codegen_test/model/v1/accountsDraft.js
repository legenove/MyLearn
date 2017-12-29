/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var AccountsDraft = function () {
    /*
        @params obj 'data params'
            
        @success
            status 200    type:object
            status   'string' 
            title   'string' 
            introduction   'string' 
            date_updated   'ref' 
            reason   'string' 
            avatar   'string' 
            date_created   'ref' 
            nickname   'string' 
            
    */
    this.get = function (that, obj){
        http.request({
            baseUrl: "/v1",
            url: "/accounts/draft",
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
    AccountsDraft: new AccountsDraft
};