/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var Admins = function () {
    /*
        @params obj 'data params'
            id   'integer' int id in query
            nickname   'string' nickname in query
            limit   'integer' limit number
            offset   'integer' offset number
            page   'integer' page number
            per_page   'integer' per_page number
            
        @success
            status 200    type:array
            role_ids   'array' 
            nickname   'string' 
            id   'integer' 
            avatar   'string' 
            
    */
    this.get = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/admins",
            method: "GET",
            data: {
                id: obj.id,
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
            mobile   'string' 
            role_ids   'array' 
            account_id   'integer' 
            
        @success
            status 201    type:object
            role_ids   'array' 
            nickname   'string' 
            id   'integer' 
            avatar   'string' 
            
    */
    this.post = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/admins",
            method: "POST",
            data: {
                mobile: obj.mobile,
                role_ids: obj.role_ids,
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
    Admins: new Admins
};