/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var RolesIdAccounts = function () {
    /*
        @params obj 'data params'
            id   'integer' int id in query
            account_ids   'array' 
            
        @success
            status 200    type:object
            ok   'boolean' 
            
    */
    this.post = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/roles/" + obj.id + "/accounts",
            method: "POST",
            data: {
                account_ids: obj.account_ids
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
    RolesIdAccounts: new RolesIdAccounts
};