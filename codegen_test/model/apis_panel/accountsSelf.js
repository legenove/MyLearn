/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var AccountsSelf = function () {
    /*
        @params obj 'data params'
            
        @success
            status 200    type:object
            nickname   'ref' 
            is_admin   'boolean' 
            id   'ref' 
            permission_codes   'array' 
            
    */
    this.get = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/accounts/self",
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
    AccountsSelf: new AccountsSelf
};