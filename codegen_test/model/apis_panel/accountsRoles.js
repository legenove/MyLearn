/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var AccountsRoles = function () {
    /*
        @params obj 'data params'
            account_id   'integer' account id in query
            nickname   'string' nickname in query
            role_id   'integer' role id in query
            limit   'integer' limit number
            offset   'integer' offset number
            page   'integer' page number
            per_page   'integer' per_page number
            
        @success
            status 200    type:array
            account   'ref' 
            role   'ref' 
            account_id   'integer' 
            role_id   'integer' 
            
    */
    this.get = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/accounts/roles",
            method: "GET",
            data: {
                account_id: obj.account_id,
                nickname: obj.nickname,
                role_id: obj.role_id,
                limit: obj.limit,
                offset: obj.offset,
                page: obj.page,
                per_page: obj.per_page
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
    AccountsRoles: new AccountsRoles
};