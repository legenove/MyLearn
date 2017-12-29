/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var AccountsDraftsId = function () {
    /*
        @params obj 'data params'
            id   'integer' int id in query
            
        @success
            status 200    type:object
            account   'ref' 
            
    */
    this.get = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/accounts/drafts/" + obj.id + "",
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
            status   'string' 
            reason   'string' 
            
        @success
            status 200    type:object
            status   'string' 
            operator_id   'string' 
            account_id   'integer' 
            title   'string' 
            introduction   'string' 
            date_updated   'ref' 
            reason   'string' 
            avatar   'string' 
            date_created   'ref' 
            nickname   'string' 
            id   'integer' 
            
    */
    this.put = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/accounts/drafts/" + obj.id + "",
            method: "PUT",
            data: {
                status: obj.status,
                reason: obj.reason
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
    AccountsDraftsId: new AccountsDraftsId
};