/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var AccountsAccountIdRolesRoleId = function () {
    /*
        @params obj 'data params'
            account_id   'integer' account id in path
            role_id   'integer' role id in path
            
        @success
            status 204    type:object
            ok   'boolean' 
            
    */
    this.delete = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/accounts/" + obj.account_id + "/roles/" + obj.role_id + "",
            method: "DELETE",
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
    AccountsAccountIdRolesRoleId: new AccountsAccountIdRolesRoleId
};