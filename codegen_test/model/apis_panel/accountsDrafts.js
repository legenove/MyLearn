/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var AccountsDrafts = function () {
    /*
        @params obj 'data params'
            account_id   'integer' account id in query
            nickname   'string' nickname in query
            status   'string' account draft status in query
            order_by   'string' order by in query
            limit   'integer' limit number
            offset   'integer' offset number
            page   'integer' page number
            per_page   'integer' per_page number
            
        @success
            status 200    type:array
            account   'ref' 
            
    */
    this.get = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/accounts/drafts",
            method: "GET",
            data: {
                account_id: obj.account_id,
                nickname: obj.nickname,
                status: obj.status,
                order_by: obj.order_by,
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
    AccountsDrafts: new AccountsDrafts
};