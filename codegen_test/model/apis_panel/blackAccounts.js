/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var BlackAccounts = function () {
    /*
        @params obj 'data params'
            account_id   'integer' account id in query
            nickname   'string' nickname in query
            limit   'integer' limit number
            offset   'integer' offset number
            page   'integer' page number
            per_page   'integer' per_page number
            
        @success
            status 200    type:array
            comment   'string' 
            account   'ref' 
            account_id   'integer' 
            date_updated   'ref' 
            gravity   'integer' 
            date_created   'ref' 
            
    */
    this.get = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/black_accounts",
            method: "GET",
            data: {
                account_id: obj.account_id,
                nickname: obj.nickname,
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
    
    /*
        @params obj 'data params'
            account_id   'integer' 
            
        @success
            status 201    type:object
            comment   'string' 
            account   'ref' 
            account_id   'integer' 
            date_updated   'ref' 
            gravity   'integer' 
            date_created   'ref' 
            
    */
    this.post = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/black_accounts",
            method: "POST",
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
    BlackAccounts: new BlackAccounts
};