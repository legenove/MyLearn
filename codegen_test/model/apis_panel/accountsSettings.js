/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var AccountsSettings = function () {
    /*
        @params obj 'data params'
            account_id   'integer' account id in query
            nickname   'string' nickname in query
            key   'string' setting key in query
            _value   'string' 
            is_star   'boolean' is star in query
            category   'string' category in query
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
            url: "/accounts/settings",
            method: "GET",
            data: {
                account_id: obj.account_id,
                nickname: obj.nickname,
                key: obj.key,
                _value: obj._value,
                is_star: obj.is_star,
                category: obj.category,
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
            _value   'string' 
            account_ids   'array' 
            key   'string' 
            
        @success
            status 200    type:object
            account_id   'integer' 
            date_updated   'string' 
            _value   'string' 
            key   'string' 
            date_created   'string' 
            id   'integer' 
            
    */
    this.post = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/accounts/settings",
            method: "POST",
            data: {
                _value: obj._value,
                account_ids: obj.account_ids,
                key: obj.key
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
    AccountsSettings: new AccountsSettings
};