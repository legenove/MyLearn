/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var VerifiedAccountsId = function () {
    /*
        @params obj 'data params'
            id   'integer' int id in query
            
        @success
            status 200    type:object
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
            url: "/verified_accounts/" + obj.id + "",
            method: "GET",
            data: {
                id: obj.id
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
            category   'string' 
            organization   'string' 
            order_score   'integer' 
            
        @success
            status 200    type:object
            category   'string' 
            account   'ref' 
            account_id   'integer' 
            order_score   'integer' 
            organization   'string' 
            date_created   'ref' 
            
    */
    this.put = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/verified_accounts/" + obj.id + "",
            method: "PUT",
            data: {
                id: obj.id,
                category: obj.category,
                organization: obj.organization,
                order_score: obj.order_score
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
            url: "/verified_accounts/" + obj.id + "",
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
    VerifiedAccountsId: new VerifiedAccountsId
};