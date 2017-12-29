/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var BlackAccountsId = function () {
    /*
        @params obj 'data params'
            id   'integer' int id in query
            
        @success
            status 200    type:object
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
            url: "/black_accounts/" + obj.id + "",
            method: "GET",
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
            id   'integer' int id in query
            comment   'string' 
            gravity   'integer' 
            
        @success
            status 200    type:object
            comment   'string' 
            account   'ref' 
            account_id   'integer' 
            date_updated   'ref' 
            gravity   'integer' 
            date_created   'ref' 
            
    */
    this.put = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/black_accounts/" + obj.id + "",
            method: "PUT",
            data: {
                comment: obj.comment,
                gravity: obj.gravity
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
            id   'integer' int id in query
            
        @success
            status 204    type:object
            ok   'boolean' 
            
    */
    this.delete = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/black_accounts/" + obj.id + "",
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
    BlackAccountsId: new BlackAccountsId
};