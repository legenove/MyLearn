/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var BatchAccounts = function () {
    /*
        @params obj 'data params'
            account_id   'array' account ids in query
            
        @success
            status 200    type:array
            questions_count   'integer' 
            is_verified   'boolean' 
            answers_count   'integer' 
            
    */
    this.get = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/batch/accounts",
            method: "GET",
            data: {
                account_id: obj.account_id
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
    BatchAccounts: new BatchAccounts
};