/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var QuestionsLibrariesId = function () {
    /*
        @params obj 'data params'
            id   'string' string id in path
            
        @success
            status 200    type:object
            answers_count   'integer' 
            
    */
    this.get = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/questions/libraries/" + obj.id + "",
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
            id   'string' string id in path
            content   'ref' 
            is_active   'boolean' 
            account_id   'ref' 
            offer   'ref' 
            
        @success
            status 200    type:object
            operator_id   'ref' 
            account_id   'ref' 
            offer   'ref' 
            date_updated   'ref' 
            is_active   'boolean' 
            content   'ref' 
            date_created   'ref' 
            type   'string' 
            id   'ref' 
            
    */
    this.put = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/questions/libraries/" + obj.id + "",
            method: "PUT",
            data: {
                content: obj.content,
                is_active: obj.is_active,
                account_id: obj.account_id,
                offer: obj.offer
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
            id   'string' string id in path
            
        @success
            status 204    type:object
            ok   'boolean' 
            
    */
    this.delete = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/questions/libraries/" + obj.id + "",
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
    QuestionsLibrariesId: new QuestionsLibrariesId
};