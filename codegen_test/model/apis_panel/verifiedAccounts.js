/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var VerifiedAccounts = function () {
    /*
        @params obj 'data params'
            account_id   'integer' account id in query
            nickname   'string' nickname in query
            category   'string' category in query
            organization   'string' organization in query
            tag_name   'string' tag name in query
            date_start   'string' start date in query
            date_end   'string' end date in query
            is_star   'boolean' is star in query
            limit   'integer' limit number
            offset   'integer' offset number
            page   'integer' page number
            per_page   'integer' per_page number
            
        @success
            status 200    type:array
            category   'string' 
            account   'ref' 
            account_id   'integer' 
            order_score   'integer' 
            organization   'string' 
            date_created   'ref' 
            
    */
    this.get = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/verified_accounts",
            method: "GET",
            data: {
                account_id: obj.account_id,
                nickname: obj.nickname,
                category: obj.category,
                organization: obj.organization,
                tag_name: obj.tag_name,
                date_start: obj.date_start,
                date_end: obj.date_end,
                is_star: obj.is_star,
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
            category   'string' 
            organization   'string' 
            account_id   'integer' 
            
        @success
            status 201    type:object
            category   'string' 
            account   'ref' 
            account_id   'integer' 
            order_score   'integer' 
            organization   'string' 
            date_created   'ref' 
            
    */
    this.post = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/verified_accounts",
            method: "POST",
            data: {
                category: obj.category,
                organization: obj.organization,
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
    VerifiedAccounts: new VerifiedAccounts
};