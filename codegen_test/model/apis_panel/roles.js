/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var Roles = function () {
    /*
        @params obj 'data params'
            type   'string' role type in query
            limit   'integer' limit number
            offset   'integer' offset number
            page   'integer' page number
            per_page   'integer' per_page number
            
        @success
            status 200    type:array
            description   'string' 
            date_updated   'string' 
            permission_codes   'array' 
            date_created   'string' 
            type   'string' 
            id   'integer' 
            name   'string' 
            
    */
    this.get = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/roles",
            method: "GET",
            data: {
                type: obj.type,
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
            type   'string' 
            name   'string' 
            permission_codes   'array' 
            description   'string' 
            
        @success
            status 201    type:object
            description   'string' 
            date_updated   'string' 
            permission_codes   'array' 
            date_created   'string' 
            type   'string' 
            id   'integer' 
            name   'string' 
            
    */
    this.post = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/roles",
            method: "POST",
            data: {
                type: obj.type,
                name: obj.name,
                permission_codes: obj.permission_codes,
                description: obj.description
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
    Roles: new Roles
};